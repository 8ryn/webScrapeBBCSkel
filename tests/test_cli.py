import subprocess
import sys

from webScrapeBBCSkel import __version__


def test_cli_version():
    cmd = [sys.executable, "-m", "webScrapeBBCSkel", "--version"]
    assert subprocess.check_output(cmd).decode().strip() == __version__
