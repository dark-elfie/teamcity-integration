import logging
import allure
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class ContractsPage:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.wait = WebDriverWait(self.driver, 15)
        self.sales_contract_xpath = "//span[@aria-labelledby='select2-sales-contract-id-container']"
        self.sales_contract_input_xpath = "//span/input[@class='select2-search__field']"
        self.purchase_contract_xpath = "//select[@id='purchase-contract-id']/../span"
        self.purchase_contract_input_xpath = "//li/input[@class='select2-search__field']"
        self.connect_button_xpath = "//button[@id='connect-contractors']"
        self.connected_kz_xpath = "//h3[contains(text(), 'Powiązane kontrakty zakupu')]"
        self.connected_ks_xpath = "//h3[contains(text(), 'Powiązane kontrakty sprzedaży')]"
        self.contracts_list_xpath = "//td[1]/a"
        self.schedules_xpath = "//div[@class='row'][3]//h3[contains(text(), 'Grafiki')]"
        self.add_new_schedule_xpath = "//div[@class='row'][3]//a[text()='Dodaj nowy']"
        self.add_many_schedules_xpath = "//div[@class='row'][3]//a[text()='Dodaj wiele']"

        self.schedule_dialog_xpath = "//div[@id='append-schedules']"
        self.schedule_dialog_multi_xpath = "//div[@id='append-schedules-multi']"
        self.add_row_xpath = "//button[contains(@class, 'add-row')]"
        self.delete_row_xpath = "//button[contains(@class, 'del-row')]"
        self.non_schedule_button_xpath = "//div[@id='graphicless']"
        self.schedule_date_from_xpath = "//input[@name='date']"
        self.schedule_date_to_xpath = "//input[@name='date_to']"
        self.schedule_grain_trader_xpath = "//span[@aria-labelledby='select2-grain-trader-id-container']"
        self.schedule_save_xpath = "//div[@class='modal-dialog']//button[text()='Zapisz']"
        self.schedule_list_date_xpath = "//tbody/tr/td[@data-label='Data']"
        self.schedule_list_gt_xpath = "//tbody/tr/td[@data-label='Planowany Grain Trader']"
        self.confirm_delete_xpath = "//a[text()='Usuń']"

        self.many_non_schedule_button_xpath = "//input[contains(@name, 'graphicless')][@type='checkbox']/.."
        self.many_schedule_save_xpath = "//div[@class='modal-body']//button[text()='Zapisz']"
        self.many_schedule_list_date_xpath = "//tbody/tr/td[@data-label='Data']"
        self.many_schedule_list_gt_xpath = "//tbody/tr/td[@data-label='Planowany Grain Trader']"

    @allure.step("Wybor kontraktu sprzedazy (po numerze awizacji)")
    def set_sales_contract(self, sales_number):
        self.logger.info("Wybor kontraktu sprzedazy (po numerze awizacji)")
        self.wait.until(ec.element_to_be_clickable((By.XPATH, self.sales_contract_xpath)))
        time.sleep(1)
        self.driver.find_element_by_xpath(self.sales_contract_xpath).click()
        self.wait.until(ec.element_to_be_clickable((By.XPATH, self.sales_contract_input_xpath)))
        sales_input = self.driver.find_element_by_xpath(self.sales_contract_input_xpath)
        sales_input.click()
        sales_input.send_keys(sales_number)
        sales_option_xpath = "//li/p/span[contains(text(), '" + sales_number + "')]/.."
        self.wait.until(ec.element_to_be_clickable((By.XPATH, sales_option_xpath)))
        self.driver.find_element_by_xpath(sales_option_xpath).click()

    @allure.step("Wybor kontraktu zakupu (po numerze awizacji)")
    def set_purchase_contract(self, purchase_number):
        self.logger.info("Wybor kontraktu zakupu (po numerze awizacji)")
        self.wait.until(ec.element_to_be_clickable((By.XPATH, self.purchase_contract_xpath)))
        self.driver.find_element_by_xpath(self.purchase_contract_xpath).click()
        self.wait.until(ec.element_to_be_clickable((By.XPATH, self.purchase_contract_input_xpath)))
        purchase_input = self.driver.find_element_by_xpath(self.purchase_contract_input_xpath)
        purchase_input.click()
        purchase_input.send_keys(purchase_number)
        purchase_option_xpath = "//li/p/span[contains(text(), '" + purchase_number + "')]/.."
        self.wait.until(ec.element_to_be_clickable((By.XPATH, purchase_option_xpath)))
        self.driver.find_element_by_xpath(purchase_option_xpath).click()

    @allure.step("Laczenie kontraktow")
    def connect_contracts(self):
        self.logger.info("Laczenie kontraktow")
        self.driver.find_element_by_xpath(self.connect_button_xpath).click()
        self.wait.until(ec.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Pomyślnie połączono')]")))

    @allure.step("Rozlaczenie kontraktow")
    def disconnect_contracts(self, purchase_number):
        self.logger.info("Rozlaczenie kontraktow")
        disconnect_button = "//a[contains(text(), '" + purchase_number + "')]/../../../..//a[@title='Usuń połączenie']"
        self.driver.find_element_by_xpath(disconnect_button).click()
        self.wait.until(ec.element_to_be_clickable((By.XPATH, "//div[text()='Pomyślnie usunięto']")))

    @allure.step("Utworzenie awizacji do polaczonych kontraktow")
    def create_advice(self, purchase_number):
        self.logger.info("Utworzenie awizacji do polaczonych kontraktow")
        create_advice_button = "//a[contains(text(), '" + purchase_number +\
                               "')]/../../../..//a[@title='Dodaj awizację']"
        self.driver.find_element_by_xpath(create_advice_button).click()

    @allure.step("Sprawdzenie widoczności polaczenia w KS")
    def visibility_in_sales(self, purchase_number):
        self.logger.info("Sprawdzenie widoczności polaczenia w KS")
        self.wait.until(lambda l: len(self.driver.find_elements_by_xpath("//a[text()='Dodaj nowy']")) == 3)
        self.driver.find_element_by_xpath(self.connected_kz_xpath).click()
        self.wait.until(lambda l: len(self.driver.find_elements_by_xpath("//a[@title='Podgląd']")) >= 1)
        kz_list = self.driver.find_elements_by_xpath(self.contracts_list_xpath)
        if len(purchase_number) == 4:
            purchase = "KZ/00" + purchase_number
        else:
            purchase = purchase_number
        for kz in kz_list:
            if purchase in kz.text:
                return True

        return False

    @allure.step("Sprawdzenie widoczności polaczenia w KZ")
    def visibility_in_purchase(self, sales_number):
        self.logger.info("Sprawdzenie widoczności polaczenia w KZ")
        self.wait.until(lambda l: len(self.driver.find_elements_by_xpath("//a[text()='Dodaj nowy']")) == 2)
        self.driver.find_element_by_xpath(self.connected_ks_xpath).click()
        self.wait.until(lambda l: len(self.driver.find_elements_by_xpath("//a[@title='Podgląd']")) >= 1)
        ks_list = self.driver.find_elements_by_xpath(self.contracts_list_xpath)
        if len(sales_number) == 4:
            sales = "KS/00" + sales_number
        else:
            sales = sales_number
        for ks in ks_list:
            if sales in ks.text:
                return True

        return False

    @allure.step("Wejscie w szczegoly kontraktu")
    def get_into_sales_contract(self, contract_number):
        self.logger.info("Wejscie w szczegoly kontraktu")
        contract_xpath = "//a[text()='" + contract_number + "']"
        self.wait.until(ec.element_to_be_clickable((By.XPATH, contract_xpath)))
        self.driver.find_element_by_xpath(contract_xpath).click()

    @allure.step("Otwarcie zakladki 'Grafiki'")
    def open_schedules(self):
        self.logger.info("Otwarcie zakladki 'Grafiki'")
        self.wait.until(lambda l: len(self.driver.find_elements_by_xpath("//a[text()='Dodaj nowy']")) == 3)
        self.driver.find_element_by_xpath(self.schedules_xpath).click()

    @allure.step("Dodaj nowy grafik")
    def add_new_schedule(self, is_scheduleless, date_from, date_to, grain_trader):
        self.logger.info("Dodaj nowy grafik")
        time.sleep(2)
        self.driver.find_element_by_xpath(self.add_new_schedule_xpath).click()
        self.wait.until(ec.visibility_of_element_located((By.XPATH, self.schedule_dialog_xpath)))

        if is_scheduleless:
            self.driver.find_element_by_xpath(self.non_schedule_button_xpath).click()

        date_from_input = self.driver.find_element_by_xpath(self.schedule_date_from_xpath)
        date_from_input.send_keys(date_from)

        date_to_input = self.driver.find_element_by_xpath(self.schedule_date_to_xpath)
        date_to_input.send_keys(date_to)

        self.driver.find_element_by_xpath(self.schedule_grain_trader_xpath).click()
        gt_option_xpath = "//li[text()='" + grain_trader + "']"
        self.driver.find_element_by_xpath(gt_option_xpath).click()

        self.driver.find_element_by_xpath(self.schedule_save_xpath).click()

    @allure.step("Dodaj nowe grafiki")
    def add_many_schedules(self, is_scheduleless, date_from, date_to, grain_trader, schedule_number):
        self.logger.info("Dodaj nowe grafiki")
        time.sleep(2)
        self.driver.find_element_by_xpath(self.add_many_schedules_xpath).click()
        self.wait.until(ec.visibility_of_element_located((By.XPATH, self.schedule_dialog_multi_xpath)))

        non_schedule_list = self.driver.find_elements_by_xpath(self.many_non_schedule_button_xpath)

        while (len(non_schedule_list) - 1) < schedule_number:
            self.driver.find_element_by_xpath(self.add_row_xpath).click()
            non_schedule_list = self.driver.find_elements_by_xpath(self.many_non_schedule_button_xpath)
            time.sleep(0.5)

        while (len(non_schedule_list) - 1) > schedule_number:
            self.driver.find_element_by_xpath(self.delete_row_xpath).click()
            non_schedule_list = self.driver.find_elements_by_xpath(self.many_non_schedule_button_xpath)
            time.sleep(0.5)

        for i in range(schedule_number):
            many_schedule_grain_trader_xpath = "//span[@aria-labelledby='select2-planned-grain-trader-id-" \
                                                + str(i) + "-container']"
            many_schedule_date_from_xpath = "//input[@name='" + str(i) + "[date]']"
            many_schedule_date_to_xpath = "//input[@name='" + str(i) + "[date_to]']"

            self.driver.find_element_by_xpath(many_schedule_date_from_xpath).send_keys(date_from[i])

            self.driver.find_element_by_xpath(many_schedule_date_to_xpath).send_keys(date_to[i])

            if is_scheduleless[i]:
                non_schedule_list[i].click()
            else:
                self.driver.find_element_by_xpath(many_schedule_grain_trader_xpath).click()
                gt_option_xpath = "//li[text()='" + grain_trader[i] + "']"
                self.driver.find_element_by_xpath(gt_option_xpath).click()
            time.sleep(0.5)

        self.driver.find_element_by_xpath(self.many_schedule_save_xpath).click()

    @allure.step("Walidacja dodanego grafiku")
    def validate_schedule(self, date_from, date_to, grain_trader):
        self.logger.info("Walidacja dodanego grafiku")
        v_date = date_from + " - " + date_to
        assert v_date == self.driver.find_element_by_xpath(self.schedule_list_date_xpath).text

        assert grain_trader == self.driver.find_element_by_xpath(self.schedule_list_gt_xpath).text

    @allure.step("Walidacja dodanych grafikow")
    def validate_many_schedules(self, is_scheduleless, date_from, date_to, grain_trader, schedule_number):
        self.logger.info("Walidacja dodanych grafikow")

        for i in range(schedule_number):
            v_date = date_from[i] + " - " + date_to[i]
            assertion_xpath = "//td[text()='" + v_date + "']/following-sibling::td" \
                              "[@data-label='Planowany Grain Trader'][text()='" + grain_trader[i] + "']"

            assert self.driver.find_element_by_xpath(assertion_xpath)

    @allure.step("Otwarcie szczegolow grafiku")
    def get_in_schedule(self, date_from, date_to, grain_trader):
        self.logger.info("Otwarcie szczegolow grafiku")
        v_date = date_from + " - " + date_to
        schedule_xpath = "//tbody/tr/td[text()='" + v_date + "']/following-sibling::td[text()='" + grain_trader \
                         + "']/following-sibling::td[@data-label='actions']/a[@title='Edycja']"
        self.driver.find_element_by_xpath(schedule_xpath).click()

    @allure.step("Edycja grafiku")
    def edit_schedule(self, date_from, date_to, grain_trader):
        self.logger.info("Edycja grafiku")
        self.wait.until(ec.visibility_of_element_located((By.XPATH, self.schedule_dialog_xpath)))

        date_from_input = self.driver.find_element_by_xpath(self.schedule_date_from_xpath)
        date_from_input.clear()
        date_from_input.send_keys(date_from)

        date_to_input = self.driver.find_element_by_xpath(self.schedule_date_to_xpath)
        date_to_input.clear()
        date_to_input.send_keys(date_to)

        self.driver.find_element_by_xpath(self.schedule_grain_trader_xpath).click()
        gt_option_xpath = "//li[text()='" + grain_trader + "']"
        self.driver.find_element_by_xpath(gt_option_xpath).click()

        self.driver.find_element_by_xpath(self.schedule_save_xpath).click()

    @allure.step("Usuwanie grafiku z poziomu KS")
    def delete_schedule_KS(self, date_from, date_to, grain_trader):
        self.logger.info("Usuwanie grafiku z poziomu KS")
        v_date = date_from + " - " + date_to
        delete_xpath = "//tbody/tr/td[text()='" + v_date + "']/following-sibling::td[text()='" + grain_trader \
                       + "']/following-sibling::td[@data-label='actions']/a[@data-title='Na pewno usunąć?']"
        self.driver.find_element_by_xpath(delete_xpath).click()

    @allure.step("Potwierdzenie usuniecia grafiku")
    def confirm_delete_schedule(self):
        self.logger.info("Potwierdzenie usuniecia grafiku")
        self.wait.until(ec.element_to_be_clickable((By.XPATH, self.confirm_delete_xpath)))
        self.driver.find_element_by_xpath(self.confirm_delete_xpath).click()
