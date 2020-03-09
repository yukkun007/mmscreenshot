import os
import logging
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class ChromeDriver:
    def __init__(self) -> None:
        logging.debug("driver.create/start")

        options = ChromeOptions()
        binary_location = os.environ.get("CHROME_BINARY_LOCATION", None)
        if not (binary_location is None):
            options.binary_location = binary_location
        # 必須
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-gpu")
        options.add_argument("--single-process")
        # options.add_argument("--disable-setuid-sandbox")
        # options.add_argument("--disable-dev-shm-usage")
        # エラーの許容
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--allow-running-insecure-content")
        options.add_argument("--disable-web-security")
        # headlessでは不要そうな機能
        options.add_argument("--disable-desktop-notifications")
        options.add_argument("--disable-extensions")
        # UA
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36"  # noqa
        options.add_argument("--user-agent=" + user_agent)
        # 言語
        options.add_argument("--lang=ja")
        # 画像を読み込まないで軽くする(→コメントアウト)
        # options.add_argument("--blink-settings=imagesEnabled=false")

        # chromedriver生成
        executable_path = os.environ.get("CHROME_DRIVER_LOCATION", None)
        self._driver = Chrome(options=options, executable_path=executable_path)
        # ウィンドウサイズ指定しないとスクロールバーが出る
        self._driver.set_window_size(1280, 720)

        logging.debug("driver.create/end")

    def screenshot(self, url: str, xpath: str, out_file: str = "./screenshot.png"):
        self._driver.get(url)
        png = self._driver.find_element_by_xpath(xpath).screenshot_as_png
        with open(out_file, "wb") as f:
            f.write(png)
        self._driver.close()

    def get_text(self, url: str, xpath: str, out_file: str = "./screenshot.png"):
        self._driver.get(url)
        text = self._driver.find_element_by_xpath(xpath).text
        self._driver.close()
        return text

    def _wait(self) -> None:
        WebDriverWait(self._driver, 10, poll_frequency=0.05).until(
            ec.presence_of_all_elements_located
        )

    def _wait_element(self, target):
        element = WebDriverWait(self._driver, 10, poll_frequency=0.05).until(
            ec.presence_of_element_located(target)
        )

        return element

    def __del__(self):
        logging.debug("driver.quit/start")
        self._driver.quit()
        logging.debug("driver.quit/end")
