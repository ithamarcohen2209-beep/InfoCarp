"""Validate the standalone public site without application dependencies."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
PAGES = ('index.html', 'privacy.html', 'support.html', 'terms.html',
         'account-deletion.html', 'security.html')
ASSETS = ('style.css', 'assets/infocarp-logo.png')
PUBLIC_FILES = frozenset(PAGES + ASSETS + (
    'README.md', 'AUDIT.md', 'CHANGELOG.md', 'SECURITY.md', '.gitignore',
    'requirements-dev.txt', 'pyproject.toml',
    'scripts/__init__.py', 'scripts/build.py', 'scripts/validate.py',
    'tests/test_site.py', '.github/workflows/validate-public-site.yml',
))
VOID = frozenset('area base br col embed hr img input link meta param source track wbr'.split())
SECRET_PATTERNS = (
    r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----',
    r'\bAIza[0-9A-Za-z_-]{35}\b',
    r'\b(?:ghp|gho|ghu|ghs|ghr)_[0-9A-Za-z]{30,}\b',
    r'\bgithub_pat_[0-9A-Za-z_]{60,}\b',
    r'\bsk-(?:proj-)?[0-9A-Za-z_-]{30,}\b',
    r'\bAKIA[0-9A-Z]{16}\b',
    r'\beyJ[0-9A-Za-z_-]{12,}\.eyJ[0-9A-Za-z_-]{12,}\.[0-9A-Za-z_-]{20,}\b',
)


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.stack: list[str] = []
        self.links: list[str] = []
        self.ids: set[str] = set()
        self.errors: list[str] = []
        self.doctype = False
        self.lang = False
        self.title = False
        self.viewport = False

    def handle_decl(self, declaration: str) -> None:
        self.doctype |= declaration.lower() == 'doctype html'

    def handle_starttag(self, tag: str, raw_attrs: list[tuple[str, str | None]]) -> None:
        attrs = dict(raw_attrs)
        if tag == 'html':
            self.lang |= bool(attrs.get('lang'))
        if tag == 'title':
            self.title = True
        if tag == 'meta' and attrs.get('name') == 'viewport':
            self.viewport = True
        if tag == 'script':
            self.errors.append('Unexpected executable script in the static legal site')
        if tag == 'img' and not attrs.get('alt'):
            self.errors.append('Image missing descriptive alt text')
        identifier = attrs.get('id')
        if identifier:
            if identifier in self.ids:
                self.errors.append('Duplicate HTML id')
            self.ids.add(identifier)
        for key, value in attrs.items():
            if key.lower().startswith('on'):
                self.errors.append('Unexpected inline event handler')
            if key in ('href', 'src'):
                self.links.append(value or '')
        if tag not in VOID:
            self.stack.append(tag)

    def handle_endtag(self, tag: str) -> None:
        if not self.stack or self.stack[-1] != tag:
            self.errors.append('Unbalanced HTML tag: ' + tag)
        else:
            self.stack.pop()


def validate_page(path: Path, root: Path) -> list[str]:
    parser = PageParser()
    parser.feed(path.read_text(encoding='utf-8'))
    errors = list(parser.errors)
    if parser.stack:
        errors.append('Unclosed HTML tags')
    if not all((parser.doctype, parser.lang, parser.title, parser.viewport)):
        errors.append('Missing document type, language, title or viewport')
    for link in parser.links:
        url = urlsplit(link)
        if url.scheme or url.netloc:
            if url.scheme not in ('https', 'mailto') or url.username or url.password:
                errors.append('Unsafe external link scheme or embedded credentials')
            continue
        target = (path.parent / unquote(url.path)).resolve() if url.path else path.resolve()
        if not target.is_relative_to(root.resolve()):
            errors.append('Link escapes the site root')
        elif not target.is_file():
            errors.append('Missing local link or asset: ' + url.path)
        elif url.fragment and target.suffix == '.html':
            other = PageParser()
            other.feed(target.read_text(encoding='utf-8'))
            if unquote(url.fragment) not in other.ids:
                errors.append('Missing local anchor: ' + url.fragment)
    return errors


def check_publication_scope(paths: list[str]) -> list[str]:
    return ['File outside the approved legal/support publication scope: ' + path
            for path in paths if path not in PUBLIC_FILES]


def secret_findings(text: str) -> bool:
    return any(re.search(pattern, text) for pattern in SECRET_PATTERNS)


def validate_site(root: Path = ROOT) -> list[str]:
    errors = []
    for name in PAGES:
        path = root / name
        if not path.is_file():
            errors.append(name + ': missing page')
        else:
            errors.extend(name + ': ' + error for error in validate_page(path, root))
    for name in ASSETS:
        if not (root / name).is_file():
            errors.append(name + ': missing asset')
    css_path = root / 'style.css'
    if css_path.is_file():
        css = re.sub(r'/\*.*?\*/', '', css_path.read_text(), flags=re.S)
        depth = 0
        for char in css:
            if char == '{':
                depth += 1
            elif char == '}':
                depth -= 1
                if depth < 0:
                    break
        if depth != 0:
            errors.append('style.css: unbalanced braces')
    for path in root.rglob('*'):
        if not path.is_file() or any(part in ('.git', 'build', '__pycache__', '.venv', '.mypy_cache', '.ruff_cache') for part in path.relative_to(root).parts):
            continue
        if path.name == '.env' or path.name.startswith('.env.'):
            errors.append('Environment file must not be included in this site')
        if path.suffix in ('.jks', '.keystore', '.p12', '.p8'):
            errors.append('Signing material must not be included in this site')
        try:
            text = path.read_text(encoding='utf-8')
        except UnicodeDecodeError:
            continue
        if secret_findings(text):
            errors.append(str(path.relative_to(root)) + ': possible credential detected (value withheld)')
    return errors


if __name__ == '__main__':
    findings = validate_site()
    if '--tracked' in sys.argv[1:]:
        tracked = subprocess.check_output(
            ['git', 'ls-files', '-z'], cwd=ROOT, text=True).split('\0')
        findings.extend(check_publication_scope([path for path in tracked if path]))
    for finding in findings:
        print(finding)
    if findings:
        raise SystemExit(1)
    print('Public site validation passed: 6 pages, links/assets, HTML, CSS and credential safeguards.')
