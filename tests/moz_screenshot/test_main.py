from moz_screenshot import screenshot, get_text


class TestCore:
    def test_screenshot(self):
        screenshot(
            "https://weather.yahoo.co.jp/weather/jp/13/4410.html",
            "//div[@class='forecastCity']/table/tbody/tr/td/div",
            "./screenshot.png",
        )

    def test_get_text(self):
        text = get_text(
            "https://weather.yahoo.co.jp/weather/jp/13/4410.html",
            "//div[@class='forecastCity']/table/tbody/tr/td/div/table/tbody/tr[2]/td[3]",
        )
        print(text)
