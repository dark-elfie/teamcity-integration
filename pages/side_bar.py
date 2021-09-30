import logging
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class SideBar:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.wait = WebDriverWait(self.driver, 10)
        self.side_bar_xpath = "//a[contains(@class, 'navbar-burger')]"
        self.dashboard_xpath = "//li[@class='active']//span[text()='Kokpit']"
        self.planner_xpath = "//li[@class='active']//span[text()='Planer']"
        self.advices_xpath = "//li[@class='active']//span[text()='Awizacje']"
        self.sales_contracts_xpath = "//li[@class='active']//span[text()='Kontrakty sprzedaży']"
        self.purchase_contracts_xpath = "//li[@class='active']//span[text()='Kontrakty zakupu']"
        self.connect_contracts_xpath = "//li[@class='active']//span[text()='Łączenie kontraktów']"
        self.schedules_xpath = "//li[@class='active']//span[text()='Grafiki']"
        self.payoffs_templates_xpath = "//li[@class='active']//span[text()='Szablony']"
        self.payoffs_import_xpath = "//li[@class='active']//span[text()='Import']"
        self.payoffs_import_list_xpath = "//li//span[text()='Lista importów']"

    @allure.step("Otworz/zamknij menu boczne")
    def open_side_bar(self):
        self.logger.info("Otworz/zamknij menu boczne")
        self.wait.until(ec.element_to_be_clickable((By.XPATH, self.side_bar_xpath)))
        self.driver.find_element_by_xpath(self.side_bar_xpath).click()

    @allure.step("Przejdz do 'Awizacje'")
    def get_in_advices(self):
        self.logger.info("Przejdz do 'Awizacje'")
        self.wait.until(ec.element_to_be_clickable((By.XPATH, self.advices_xpath)))
        self.driver.find_element_by_xpath(self.advices_xpath).click()

    @allure.step("Przejdz do 'Kokpit'")
    def get_in_dashboard(self):
        self.logger.info("Przejdz do 'Kokpit'")
        self.wait.until(ec.element_to_be_clickable((By.XPATH, self.dashboard_xpath)))
        self.driver.find_element_by_xpath(self.dashboard_xpath).click()

    @allure.step("Przejdz do 'Planner'")
    def get_in_planner(self):
        self.logger.info("Przejdz do 'Planner'")
        self.wait.until(ec.element_to_be_clickable((By.XPATH, self.planner_xpath)))
        self.driver.find_element_by_xpath(self.planner_xpath).click()

    @allure.step("Przejdz do 'Kontrakty sprzedazy'")
    def get_in_sales_contracts(self):
        self.logger.info("Przejdz do 'Kontrakty sprzedazy'")
        self.wait.until(ec.element_to_be_clickable((By.XPATH, self.sales_contracts_xpath)))
        self.driver.find_element_by_xpath(self.sales_contracts_xpath).click()

    @allure.step("Przejdz do 'Kontrakty zakupu'")
    def get_in_purchase_contracts(self):
        self.logger.info("Przejdz do 'Kontrakty zakupu'")
        self.wait.until(ec.element_to_be_clickable((By.XPATH, self.purchase_contracts_xpath)))
        self.driver.find_element_by_xpath(self.purchase_contracts_xpath).click()

    @allure.step("Przejdz do 'Laczenie kontraktow'")
    def get_in_contracts(self):
        self.logger.info("Przejdz do 'Laczenie kontraktow'")
        self.wait.until(ec.element_to_be_clickable((By.XPATH, self.connect_contracts_xpath)))
        self.driver.find_element_by_xpath(self.connect_contracts_xpath).click()

    @allure.step("Przejdz do 'Grafiki'")
    def get_in_schedules(self):
        self.logger.info("Przejdz do 'Grafiki'")
        self.wait.until(ec.element_to_be_clickable((By.XPATH, self.schedules_xpath)))
        self.driver.find_element_by_xpath(self.schedules_xpath).click()

    @allure.step("Przejdz do 'Szablony'")
    def get_in_payoffs_templates(self):
        self.logger.info("Przejdz do 'Szablony'")
        self.wait.until(ec.element_to_be_clickable((By.XPATH, self.payoffs_templates_xpath)))
        self.driver.find_element_by_xpath(self.payoffs_templates_xpath).click()

    @allure.step("Przejdz do 'Import'")
    def get_in_payoffs_import(self):
        self.logger.info("Przejdz do 'Import'")
        self.wait.until(ec.element_to_be_clickable((By.XPATH, self.payoffs_import_xpath)))
        self.driver.find_element_by_xpath(self.payoffs_import_xpath).click()

    @allure.step("Przejdz do 'Lista importow'")
    def get_in_payoffs_import_list(self):
        self.logger.info("Przejdz do 'Lista importow'")
        self.wait.until(ec.element_to_be_clickable((By.XPATH, self.payoffs_import_list_xpath)))
        self.driver.find_element_by_xpath(self.payoffs_import_list_xpath).click()
