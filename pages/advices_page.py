import logging
import allure
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class AdvicePage:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.wait = WebDriverWait(self.driver, 15)
        self.short_wait = WebDriverWait(self.driver, 5)
        self.search_input_xpath = "//input[@id='fullsearch-delegate']"
        self.filters_xpath = "//a[contains(@class, 'toggle-filters-btn')]"
        self.add_new_xpath = "//a[text()='Dodaj nowy']"
        self.export_xlsx_xpath = "//a[text()='Eksport']"
        self.export_csv_xpath = "//a[text()='Eksport do CSV']"
        self.edit_first_xpath = "//*[@id='w0']/div[2]/div/table/tbody/tr[1]/td[15]/a[2]"
        self.confirm_delete_xpath = "//a[text()='Usuń']"
        self.first_aw_xpath = "//*[@id='w0']/div[2]/div/table/tbody/tr[1]/td[2]/a"

        self.edit_opened_aw_xpath = "//a[text()='Edytuj awizację']"

        self.receiver_xpath = "//span[@id='select2-sales-contract-id-container']//.."
        self.receiver_input_xpath = "/html/body/span/span/span[1]/input"
        self.receiver_input_option_xpath = "//*[@id='select2-sales-contract-id-results']/li[2]"
        self.receiver_contact_xpath = "//div[@class='step-1-additionals-sales']//ul"
        self.receiver_contact_option_xpath = "//span[@class='select2-results']//li[1]"
        self.receiver_address_xpath = "//*[@id='step1']/div/div[2]/div[3]/div/div/span/span[1]/span"
        self.receiver_address_option_xpath = "//span[@class='select2-results']//li[1]"

        self.deliverer_xpath = "//span[@id='select2-purchase-contract-id-container']//.."
        self.deliverer_input_xpath = "/html/body/span/span/span[1]/input"
        self.deliverer_input_option_xpath = "//*[@id='select2-purchase-contract-id-results']/li[2]"
        self.deliverer_contact_xpath = "//*[@id='step1']/div/div[3]/div[2]/div/div/span/span[1]/span"
        self.deliverer_contact_option_xpath = "//*[@id='select2-advice-suppliers-emails-results']/li[1]"
        self.deliverer_address_xpath = "//*[@id='step1']/div/div[3]/div[3]/div/div/span/span[1]/span"
        self.deliverer_address_option_xpath = "//*[@id='select2-supplier-address-id-results']/li[1]"
        self.go_to_carriage_button = "//*[@id='add-advice-form']/div[2]/div[2]/div[1]/button[2]"

        self.carrier_xpath = "//*[@id='step2']/div[1]/div[2]/div[1]/div/span/span[1]/span"
        self.carrier_option_xpath = "//*[@id='select2-carrier-id-results']/li[2]"
        self.carrier_contact_xpath = "//*[@id='step2']/div[1]/div[4]/div/div/div/span/span[1]/span"
        self.carrier_contact_option_xpath = "//*[@id='select2-carrier-email-id-results']/li[2]"

        self.loading_date_xpath = "//*[@id='loading-date']"
        self.loading_time_from_xpath = "//*[@id='loading-time-from']"
        self.loading_time_to_xpath = "//*[@id='loading-time-to']"
        self.delivery_date_xpath = "//*[@id='delivery-date']"
        self.delivery_time_from_xpath = "//*[@id='time-from']"
        self.delivery_time_to_xpath = "//*[@id='time-to']"
        self.schedule_xpath = "//span[@aria-labelledby='select2-schedule-id-container']"
        self.vehicle_number_xpath = "//*[@id='vehicle-identification-number']"
        self.driver_name_xpath = "//*[@id='driver-first-name']"
        self.driver_last_name_xpath = "//*[@id='driver-last-name']"
        self.id_type_xpath = "//*[@id='step2']/div[2]/div[15]/div/span/span[1]/span"
        self.id_number_xpath = "//*[@id='identification-number']"
        self.driver_phone_xpath = "//*[@id='driver-phone']"
        self.price_per_ton_xpath = "//*[@id='transport-rate']"
        self.go_to_summary_button = "//*[@id='add-advice-form']/div[2]/div[2]/div[1]/button[2]"
        self.save_button = "//*[@id='add-advice-form']/div[2]/div[2]/div[1]/button[3]"

        self.summary_receiver_xpath = "//*[@id='step3']/div/div[1]/p/strong"
        self.summary_deliverer_xpath = "//*[@id='step3']/div/div[2]/p/strong"
        self.summary_carrier_xpath = "//*[@id='step3']/div/div[4]/p/strong"
        self.summary_ks_number_xpath = "//div/dt[contains(text(),  'Numer KS')]/../..//dd"
        self.summary_kz_number_xpath = "//div/dt[contains(text(),  'Numer KZ')]/../..//dd"
        self.summary_loading_date_xpath = "//*[@id='step3']/div/div[10]/dl[3]/div[2]/dd"
        self.summary_loading_time_xpath = "//*[@id='step3']/div/div[10]/dl[4]/div[2]/dd"
        self.summary_delivery_date_xpath = "//*[@id='step3']/div/div[10]/dl[1]/div[2]/dd"
        self.summary_delivery_time_xpath = "//*[@id='step3']/div/div[10]/dl[2]/div[2]/dd"
        self.summary_schedule_xpath = "//div/dt[contains(text(), 'Grafik')]/../..//dd"
        self.summary_vehicle_number_xpath = "//*[@id='step3']/div/div[9]/dl[3]/div[2]/dd"
        self.summary_driver_name_xpath = "//*[@id='step3']/div/div[11]/dl[3]/div[2]/dd"
        self.summary_driver_last_name_xpath = "//*[@id='step3']/div/div[11]/dl[4]/div[2]/dd"
        self.summary_id_type_xpath = "//*[@id='step3']/div/div[12]/dl[1]/div[2]/dd"
        self.summary_id_number_xpath = "//*[@id='step3']/div/div[12]/dl[2]/div[2]/dd"
        self.summary_driver_phone_xpath = "//*[@id='step3']/div/div[12]/dl[3]/div[2]/dd"
        self.summary_price_per_ton_xpath = "//*[@id='step3']/div/div[9]/dl[5]/div[2]/dd"
        self.summary_price_xpath = "//*[@id='step3']/div/div[11]/dl[2]/div[2]/dd"

        self.filters_advice_number_xpath = "//input[@id='w1fieldadvice-number']"
        self.filters_sales_name_xpath = "//input[@id='w1fieldsales-contact-recipient-short-name']"
        self.filters_sales_number_xpath = "//input[@id='w1fieldsales-contact-recipient-number']"
        self.filters_sales_user_xpath = "//span[@aria-owns='select2-w1fieldpurchase-contract-user-ax-id-results']" \
                                        "//input"
        self.filters_contract_supplier_xpath = "//input[@id='w1fieldpurchase-contract-supplier-name']"
        self.filters_sales_contract_xpath = "//input[@id='w1fieldsales-contract-note-invoice']"
        self.filters_sales_contract_number_ks_xpath = "//input[@id='w1fieldsales-contract-number']"
        self.filters_carrier_name_xpath = "//input[@id='w1fieldcarrier-name']"
        self.filters_advice_status_xpath = "//label[text()='Status']/following-sibling::span//input"
        self.filters_recipient_address_xpath = "//span[@aria-owns='select2-w1fieldrecipient-advice-address-address-" \
                                               "id-results']//input"
        self.filters_import_status_xpath = "//label[text()='Status Eksportu']/following-sibling::span//input"
        self.filters_advice_user_xpath = "//input[@id='w1fielduser']"
        self.filters_delivery_date_xpath = "//input[@id='w1fielddelivery-date']"
        self.filters_loading_date_xpath = "//input[@id='w1fieldloading-date']"
        self.filters_product_id_xpath = "//select[@id='w1fieldproduct-id']/following-sibling::span//input"
        self.filters_driver_name_xpath = "//input[@id='w1fielddriver-first-name']"
        self.filters_driver_last_name_xpath = "//input[@id='w1fielddriver-last-name']"
        self.filters_vehicle_number_xpath = "//input[@id='w1fieldvehicle-identification-number']"
        self.filters_button_xpath = "//button[text()='Filtruj']"
        self.filters_delete_xpath = "//a[@title='Wyczyść filtry']"   # przyciski do usuwania filtrów

        self.advice_number_xpath = "//h1[contains(@class, 'a-title')]"
        self.status_button_xpath = "//a[@data-title='Wybierz status']"
        self.status_submit_xpath = "//button[contains(@class, 'editable-submit')]"

        self.redirect_button_xpath = "//a[text()='Przekieruj']"
        self.redirect_new_status_xpath = "//span[@aria-labelledby='select2-advice-new-status-container']"
        self.redirect_odmowa_xpath = "//li[text()='Odmowa']"
        self.redirect_odrzucona_xpath = "//li[text()='Odrzucona']"
        self.redirect_anulowana_xpath = "//li[text()='Anulowana']"
        self.redirect_note_xpath = "//textarea[@name='note']"
        self.redirect_go_to_advice_xpath = "//button[text()='Idź do tworzenia awizacji']"

    @allure.step("Dodawanie awizacji")
    def add_new(self):
        self.logger.info("Dodawanie awizacji")
        self.driver.find_element_by_xpath(self.add_new_xpath).click()
        time.sleep(0.5)

    @allure.step("Dodawanie odbiorcy")
    def add_receiver(self, receiver_input, receiver_contact, receiver_address):
        self.logger.info("Dodawanie odbiorcy")
        self.driver.find_element_by_xpath(self.receiver_xpath).click()
        receiver = self.driver.find_element_by_xpath(self.receiver_input_xpath)
        receiver.click()
        receiver.send_keys(receiver_input)
        receiver_input_option_xpath = "//li//span[text()='" + receiver_input + "']/.."
        self.wait.until(ec.element_to_be_clickable((By.XPATH, receiver_input_option_xpath)))
        self.driver.find_element_by_xpath(receiver_input_option_xpath).click()

        self.driver.find_element_by_xpath(self.receiver_contact_xpath).click()
        receiver_contact_option_xpath = "//span[@class='select2-results']//li[text()='" + receiver_contact + "']"
        self.wait.until(ec.element_to_be_clickable((By.XPATH, receiver_contact_option_xpath)))
        self.driver.find_element_by_xpath(receiver_contact_option_xpath).click()

        self.driver.find_element_by_xpath(self.receiver_address_xpath).click()
        receiver_address_option_xpath = "//span[@class='select2-results']//li[text()='" + receiver_address + "']"
        self.wait.until(ec.element_to_be_clickable((By.XPATH, receiver_address_option_xpath)))
        self.driver.find_element_by_xpath(receiver_address_option_xpath).click()

    @allure.step("Dodawanie odbiorcy (bez osoby kontaktowej i adresu)")
    def add_receiver_without_contact_address(self, receiver_input):
        self.logger.info("Dodawanie odbiorcy (bez osoby kontaktowej i adresu)")
        self.driver.find_element_by_xpath(self.receiver_xpath).click()
        receiver = self.driver.find_element_by_xpath(self.receiver_input_xpath)
        receiver.click()
        receiver.send_keys(receiver_input)
        receiver_input_option_xpath = "//li//span[2][text()='" + receiver_input + "']/.."
        self.wait.until(ec.element_to_be_clickable((By.XPATH, receiver_input_option_xpath)))
        self.driver.find_element_by_xpath(self.receiver_input_option_xpath).click()

    @allure.step("Dodawanie nadawcy")
    def add_deliverer(self, deliverer_input, deliverer_contact, deliverer_address):
        self.logger.info("Dodawanie nadawcy")
        self.driver.find_element_by_xpath(self.deliverer_xpath).click()
        deliverer = self.driver.find_element_by_xpath(self.deliverer_input_xpath)
        deliverer.click()
        deliverer.send_keys(deliverer_input)
        deliverer_input_option_xpath = "//li//span[text()='" + deliverer_input + "']/.."
        self.wait.until(ec.element_to_be_clickable((By.XPATH, deliverer_input_option_xpath)))
        self.driver.find_element_by_xpath(deliverer_input_option_xpath).click()

        self.driver.find_element_by_xpath(self.deliverer_contact_xpath).click()
        deliverer_contact_option_xpath = "//span[@class='select2-results']//li[text()='" + deliverer_contact + "']"
        self.wait.until(ec.element_to_be_clickable((By.XPATH, deliverer_contact_option_xpath)))
        self.driver.find_element_by_xpath(deliverer_contact_option_xpath).click()

        self.driver.find_element_by_xpath(self.deliverer_address_xpath).click()
        deliverer_address_option_xpath = "//span[@class='select2-results']//li[text()='" + deliverer_address + "']"
        self.wait.until(ec.element_to_be_clickable((By.XPATH, deliverer_address_option_xpath)))
        self.driver.find_element_by_xpath(deliverer_address_option_xpath).click()

    @allure.step("Dodawanie nadawcy (bez osoby kontaktowej i adresu)")
    def add_deliverer_without_contact_address(self, deliverer_input):
        self.logger.info("Dodawanie nadawcy (bez osoby kontaktowej i adresu)")
        self.driver.find_element_by_xpath(self.deliverer_xpath).click()
        deliverer = self.driver.find_element_by_xpath(self.deliverer_input_xpath)
        deliverer.click()
        deliverer.send_keys(deliverer_input)
        deliverer_input_option_xpath = "//li//span[2][text()='" + deliverer_input + "']/.."
        self.wait.until(ec.element_to_be_clickable((By.XPATH, deliverer_input_option_xpath)))
        self.driver.find_element_by_xpath(deliverer_input_option_xpath).click()

    @allure.step("Przejscie do nastepnej strony (dane przewoznika)")
    def go_to_carriage(self):
        self.logger.info("Przejscie do nastepnej strony (dane przewoznika)")
        self.driver.find_element_by_xpath(self.go_to_carriage_button).click()

    @allure.step("Dodawanie przewoznika")
    def add_carrier(self):
        self.logger.info("Dodawanie przewoznika")
        self.driver.find_element_by_xpath(self.carrier_xpath).click()
        self.wait.until(ec.element_to_be_clickable((By.XPATH, self.carrier_option_xpath)))
        self.driver.find_element_by_xpath(self.carrier_option_xpath).click()

        self.driver.find_element_by_xpath(self.carrier_contact_xpath).click()
        self.wait.until(ec.element_to_be_clickable((By.XPATH, self.carrier_contact_option_xpath)))
        self.driver.find_element_by_xpath(self.carrier_contact_option_xpath).click()

    @allure.step("Dodawanie danych przewozu")
    def add_carriage_data(self, loading_date, loading_time_from, loading_time_to, delivery_date, delivery_time_from,
                          delivery_time_to, vehicle_number, driver_name, driver_last_name, id_type, id_number,
                          driver_phone, price_per_ton):
        self.logger.info("Dodawanie danych przewozu")
        load = self.driver.find_element_by_xpath(self.loading_date_xpath)
        load.click()
        load.send_keys(loading_date)
        load_time_from = self.driver.find_element_by_xpath(self.loading_time_from_xpath)
        load_time_from.click()
        load_time_from.clear()
        load_time_from.send_keys(loading_time_from)
        load_time_to = self.driver.find_element_by_xpath(self.loading_time_to_xpath)
        load_time_to.click()
        load_time_to.clear()
        load_time_to.send_keys(loading_time_to)

        deliv = self.driver.find_element_by_xpath(self.delivery_date_xpath)
        deliv.click()
        deliv.send_keys(delivery_date)
        deliv_time_from = self.driver.find_element_by_xpath(self.delivery_time_from_xpath)
        deliv_time_from.click()
        deliv_time_from.clear()
        deliv_time_from.send_keys(delivery_time_from)
        deliv_time_to = self.driver.find_element_by_xpath(self.delivery_time_to_xpath)
        deliv_time_to.click()
        deliv_time_to.clear()
        deliv_time_to.send_keys(delivery_time_to)

        vehicle = self.driver.find_element_by_xpath(self.vehicle_number_xpath)
        vehicle.click()
        vehicle.send_keys(vehicle_number)

        name = self.driver.find_element_by_xpath(self.driver_name_xpath)
        name.click()
        name.send_keys(driver_name)
        name.click()

        last_name = self.driver.find_element_by_xpath(self.driver_last_name_xpath)
        last_name.click()
        last_name.send_keys(driver_last_name)
        last_name.click()

        id_t = self.driver.find_element_by_xpath(self.id_type_xpath)
        id_t.click()
        if id_type == 'dowód osobisty':
            dowod = "//*[@id='select2-identification-type-id-results']/li[1]"
            self.wait.until(ec.element_to_be_clickable((By.XPATH, dowod)))
            self.driver.find_element_by_xpath(dowod).click()
        elif id_type == 'paszport':
            paszport = "//*[@id='select2-identification-type-id-results']/li[2]"
            self.wait.until(ec.element_to_be_clickable((By.XPATH, paszport)))
            self.driver.find_element_by_xpath(paszport).click()

        id_num = self.driver.find_element_by_xpath(self.id_number_xpath)
        id_num.click()
        id_num.send_keys(id_number)

        phone = self.driver.find_element_by_xpath(self.driver_phone_xpath)
        phone.click()
        phone.send_keys(driver_phone)

        price_per = self.driver.find_element_by_xpath(self.price_per_ton_xpath)
        price_per.click()
        price_per.send_keys(price_per_ton)

    @allure.step("Dodawanie danych przewozu")
    def add_carriage_data_schedule(self, loading_date, delivery_date, vehicle_number, driver_name, driver_last_name,
                                   id_type, id_number, driver_phone, price_per_ton, schedule):
        self.logger.info("Dodawanie danych przewozu")
        deliv = self.driver.find_element_by_xpath(self.delivery_date_xpath)
        deliv.click()
        deliv.send_keys(delivery_date)

        load = self.driver.find_element_by_xpath(self.loading_date_xpath)
        load.click()
        load.send_keys(loading_date)

        schedule_input = self.driver.find_element_by_xpath(self.schedule_xpath)
        schedule_input.click()
        schedule_option = "//li[contains(text(), '" + schedule + "')]"
        self.wait.until(ec.element_to_be_clickable((By.XPATH, schedule_option)))
        self.driver.find_element_by_xpath(schedule_option).click()

        vehicle = self.driver.find_element_by_xpath(self.vehicle_number_xpath)
        vehicle.click()
        vehicle.send_keys(vehicle_number)

        name = self.driver.find_element_by_xpath(self.driver_name_xpath)
        name.click()
        name.send_keys(driver_name)
        name.click()

        last_name = self.driver.find_element_by_xpath(self.driver_last_name_xpath)
        last_name.click()
        last_name.send_keys(driver_last_name)
        last_name.click()

        id_t = self.driver.find_element_by_xpath(self.id_type_xpath)
        id_t.click()
        if id_type == 'dowód osobisty':
            dowod = "//*[@id='select2-identification-type-id-results']/li[1]"
            self.wait.until(ec.element_to_be_clickable((By.XPATH, dowod)))
            self.driver.find_element_by_xpath(dowod).click()
        elif id_type == 'paszport':
            paszport = "//*[@id='select2-identification-type-id-results']/li[2]"
            self.wait.until(ec.element_to_be_clickable((By.XPATH, paszport)))
            self.driver.find_element_by_xpath(paszport).click()

        id_num = self.driver.find_element_by_xpath(self.id_number_xpath)
        id_num.click()
        id_num.send_keys(id_number)

        phone = self.driver.find_element_by_xpath(self.driver_phone_xpath)
        phone.click()
        phone.send_keys(driver_phone)

        price_per = self.driver.find_element_by_xpath(self.price_per_ton_xpath)
        price_per.click()
        price_per.send_keys(price_per_ton)

    @allure.step("Dodawanie danych przewozu")
    def add_carriage_data_planner(self, vehicle_number, driver_name, driver_last_name, id_type, id_number,
                                  driver_phone, schedule):
        self.logger.info("Dodawanie danych przewozu")

        schedule_input = self.driver.find_element_by_xpath(self.schedule_xpath)
        schedule_input.click()
        schedule_option = "//li[contains(text(), '" + schedule + "')]"
        self.wait.until(ec.element_to_be_clickable((By.XPATH, schedule_option)))
        self.driver.find_element_by_xpath(schedule_option).click()

        vehicle = self.driver.find_element_by_xpath(self.vehicle_number_xpath)
        vehicle.click()
        vehicle.send_keys(vehicle_number)

        name = self.driver.find_element_by_xpath(self.driver_name_xpath)
        name.click()
        name.send_keys(driver_name)
        name.click()

        last_name = self.driver.find_element_by_xpath(self.driver_last_name_xpath)
        last_name.click()
        last_name.send_keys(driver_last_name)
        last_name.click()

        id_t = self.driver.find_element_by_xpath(self.id_type_xpath)
        id_t.click()
        if id_type == 'dowód osobisty':
            dowod = "//*[@id='select2-identification-type-id-results']/li[1]"
            self.wait.until(ec.element_to_be_clickable((By.XPATH, dowod)))
            self.driver.find_element_by_xpath(dowod).click()
        elif id_type == 'paszport':
            paszport = "//*[@id='select2-identification-type-id-results']/li[2]"
            self.wait.until(ec.element_to_be_clickable((By.XPATH, paszport)))
            self.driver.find_element_by_xpath(paszport).click()

        id_num = self.driver.find_element_by_xpath(self.id_number_xpath)
        id_num.click()
        id_num.send_keys(id_number)

        phone = self.driver.find_element_by_xpath(self.driver_phone_xpath)
        phone.click()
        phone.send_keys(driver_phone)

    @allure.step("Przejscie do nastepnej strony (podsumowanie)")
    def go_to_summary(self):
        self.logger.info("Przejscie do nastepnej strony (podsumowanie)")
        self.driver.find_element_by_xpath(self.go_to_summary_button).click()

    @allure.step("Walidacja danych w podsumowaniu")
    def validate_data(self, receiver_input, deliverer_input, loading_date, loading_time_from, loading_time_to,
                      delivery_date, delivery_time_from, delivery_time_to, vehicle_number, driver_name,
                      driver_last_name, id_type, id_number, driver_phone, price_per_ton):
        if len(receiver_input) <= 9 and len(deliverer_input) <= 9:
            summary_rec_xpath = "//dt[text()='Numer KS']/../..//dd"
            summary_rec = self.driver.find_element_by_xpath(summary_rec_xpath).text
            assert receiver_input in summary_rec, "1: {}, 2: {}".format(receiver_input, summary_rec)

            summary_deliv_xpath = "//dt[text()='Numer KZ']/../..//dd"
            summary_deliv = self.driver.find_element_by_xpath(summary_deliv_xpath).text
            assert deliverer_input in summary_deliv
        else:
            summary_rec = self.driver.find_element_by_xpath(self.summary_receiver_xpath).text
            assert summary_rec == receiver_input

            summary_deliv = self.driver.find_element_by_xpath(self.summary_deliverer_xpath).text
            assert summary_deliv == deliverer_input

        summary_loading_date = self.driver.find_element_by_xpath(self.summary_loading_date_xpath).text
        assert summary_loading_date == loading_date

        summary_loading_time = self.driver.find_element_by_xpath(self.summary_loading_time_xpath).text
        loading_time = loading_time_from + ' - ' + loading_time_to
        assert summary_loading_time == loading_time

        summary_delivery_date = self.driver.find_element_by_xpath(self.summary_delivery_date_xpath).text
        assert summary_delivery_date == delivery_date

        summary_delivery_time = self.driver.find_element_by_xpath(self.summary_delivery_time_xpath).text
        delivery_time = delivery_time_from + ' - ' + delivery_time_to
        assert summary_delivery_time == delivery_time

        summary_vehicle_number = self.driver.find_element_by_xpath(self.summary_vehicle_number_xpath).text
        assert summary_vehicle_number == vehicle_number

        summary_driver_name = self.driver.find_element_by_xpath(self.summary_driver_name_xpath).text
        assert summary_driver_name == driver_name

        summary_driver_last_name = self.driver.find_element_by_xpath(self.summary_driver_last_name_xpath).text
        assert summary_driver_last_name == driver_last_name

        summary_id_type = self.driver.find_element_by_xpath(self.summary_id_type_xpath).text
        assert summary_id_type == id_type

        summary_id_number = self.driver.find_element_by_xpath(self.summary_id_number_xpath).text
        assert summary_id_number == id_number

        summary_phone = self.driver.find_element_by_xpath(self.summary_driver_phone_xpath).text
        assert summary_phone == driver_phone

        summary_price_per = self.driver.find_element_by_xpath(self.summary_price_per_ton_xpath).text
        price_per = str(price_per_ton) + '.00 pln'
        assert summary_price_per == price_per

        summary_price = self.driver.find_element_by_xpath(self.summary_price_xpath).text
        price = str(25 * price_per_ton) + '.00 pln'
        assert summary_price == price

    @allure.step("Walidacja danych w podsumowaniu")
    def validate_data_schedule(self, receiver_input, deliverer_input, loading_date, delivery_date, vehicle_number,
                               driver_name, driver_last_name, id_type, id_number, driver_phone, price_per_ton,
                               schedule):
        if len(receiver_input) <= 9 and len(deliverer_input) <= 9:
            summary_rec_xpath = "//dt[text()='Numer KS']/../..//dd"
            summary_rec = self.driver.find_element_by_xpath(summary_rec_xpath).text
            assert receiver_input in summary_rec, "1: {}, 2: {}".format(receiver_input, summary_rec)

            summary_deliv_xpath = "//dt[text()='Numer KZ']/../..//dd"
            summary_deliv = self.driver.find_element_by_xpath(summary_deliv_xpath).text
            assert deliverer_input in summary_deliv
        else:
            summary_rec = self.driver.find_element_by_xpath(self.summary_receiver_xpath).text
            assert summary_rec == receiver_input

            summary_deliv = self.driver.find_element_by_xpath(self.summary_deliverer_xpath).text
            assert summary_deliv == deliverer_input

        summary_loading_date = self.driver.find_element_by_xpath(self.summary_loading_date_xpath).text
        assert summary_loading_date == loading_date

        summary_delivery_date = self.driver.find_element_by_xpath(self.summary_delivery_date_xpath).text
        assert summary_delivery_date == delivery_date

        summary_schedule = self.driver.find_element_by_xpath(self.summary_schedule_xpath).text
        assert schedule[0:10] in summary_schedule

        summary_vehicle_number = self.driver.find_element_by_xpath(self.summary_vehicle_number_xpath).text
        assert summary_vehicle_number == vehicle_number

        summary_driver_name = self.driver.find_element_by_xpath(self.summary_driver_name_xpath).text
        assert summary_driver_name == driver_name

        summary_driver_last_name = self.driver.find_element_by_xpath(self.summary_driver_last_name_xpath).text
        assert summary_driver_last_name == driver_last_name

        summary_id_type = self.driver.find_element_by_xpath(self.summary_id_type_xpath).text
        assert summary_id_type == id_type

        summary_id_number = self.driver.find_element_by_xpath(self.summary_id_number_xpath).text
        assert summary_id_number == id_number

        summary_phone = self.driver.find_element_by_xpath(self.summary_driver_phone_xpath).text
        assert summary_phone == driver_phone

        summary_price_per = self.driver.find_element_by_xpath(self.summary_price_per_ton_xpath).text
        price_per = str(price_per_ton) + '.00 pln'
        assert summary_price_per == price_per

        summary_price = self.driver.find_element_by_xpath(self.summary_price_xpath).text
        price = str(25 * price_per_ton) + '.00 pln'
        assert summary_price == price

    @allure.step("Zapisanie awizacji")
    def save(self):
        self.logger.info("Zapisanie awizacji")
        self.driver.find_element_by_xpath(self.save_button).click()
        self.wait.until(ec.visibility_of_element_located((By.XPATH, "//div/button[@data-dismiss='alert']")))
        time.sleep(0.5)

    @allure.step("Zapisanie awizacji po edycji")
    def save_edited(self):
        self.logger.info("Zapisanie awizacji po edycji")
        self.driver.find_element_by_xpath(self.save_button).click()
        #self.wait.until(ec.visibility_of_element_located((By.XPATH, "//div/button[@data-dismiss='alert']")))
        time.sleep(5)

    @allure.step("Usuwanie awizacji")
    def delete(self, receiver, deliverer):
        self.logger.info("Usuwanie awizacji")
        if len(receiver) <= 9 and len(deliverer) <= 9:
            deletion_xpath = "//a[contains(text(), '" + receiver + " ')]/../..//a[contains(text(), '" + deliverer + \
                             " ')]/../..//a[4]"
        else:
            deletion_xpath = "//td[text()='" + receiver + "']/following-sibling::td[text()='" + deliverer + \
                        "']/..//a[4]"
        self.wait.until(ec.element_to_be_clickable((By.XPATH, deletion_xpath)))
        self.driver.find_element_by_xpath(deletion_xpath).click()

    @allure.step("Usuwanie awizacji po numerze")
    def delete_number(self, advice):
        self.logger.info("Usuwanie awizacji po numerze")
        deletion_xpath = "//a[contains(text(), '" + advice + "')]/../..//a[4]"
        self.wait.until(ec.element_to_be_clickable((By.XPATH, deletion_xpath)))
        self.driver.find_element_by_xpath(deletion_xpath).click()

    @allure.step("Potwierdzenie usuniecia awizacji")
    def confirm_delete(self):
        self.logger.info("Potwierdzenie usuniecia awizacji")
        self.wait.until(ec.element_to_be_clickable((By.XPATH, self.confirm_delete_xpath)))
        self.driver.find_element_by_xpath(self.confirm_delete_xpath).click()

    @allure.step("Wejscie w pojedyncza awizacje")
    def get_into_aw(self):
        self.logger.info("Wejscie w pojedyncza awizacje")
        self.wait.until(ec.element_to_be_clickable((By.XPATH, self.first_aw_xpath)))
        self.driver.find_element_by_xpath(self.first_aw_xpath).click()

    @allure.step("Wejscie w pojedyncza awizacje po numerze")
    def get_into_aw_number(self, advice):
        self.logger.info("Wejscie w pojedyncza awizacje po numerze")
        self.wait.until(ec.element_to_be_clickable((By.XPATH, self.search_input_xpath)))
        search_input = self.driver.find_element_by_xpath(self.search_input_xpath)
        search_input.click()
        search_input.clear()
        search_input.send_keys(advice)
        search_input.send_keys(Keys.ENTER)
        time.sleep(1)
        self.wait.until(ec.element_to_be_clickable((By.XPATH, self.first_aw_xpath)))
        self.driver.find_element_by_xpath(self.first_aw_xpath).click()

    @allure.step("Wejscie w edycje awizacji z widoku szczegolow awizacji")
    def edit_opened_aw(self):
        self.logger.info("Wejscie w edycje awizacji z widoku szczegolow awizacji")
        self.wait.until(ec.element_to_be_clickable((By.XPATH, self.edit_opened_aw_xpath)))
        self.driver.find_element_by_xpath(self.edit_opened_aw_xpath).click()

    @allure.step("Wejscie w edycje awizacji")
    def edit_first(self):
        self.logger.info("Wejscie w edycje awizacji")
        self.wait.until(ec.element_to_be_clickable((By.XPATH, self.edit_first_xpath)))
        self.driver.find_element_by_xpath(self.edit_first_xpath).click()

    @allure.step("Edycja awizacji (adres odbiorcy)")
    def edit_receiver_address(self):
        self.logger.info("Edycja awizacji (adres odbiorcy)")
        self.wait.until(ec.element_to_be_clickable((By.XPATH, self.receiver_address_xpath)))
        self.driver.find_element_by_xpath(self.receiver_address_xpath).click()
        self.wait.until((ec.element_to_be_clickable((By.XPATH, self.receiver_address_option_xpath))))
        self.driver.find_element_by_xpath(self.receiver_address_option_xpath).click()
        time.sleep(3)
        #self.wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@id='travel-time']")))

    @allure.step("Edycja przewoznika (stawka transportowa)")
    def edit_carrier_price_per_ton(self, new_price):
        self.logger.info("Edycja przewoznika (stawka transportowa)")
        price = self.driver.find_element_by_xpath(self.price_per_ton_xpath)
        price.click()
        price.clear()
        price.send_keys(new_price)

    @allure.step("Klonowanie awizacji")
    def clone_aw(self, receiver, deliverer):
        self.logger.info("Klonowanie awizacji")
        clone_xpath = "//a[text()='" + receiver + " ']/../..//a[text()='" + deliverer + \
                      " ']/../..//a[@title='Klonuj']"
        self.driver.find_element_by_xpath(clone_xpath).click()

    @allure.step("Uzupelnienie danych klonowanej awizacji")
    def add_carriage_data_clone(self, delivery_date, schedule):
        self.logger.info("Uzupelnienie danych klonowanej awizacji")
        deliv = self.driver.find_element_by_xpath(self.delivery_date_xpath)
        deliv.click()
        deliv.send_keys(delivery_date)

        schedule_input = self.driver.find_element_by_xpath(self.schedule_xpath)
        schedule_input.click()
        schedule_option = "//li[contains(text(), '" + schedule + "')]"
        self.wait.until(ec.element_to_be_clickable((By.XPATH, schedule_option)))
        self.driver.find_element_by_xpath(schedule_option).click()

    @allure.step("Exportowanie listy awizacji do xlsx")
    def export_xlsx(self):
        self.logger.info("Exportowanie listy awizacji do xlsx")
        self.driver.find_element_by_xpath(self.export_xlsx_xpath).click()

    @allure.step("Exportowanie listy awizacji do csv")
    def export_csv(self):
        self.logger.info("Exportowanie listy awizacji do csv")
        self.driver.find_element_by_xpath(self.export_csv_xpath).click()

    @allure.step("Otwieranie filtrow")
    def open_filters(self):
        self.logger.info("Otwieranie filtrow")
        self.driver.find_element_by_xpath(self.filters_xpath).click()

    @allure.step("Filtr: numer awizacji")
    def set_filter_advice_number(self, advice_number):
        self.logger.info("Filtr: numer awizacji")
        filter_input = self.driver.find_element_by_xpath(self.filters_advice_number_xpath)
        filter_input.click()
        filter_input.send_keys(advice_number)

    @allure.step("Filtr: nazwa skr. odb.")
    def set_filter_sales_name(self, sales_name):
        self.logger.info("Filtr: nazwa skr. odb.")
        filter_input = self.driver.find_element_by_xpath(self.filters_sales_name_xpath)
        filter_input.click()
        filter_input.send_keys(sales_name)

    @allure.step("Filtr: nr odbiorcy")
    def set_filter_sales_number(self, sales_number):
        self.logger.info("Filtr: nr odbiorcy")
        filter_input = self.driver.find_element_by_xpath(self.filters_sales_number_xpath)
        filter_input.click()
        filter_input.send_keys(sales_number)

    @allure.step("Filtr: osoba odpow.")
    def set_filter_sales_user(self, sales_user):
        self.logger.info("Filtr: osoba odpow.")
        filter_input = self.driver.find_element_by_xpath(self.filters_sales_user_xpath)
        filter_input.click()
        filter_input.send_keys(sales_user)
        filter_input_option_xpath = "//li[text()='" + sales_user + "']"
        self.wait.until(ec.element_to_be_clickable((By.XPATH, filter_input_option_xpath)))
        self.driver.find_element_by_xpath(filter_input_option_xpath).click()

    @allure.step("Filtr: nazwa dostawcy")
    def set_filter_contract_supplier(self, contract_supplier):
        self.logger.info("Filtr: nazwa dostawcy")
        filter_input = self.driver.find_element_by_xpath(self.filters_contract_supplier_xpath)
        filter_input.click()
        filter_input.send_keys(contract_supplier)

    @allure.step("Filtr: nr umowy odbiorcy")
    def set_filter_sales_contract(self, sales_contract):
        self.logger.info("Filtr: nr umowy odbiorcy")
        filter_input = self.driver.find_element_by_xpath(self.filters_sales_contract_xpath)
        filter_input.click()
        filter_input.send_keys(sales_contract)

    @allure.step("Filtr: nr umowy KS")
    def set_filter_sales_contract_number(self, sales_contract_number):
        self.logger.info("Filtr: nr umowy KS")
        filter_input = self.driver.find_element_by_xpath(self.filters_sales_contract_number_ks_xpath)
        filter_input.click()
        filter_input.send_keys(sales_contract_number)

    @allure.step("Filtr: przewoznik")
    def set_filter_carrier_name(self, carrier_name):
        self.logger.info("Filtr: przewoznik")
        filter_input = self.driver.find_element_by_xpath(self.filters_carrier_name_xpath)
        filter_input.click()
        filter_input.send_keys(carrier_name)

    @allure.step("Filtr: status")
    def set_filter_advice_status(self, status):
        self.logger.info("Filtr: status")
        filter_input = self.driver.find_element_by_xpath(self.filters_advice_status_xpath)
        filter_input.click()
        filter_input.send_keys(status)
        filter_input_option_xpath = "//li[text()='" + status + "']"
        self.wait.until(ec.element_to_be_clickable((By.XPATH, filter_input_option_xpath)))
        self.driver.find_element_by_xpath(filter_input_option_xpath).click()

    @allure.step("Filtr: adres dostawy")
    def set_filter_recipient_address(self, recipient_address):
        self.logger.info("Filtr: adres dostawy")
        filter_input = self.driver.find_element_by_xpath(self.filters_recipient_address_xpath)
        filter_input.click()
        filter_input.send_keys(recipient_address)
        filter_input_option_xpath = "//li[text()='" + recipient_address + "']"
        self.wait.until(ec.element_to_be_clickable((By.XPATH, filter_input_option_xpath)))
        self.driver.find_element_by_xpath(filter_input_option_xpath).click()

    @allure.step("Filtr: status eksportu")
    def set_filter_import_status(self, import_status):
        self.logger.info("Filtr: status eksportu")
        filter_input = self.driver.find_element_by_xpath(self.filters_import_status_xpath)
        filter_input.click()
        filter_input.send_keys(import_status)
        filter_input_option_xpath = "//li[text()='" + import_status + "']"
        self.wait.until(ec.element_to_be_clickable((By.XPATH, filter_input_option_xpath)))
        self.driver.find_element_by_xpath(filter_input_option_xpath).click()

    @allure.step("Filtr: osoba awizujaca")
    def set_filter_advice_user(self, advice_user):
        self.logger.info("Filtr: osoba awizujaca")
        filter_input = self.driver.find_element_by_xpath(self.filters_advice_user_xpath)
        filter_input.click()
        filter_input.send_keys(advice_user)

    @allure.step("Filtr: data dostawy")
    def set_filter_delivery_date(self, delivery_date):
        self.logger.info("Filtr: data dostawy")
        filter_input = self.driver.find_element_by_xpath(self.filters_delivery_date_xpath)
        filter_input.click()
        filter_input.send_keys(delivery_date)

    @allure.step("Filtr: data zaladunku")
    def set_filter_loading_date(self, loading_date):
        self.logger.info("Filtr: data zaladunku")
        filter_input = self.driver.find_element_by_xpath(self.filters_loading_date_xpath)
        filter_input.click()
        filter_input.send_keys(loading_date)

    @allure.step("Filtr: produkt")
    def set_filter_product_id(self, product_id):
        self.logger.info("Filtr: produkt")
        filter_input = self.driver.find_element_by_xpath(self.filters_product_id_xpath)
        filter_input.click()
        filter_input.send_keys(product_id)
        filter_input_option_xpath = "//li[text()='" + product_id + "']"
        self.wait.until(ec.element_to_be_clickable((By.XPATH, filter_input_option_xpath)))
        self.driver.find_element_by_xpath(filter_input_option_xpath).click()

    @allure.step("Filtr: imie kierowcy")
    def set_filter_driver_name(self, driver_name):
        self.logger.info("Filtr: imie kierowcy")
        filter_input = self.driver.find_element_by_xpath(self.filters_driver_name_xpath)
        filter_input.click()
        filter_input.send_keys(driver_name)

    @allure.step("Filtr: nazwisko kierowcy")
    def set_filter_driver_last_name(self, driver_last_name):
        self.logger.info("Filtr: nazwisko kierowcy")
        filter_input = self.driver.find_element_by_xpath(self.filters_driver_last_name_xpath)
        filter_input.click()
        filter_input.send_keys(driver_last_name)

    @allure.step("Filtr: nr pojazdu/naczepy")
    def set_filter_vehicle_number(self, vehicle_number):
        self.logger.info("Filtr: nr pojazdu/naczepy")
        filter_input = self.driver.find_element_by_xpath(self.filters_vehicle_number_xpath)
        filter_input.click()
        filter_input.send_keys(vehicle_number)

    @allure.step("Zastosowanie filtrow")
    def use_filters(self):
        self.logger.info("Zastosowanie filtrow")
        self.driver.find_element_by_xpath(self.filters_button_xpath).click()

    @allure.step("Usuwanie filtrow")
    def delete_filters(self):
        self.logger.info("Usuwanie filtrow")
        self.short_wait.until_not(ec.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'sk-loading')]")))
        self.wait.until(ec.element_to_be_clickable((By.XPATH, self.filters_delete_xpath)))
        self.driver.find_element_by_xpath(self.filters_delete_xpath).click()

    @allure.step("Pobranie numeru utworzonej AW")
    def get_advice_number(self):
        self.logger.info("Pobranie numeru utworzonej AW")
        advice = self.driver.find_element_by_xpath(self.advice_number_xpath).text
        self.logger.info(advice)
        return advice

    @allure.step("Zmiana statusu awizacji")
    def change_advice_status(self, new_status):
        self.logger.info("Zmiana statusu awizacji")
        self.driver.find_element_by_xpath(self.status_button_xpath).click()
        new_status_xpath = "//li[text()='" + new_status + "']"
        option = self.driver.find_element_by_xpath(new_status_xpath)
        option.click()
        self.driver.find_element_by_xpath(self.status_submit_xpath).click()

    @allure.step("Pobranie aktualnego statusu awizacji")
    def get_advice_status(self):
        self.logger.info("Pobranie aktualnego statusu awizacji")
        status = self.driver.find_element_by_xpath(self.status_button_xpath).text
        return status

    @allure.step("Pobranie aktualnego statusu awizacji z listy awizacji")
    def get_advice_status_from_list(self, advice):
        self.logger.info("Pobranie aktualnego statusu awizacji z listy awizacji")
        status = self.driver.find_element_by_xpath("//td[@data-label='#']/a[text()='" + advice + "']"
                                                   "/../../td[@data-label='Status awizacji']").text
        return status

    @allure.step("Przejscie do przekierowania awizacji")
    def go_to_redirect_advice(self):
        self.logger.info("Przejscie do przekierowania awizacji")
        self.wait.until(ec.element_to_be_clickable((By.XPATH, self.redirect_button_xpath)))
        self.driver.find_element_by_xpath(self.redirect_button_xpath).click()

    @allure.step("Przekierowanie awizacji")
    def redirect_advice(self, status):
        self.logger.info("Przekierowanie awizacji")
        self.driver.find_element_by_xpath(self.redirect_new_status_xpath).click()
        if status == "Odmowa":
            self.driver.find_element_by_xpath(self.redirect_odmowa_xpath).click()
        elif status == "Odrzucona":
            self.driver.find_element_by_xpath(self.redirect_odrzucona_xpath).click()
        elif status == "Anulowana":
            self.driver.find_element_by_xpath(self.redirect_anulowana_xpath).click()

    @allure.step("Dodanie notatki do przekierowania aw")
    def redirect_add_note(self, note):
        self.logger.info("Dodanie notatki do przekierowania aw")
        note_input = self.driver.find_element_by_xpath(self.redirect_note_xpath)
        note_input.click()
        note_input.send_keys(note)

    @allure.step("Przejscie do tworzenia nowej aw")
    def go_to_new_advice(self):
        self.logger.info("Przejscie do tworzenia nowej aw")
        self.driver.find_element_by_xpath(self.redirect_go_to_advice_xpath).click()
