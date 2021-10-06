from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class DriverFactory:

    @staticmethod
    def get_driver(browser):
        if browser == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("--start-maximized")
            return webdriver.Chrome(ChromeDriverManager().install(), options=options)
        elif browser == "firefox":
            options = webdriver.FirefoxOptions()
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
            driver.maximize_window()
            return driver
        elif browser == "travis":
            options = webdriver.ChromeOptions()
            options.add_argument('--no-sandbox')
            options.add_argument('--headless')
            options.add_argument('--disable-dev-shm-usage')
            return webdriver.Chrome(ChromeDriverManager().install(), options=options)
        """elif browser == "remote":
            options = webdriver.ChromeOptions()
            # options.add_argument("start-maximized")
            options.set_capability("browserName", "chrome")
            return webdriver.Remote("http://10.10.15.121:4444/wd/hub", options=options)"""
        return Exception("Provide valid driver name")
