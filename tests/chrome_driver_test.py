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
