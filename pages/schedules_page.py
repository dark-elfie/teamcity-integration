import logging
import allure
import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class SchedulePage:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.wait = WebDriverWait(self.driver, 15)
        self.confirm_delete_xpath = "//a[text()='Usuń']"
        self.scheduleless_xpath = "//input[@id='graphicless']/.."
        self.tonnage_xpath = "//input[@name='quantity']"
        self.pin_xpath = "//input[@name='pin']"
        self.date_from_xpath = "//input[@name='date']"
        self.date_to_xpath = "//input[@name='date_to']"
        self.planned_gt_xpath = "//span[@id='select2-grain-trader-id-container']"
        self.save_button_css = ".btn-main"

        self.open_filters_xpath = "//a[contains(@class, 'toggle-filters-btn')]"
        self.filters_gt_xpath = "//label[text()='Grain Trader']/../following-sibling::span//input"
        self.filters_receiver_xpath = "//label[text()='Nazwa skr. odb.']/../following-sibling::input"
        self.filters_address_xpath = "//label[text()='Miejsce dostawy']/../following-sibling::input"
        self.filters_ks_number_xpath = "//label[text()='Nr umowy KS']/../following-sibling::input"
        self.filters_product_xpath = "//label[text()='Towar']/following-sibling::span//input"
        self.filters_date_xpath = "//label[text()='Data grafiku']/../following-sibling::input"
        self.filters_advice_status_xpath = "//label[contains(text(), 'Status')]/../following-sibling::span//input"
        self.filters_delivery_date_xpath = "//label[text()='Data rozładunku']/../following-sibling::input"
        self.filters_planned_gt_xpath = "//label[text()='Planowany Grain Trader']/../following-sibling::input"
        self.set_filters_button_xpath = "//button[text()='Filtruj']"
        self.delete_filters_xpath = "//a[@title='Wyczyść filtry']"

    @allure.step("Usuwanie grafiku")
    def delete_schedule(self, ks_number, date, planned_gt):
        self.logger.info("Usuwanie grafiku")
        delete_xpath = "//td[text()='" + ks_number + "']/following-sibling::td[contains(text(), '" + date + "')]" \
                       "/following-sibling::td[text()='" + planned_gt + "']/following-sibling::" \
                       "td[@data-label='actions']/a[@data-title='Na pewno usunąć?']"
        self.wait.until(ec.element_to_be_clickable((By.XPATH, delete_xpath)))
        self.driver.find_element_by_xpath(delete_xpath).click()

    @allure.step("Potwierdzenie usuwania grafiku")
    def confirm_delete(self):
        self.logger.info("Potwierdzenie usuwania grafiku")
        self.wait.until(ec.element_to_be_clickable((By.XPATH, self.confirm_delete_xpath)))
        self.driver.find_element_by_xpath(self.confirm_delete_xpath).click()

    @allure.step("Sprawdzanie widocznosci grafiku")
    def check_visibility(self, ks_number, date, planned_gt):
        self.logger.info("Sprawdzanie widocznosci grafiku")
        schedule_xpath = "//td[text()='" + ks_number + "']/following-sibling::td[contains(text(), '" + date + "')]" \
                         "/following-sibling::td[text()='" + planned_gt + "']"
        try:
            self.driver.find_element_by_xpath(schedule_xpath)
            return True, ""
        except NoSuchElementException:
            return False, "Grafik nie wyświetla się na liście"

    @allure.step("Przejście do edytowania grafiku")
    def get_in_edit_schedule(self, ks_number, date, planned_gt):
        self.logger.info("Przejście do edytowania grafiku")
        edit_schedule_xpath = "//td[text()='" + ks_number + "']/following-sibling::td[contains(text(), '" + date \
                              + "')]/following-sibling::td[text()='" + planned_gt \
                              + "']/following-sibling::td[@data-label='actions']/a[@title='Edycja']"
        self.driver.find_element_by_xpath(edit_schedule_xpath).click()

    @allure.step("Edytowanie grafiku")
    def edit_schedule(self, new_date_from, new_date_to, new_gt, is_scheduleless, new_tonnage, new_pin):
        self.logger.info("Edytowanie grafiku")
        self.wait.until(ec.element_to_be_clickable((By.XPATH, self.scheduleless_xpath)))
        scheduleless = self.driver.find_element_by_xpath(self.scheduleless_xpath)
        if scheduleless.is_selected() and not is_scheduleless:
            scheduleless.click()
        elif not scheduleless.is_selected() and is_scheduleless:
            scheduleless.click()

        planned_gt = self.driver.find_element_by_xpath(self.planned_gt_xpath)
        planned_gt.click()
        planned_gt_option_xpath = "//li[text()='" + new_gt + "']"
        self.driver.find_element_by_xpath(planned_gt_option_xpath).click()

        tonnage = self.driver.find_element_by_xpath(self.tonnage_xpath)
        tonnage.click()
        tonnage.clear()
        tonnage.send_keys(new_tonnage)

        pin = self.driver.find_element_by_xpath(self.pin_xpath)
        pin.click()
        pin.clear()
        pin.send_keys(new_pin)

        date_from = self.driver.find_element_by_xpath(self.date_from_xpath)
        date_from.click()
        date_from.clear()
        date_from.send_keys(new_date_from)

        date_to = self.driver.find_element_by_xpath(self.date_to_xpath)
        date_to.click()
        date_to.clear()
        date_to.send_keys(new_date_to)

    @allure.step("Zapisanie grafiku")
    def save_schedule(self):
        self.driver.find_element(By.CSS_SELECTOR, self.save_button_css).click()

    @allure.step("Walidacja dodanego grafiku")
    def validate_schedule_list(self, ks_number, date_from, grain_trader):
        self.logger.info("Walidacja dodanego grafiku")
        assertion_xpath = "//td[text()='" + ks_number + "']/following-sibling::td[contains(text(), '" + date_from \
                          + "')]/following-sibling::td[text()='" + grain_trader + "']"

        assert self.driver.find_element_by_xpath(assertion_xpath)

    @allure.step("Otwarcie panelu filtrow")
    def open_filters_schedules(self):
        self.logger.info("Otwarcie panelu filtrow")
        self.wait.until(ec.element_to_be_clickable((By.XPATH, self.open_filters_xpath)))
        self.driver.find_element_by_xpath(self.open_filters_xpath).click()

    @allure.step("Filtry: Grain Trader")
    def filters_grain_trader(self, grain_trader):
        self.logger.info("Filtry: Grain Trader")
        self.wait.until(ec.element_to_be_clickable((By.XPATH, self.filters_gt_xpath)))
        gt = self.driver.find_element_by_xpath(self.filters_gt_xpath)
        gt.click()
        gt.send_keys(grain_trader)
        gt_option_xpath = "//li[text()='" + grain_trader + "']"
        self.driver.find_element_by_xpath(gt_option_xpath).click()

    @allure.step("Filtry: Nazwa skr. odb.")
    def filters_receiver(self, receiver):
        self.logger.info("Filtry: Nazwa skr. odb.")
        self.wait.until(ec.element_to_be_clickable((By.XPATH, self.filters_receiver_xpath)))
        rec = self.driver.find_element_by_xpath(self.filters_receiver_xpath)
        rec.click()
        rec.send_keys(receiver)

    @allure.step("Filtry: Miejsce dostawy")
    def filters_address(self, address):
        self.logger.info("Filtry: Miejsce dostawy")
        self.wait.until(ec.element_to_be_clickable((By.XPATH, self.filters_address_xpath)))
        address_input = self.driver.find_element_by_xpath(self.filters_address_xpath)
        address_input.click()
        address_input.send_keys(address)

    @allure.step("Filtry: Nr umowy KS")
    def filters_ks_number(self, ks_number):
        self.logger.info("Filtry: Nr umowy KS")
        self.wait.until(ec.element_to_be_clickable((By.XPATH, self.filters_ks_number_xpath)))
        ks = self.driver.find_element_by_xpath(self.filters_ks_number_xpath)
        ks.click()
        ks.send_keys(ks_number)

    @allure.step("Filtry: Towar")
    def filters_product(self, product):
        self.logger.info("Filtry: Towar")
        self.wait.until((ec.element_to_be_clickable((By.XPATH, self.filters_product_xpath))))
        product_input = self.driver.find_element_by_xpath(self.filters_product_xpath)
        product_input.click()
        product_input.send_keys(product[:5])
        product_option_xpath = "//li[text()='" + product + "']"
        self.driver.find_element_by_xpath(product_option_xpath).click()

    @allure.step("Filtry: Data grafiku")
    def filters_schedule_date(self, schedule_date):
        self.logger.info("Filtry: Data grafiku")
        self.wait.until(ec.element_to_be_clickable((By.XPATH, self.filters_date_xpath)))
        date = self.driver.find_element_by_xpath(self.filters_date_xpath)
        date.click()
        date.send_keys(schedule_date)

    @allure.step("Filtry: Status awizacji")
    def filters_advice_status(self, advice_status):
        self.logger.info("Filtry: Status awizacji")
        self.wait.until(ec.element_to_be_clickable((By.XPATH, self.filters_advice_status_xpath)))
        status = self.driver.find_element_by_xpath(self.filters_advice_status_xpath)
        status.click()
        status.send_keys(advice_status)
        status_option_xpath = "//li[text()='" + advice_status + "']"
        self.driver.find_element_by_xpath(status_option_xpath).click()

    @allure.step("Filtry: Data rozladunku")
    def filters_delivery_date(self, delivery_date):
        self.logger.info("Filtry: Data rozladunku")
        self.wait.until(ec.element_to_be_clickable((By.XPATH, self.filters_delivery_date_xpath)))
        date = self.driver.find_element_by_xpath(self.filters_delivery_date_xpath)
        date.click()
        date.send_keys(delivery_date)

    @allure.step("Filtry: Planowany Grain Trader")
    def filters_planned_grain_trader(self, grain_trader):
        self.logger.info("Filtry: Planowany Grain Trader")
        self.wait.until(ec.element_to_be_clickable((By.XPATH, self.filters_planned_gt_xpath)))
        planned_gt = self.driver.find_element_by_xpath(self.filters_planned_gt_xpath)
        planned_gt.click()
        planned_gt.send_keys(grain_trader)

    @allure.step("Zastosowanie filtrow")
    def use_filters(self):
        self.logger.info("Zastosowanie filtrow")
        self.driver.find_element_by_xpath(self.set_filters_button_xpath).click()

    @allure.step("Usuwanie filtrow")
    def delete_filters(self):
        self.logger.info("Usuwanie filtrow")
        self.wait.until(ec.element_to_be_clickable((By.XPATH, self.delete_filters_xpath)))
        self.driver.find_element_by_xpath(self.delete_filters_xpath).click()
