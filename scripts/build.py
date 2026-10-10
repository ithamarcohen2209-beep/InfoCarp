"""Build only allowlisted public pages/assets, never application or secret files."""
from pathlib import Path
import shutil
from scripts.validate import ROOT, PAGES, ASSETS, validate_site


def build(root: Path = ROOT) -> Path:
    errors = validate_site(root)
    if errors:
        raise ValueError('\n'.join(errors))
    output = root / 'build'
    if output.is_symlink():
        raise ValueError('Build output must not be a symlink')
    if output.exists():
        shutil.rmtree(output)
    output.mkdir()
    for name in PAGES + ASSETS:
        target = output / name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(root / name, target)
    return output


if __name__ == '__main__':
    print('Built standalone public site:', build())
