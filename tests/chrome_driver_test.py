import pytest
from mmscreenshot.chrome_driver import ChromeDriver


class TestChromeDriver:
    @pytest.fixture()
    def chrome_driver_1(self) -> ChromeDriver:
        return ChromeDriver()

    @pytest.mark.slow
    def test_screenshot(self, chrome_driver_1: ChromeDriver):
        chrome_driver_1.screenshot(
            "https://weather.yahoo.co.jp/weather/jp/13/4410.html",
            "//div[@class='forecastCity']/table/tbody/tr/td/div",
        )

    def test_get_text(self, chrome_driver_1: ChromeDriver):
        test = chrome_driver_1.get_text(
            "https://weather.yahoo.co.jp/weather/jp/13/4410.html",
            "//div[@class='forecastCity']/table/tbody/tr/td/div/table/tbody/tr[2]/td[3]",
        )
        percent = int(test.replace("％", ""))
        if percent > 10:
            print("今日は雨が降りそうです。\n  12-18時の降水確率: {}％".format(percent))
