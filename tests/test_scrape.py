from pathlib import Path

from webScrapeBBCSkel.weather import Weather

ROOT = Path(__file__).parent.parent


class TestCardiff:
    path = str(ROOT / "tests/testWeb/Cardiff.html")
    weather = Weather(path, file_path=True)

    def test_maxCardiff(self):
        assert self.weather.getMaxT() == 12

    def test_minCardiff(self):
        assert self.weather.getMinT() == 8

    def test_locCardiff(self):
        assert self.weather.getLoc() == "Cardiff"


class TestHendred:
    path = str(ROOT / "tests/testWeb/Hendred.html")
    weather = Weather(path, file_path=True)

    def test_maxHendred(self):
        assert self.weather.getMaxT() == 11

    def test_minHendred(self):
        assert self.weather.getMinT() == 7

    def test_locHendred(self):
        assert self.weather.getLoc() == "Hendred"
