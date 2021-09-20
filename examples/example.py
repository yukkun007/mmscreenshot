from moz_screenshot import screenshot, get_text


def test_screenshot():
    screenshot(
        "https://weather.yahoo.co.jp/weather/jp/13/4410.html",
        "//div[@class='forecastCity']/table/tbody/tr/td/div",
        "./screenshot.png",
    )


def test_get_text():
    text = get_text(
        "https://weather.yahoo.co.jp/weather/jp/13/4410.html",
        "//div[@class='forecastCity']/table/tbody/tr/td/div/table/tbody/tr[2]/td[3]",
    )
    print(text)


def main() -> None:
    test_screenshot()
    test_get_text()


if __name__ == "__main__":
    main()
