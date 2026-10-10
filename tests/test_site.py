from pathlib import Path
import shutil
import tempfile
import unittest

from scripts.validate import PAGES, ASSETS, secret_findings, validate_site
from scripts.build import build

ROOT = Path(__file__).resolve().parents[1]


class PublicSiteTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        for name in PAGES + ASSETS:
            target = self.root / name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / name, target)

    def alter(self, old: str, new: str) -> None:
        page = self.root / 'index.html'
        page.write_text(page.read_text().replace(old, new))

    def test_current_site_has_valid_links_and_structure(self) -> None:
        self.assertEqual(validate_site(self.root), [])

    def test_missing_local_page_is_rejected(self) -> None:
        (self.root / 'support.html').unlink()
        self.assertTrue(validate_site(self.root))

    def test_invalid_nesting_is_rejected(self) -> None:
        self.alter('</main>', '</section></main>')
        self.assertTrue(validate_site(self.root))

    def test_unsafe_url_is_rejected(self) -> None:
        self.alter('href="privacy.html"', 'href="javascript:alert(1)"')
        self.assertTrue(validate_site(self.root))

    def test_path_traversal_is_rejected(self) -> None:
        self.alter('href="privacy.html"', 'href="../private.html"')
        self.assertTrue(validate_site(self.root))

    def test_missing_anchor_is_rejected(self) -> None:
        self.alter('href="privacy.html"', 'href="privacy.html#missing"')
        self.assertTrue(validate_site(self.root))

    def test_inline_handler_is_rejected(self) -> None:
        self.alter('<body>', '<body onclick="alert(1)">')
        self.assertTrue(validate_site(self.root))

    def test_css_imbalance_is_rejected(self) -> None:
        (self.root / 'style.css').write_text('body { color: green;')
        self.assertTrue(validate_site(self.root))

    def test_environment_file_is_rejected(self) -> None:
        (self.root / '.env').write_text('EXAMPLE=placeholder\n')
        self.assertTrue(validate_site(self.root))

    def test_local_tool_cache_is_not_scanned_as_site_content(self) -> None:
        cache = self.root / '.venv'
        cache.mkdir()
        (cache / 'third_party_fixture.txt').write_text('ghp_' + 'x' * 36)
        self.assertEqual(validate_site(self.root), [])

    def test_secret_detector_without_real_secret_fixtures(self) -> None:
        self.assertTrue(secret_findings('ghp_' + 'x' * 36))
        self.assertTrue(secret_findings('-----BEGIN ' + 'PRIVATE KEY-----'))
        self.assertFalse(secret_findings('thecarpgalilee@gmail.com'))

    def test_build_exports_only_public_pages_and_assets(self) -> None:
        (self.root / 'internal.txt').write_text('not exported')
        output = build(self.root)
        self.assertEqual({str(p.relative_to(output)) for p in output.rglob('*') if p.is_file()}, set(PAGES + ASSETS))
        self.assertEqual(validate_site(output), [])
        build(self.root)
        self.assertFalse((output / 'internal.txt').exists())

    def test_privacy_and_deletion_preserve_current_disclosures(self) -> None:
        privacy = (self.root / 'privacy.html').read_text()
        self.assertIn('reduced copy of the photo to OpenAI', privacy)
        self.assertIn('Group shopping lists', privacy)
        self.assertIn('no automatic expiry', privacy)
        self.assertNotIn('run locally in the app', privacy)
        self.assertIn('Delete selected data without deleting your account', (self.root / 'account-deletion.html').read_text())


if __name__ == '__main__':
    unittest.main()
