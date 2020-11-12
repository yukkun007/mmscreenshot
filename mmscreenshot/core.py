from mmscreenshot.env import load_env
from mmscreenshot.chrome_driver import ChromeDriver


def _init(dotenv_path: str) -> None:
    if load_env(dotenv_path) is False:
        print("Failed to load dotenv file.")


def screenshot(url: str, xpath: str, out_file: str, dotenv_path: str = ".env"):
    _init(dotenv_path)
    driver = ChromeDriver()
    driver.screenshot(url, xpath, out_file=out_file)


def get_text(url: str, xpath: str, dotenv_path: str = ".env"):
    _init(dotenv_path)
    driver = ChromeDriver()
    return driver.get_text(url, xpath)
