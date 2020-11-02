import setenv
from mmscreenshot.chrome_driver import ChromeDriver


def _init() -> None:
    if setenv.load("./.env") is False:
        return


def screenshot(url: str, xpath: str, out_file: str):
    _init()
    driver = ChromeDriver()
    driver.screenshot(url, xpath, out_file=out_file)


def get_text(url: str, xpath: str, out_file: str):
    _init()
    driver = ChromeDriver()
    return driver.get_text(url, xpath, out_file=out_file)
