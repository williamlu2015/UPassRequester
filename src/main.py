from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from src.request_upass import request_upass


def main():
    """
    The entry point of the script.
    Opens a new headless instance of Chrome, requests the U-Pass, and quits the
    headless instance of Chrome.
    :return: None
    """
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(
        executable_path="../lib/chromedriver",
        options=chrome_options
    )
    request_upass(driver)

    driver.quit()


if __name__ == "__main__":
    main()
