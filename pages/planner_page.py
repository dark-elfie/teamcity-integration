import logging
import allure
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class PlannerPage:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.wait = WebDriverWait(self.driver, 15)
        self.add_new_xpath = "//a[text()='Dodaj nowy']"
        self.open_filters_xpath = "//a[@data-filters-toggle]"

        self.filters_row_id_xpath = "//label[text()='#']/../following-sibling::input"
        self.filters_product_xpath = "//label[text()='Produkt']/following-sibling::span//input"
        self.filters_deliverer_xpath = "//label[text()='Nazwa Dostawcy']/following-sibling::span//input"
        self.filters_deliverer_address_xpath = "//label[text()='Adres odbioru']/../following-sibling::input"
        self.filters_loading_date_xpath = "//label[text()='Data załadunku']/../following-sibling::input"
        self.filters_delivery_date_xpath = "//label[text()='Data dostawy']/../following-sibling::input"
        self.filters_receiver_xpath = "//label[text()='Nazwa Odbiorcy']/following-sibling::span//input"
        self.filters_receiver_address_xpath = "//label[text()='Adres dostawy']/../following-sibling::input"
        self.filters_carrier_xpath = "//label[text()='Przewoźnik']/following-sibling::span//input"
        self.filters_price_per_t_from = "//label[text()='Stawka/t od']/../following-sibling::input"
        self.filters_price_per_t_to = "//label[text()='Stawka/t do']/../following-sibling::input"
        self.filters_price_per_t_currency_xpath = "//label[text()='Stawka/t - waluta']/following-sibling::span//input"
        self.filters_price_from_xpath = "//label[text()='Fracht od']/../following-sibling::input"
        self.filters_price_to_xpath = "//label[text()='Fracht do']/../following-sibling::input"
        self.filters_price_currency_xpath = "//label[text()='Fracht - waluta']/following-sibling::span//input"
        self.filters_original_advice_xpath = "//label[text()='Nr pierwotny AW']/../following-sibling::input"
        self.filters_advice_xpath = "//label[text()='Nr AW']/../following-sibling::input"
        self.filters_kz_xpath = "//label[text()='KZ']/following-sibling::span//input"
        self.filters_ks_xpath = "//label[text()='KS']/following-sibling::span//input"
        self.filters_status_xpath = "//label[text()='Status']/following-sibling::span//input"
        self.filters_advicing_person = "//label[text()='Osoba awizująca']/following-sibling::span//input"
        self.filters_hide_xpath = "//input[@id='w1fieldhide-delivered-and-canceled-advices']"
        self.use_filters_button_xpath = "//button[text()='Filtruj']"
        self.delete_filters_xpath = "//a[@title='Wyczyść filtry']"

        self.ks_xpath = "//tr[1]/td[@data-title='Wybierz KS']"
        self.ks_input_xpath = "//h3[text()='Wybierz KS']/../following-sibling::span" \
                              "//input[@class='select2-search__field']"
        self.kz_xpath = "//tr[1]/td[@data-title='Wybierz KZ']"
        self.kz_input_xpath = "//h3[text()='Wybierz KZ']/../following-sibling::span" \
                              "//input[@class='select2-search__field']"
        self.loading_date_xpath = "//tr[1]/td[@data-title='Wybierz datę załadunku']"
        self.loading_date_input_xpath = "//h3[text()='Wybierz datę załadunku']/following-sibling::div//input"
        self.delivery_date_xpath = "//tr[1]/td[@data-title='Wybierz datę dostawy']"
        self.delivery_date_input_xpath = "//h3[text()='Wybierz datę dostawy']/following-sibling::div//input"
        self.carrier_xpath = "//tr[1]/td[@data-title='Wybierz przewoźnika']"
        self.carrier_input_xpath = "//h3[text()='Wybierz przewoźnika']/../following-sibling::span//input"
        self.price_xpath = "//tr[1]/td[@data-title='Podaj stawkę transportową']"
        self.price_input_xpath = "//input[@placeholder='Podaj stawkę transportową']"
        self.currency_xpath = "//tr[1]/td[@data-title='Wybierz walutę frachtu']"
        self.currency_eur_xpath = "//li[text()='EUR']"
        self.currency_pln_xpath = "//li[text()='pln']"
        self.submit_buttons_xpath = "//button[contains(@class, 'editable-submit')]"

        self.add_note_xpath = "//tr[1]//a[@title='Notatka']"
        self.note_area_xpath = "//textarea[@id='note']"
        self.save_note_xpath = "//button[text()='Zapisz']"
        self.create_advice_xpath = "//tr[1]//a[@title='Dodaj awizację']"
        self.go_to_ks_xpath = "//tr[1]//a[@title='Przejdź do KS']"
        self.delete_row_xpath = "//tr[1]//a[@data-title='Na pewno usunąć?']"
        self.confirm_delete_xpath = "//a[text()='Usuń']"

        self.next_page_xpath = "//li[contains(@class, 'page-item active')]//following-sibling::li[1]"

    @allure.step("Tworzenie nowego wiersza")
    def add_new_line(self):
        self.logger.info("Tworzenie nowego wiersza")
        self.wait.until(ec.element_to_be_clickable((By.XPATH, self.add_new_xpath)))
        self.driver.find_element_by_xpath(self.add_new_xpath).click()
        self.wait.until(ec.element_to_be_clickable((By.XPATH, "//div[text()='Dodano nowy wiersz']")))
        time.sleep(3)

    @allure.step("Wpisanie numeru KS")
    def set_ks(self, KS):
        self.logger.info("Wpisanie numeru KS")
        self.wait.until(ec.element_to_be_clickable((By.XPATH, self.ks_xpath)))
        self.driver.find_element_by_xpath(self.ks_xpath).click()
        self.wait.until(ec.element_to_be_clickable((By.XPATH, self.ks_input_xpath)))
        ks_input = self.driver.find_element_by_xpath(self.ks_input_xpath)
        ks_input.click()
        ks_input.send_keys(KS)
        ks_xpath = "//li[contains(text(), '" + KS + "')]"
        self.driver.find_element_by_xpath(ks_xpath).click()
        self.driver.find_element_by_xpath(self.submit_buttons_xpath).click()

    @allure.step("Wpisanie numeru KZ")
    def set_kz(self, KZ):
        self.logger.info("Wpisanie numeru KZ")
        self.wait.until(ec.element_to_be_clickable((By.XPATH, self.kz_xpath)))
        self.driver.find_element_by_xpath(self.kz_xpath).click()
        self.wait.until(ec.element_to_be_clickable((By.XPATH, self.kz_input_xpath)))
        kz_input = self.driver.find_element_by_xpath(self.kz_input_xpath)
        kz_input.click()
        kz_input.send_keys(KZ)
        kz_xpath = "//li[contains(text(), '" + KZ + "')]"
        self.driver.find_element_by_xpath(kz_xpath).click()
        self.driver.find_element_by_xpath(self.submit_buttons_xpath).click()

    @allure.step("Wpisanie daty zaladunku")
    def set_loading_date(self, loading_date):
        self.logger.info("Wpisanie daty zaladunku")
        self.wait.until(ec.element_to_be_clickable((By.XPATH, self.loading_date_xpath)))
        self.driver.find_element_by_xpath(self.loading_date_xpath).click()
        self.wait.until(ec.element_to_be_clickable((By.XPATH, self.loading_date_input_xpath)))
        loading_date_input = self.driver.find_element_by_xpath(self.loading_date_input_xpath)
        loading_date_input.click()
        loading_date_input.clear()
        loading_date_input.send_keys(loading_date)
        self.driver.find_element_by_xpath(self.submit_buttons_xpath).click()

    @allure.step("Wpisanie daty dostawy")
    def set_delivery_date(self, delivery_date):
        self.logger.info("Wpisanie daty dostawy")
        self.wait.until(ec.element_to_be_clickable((By.XPATH, self.delivery_date_xpath)))
        self.driver.find_element_by_xpath(self.delivery_date_xpath).click()
        self.wait.until(ec.element_to_be_clickable((By.XPATH, self.delivery_date_input_xpath)))
        delivery_date_input = self.driver.find_element_by_xpath(self.delivery_date_input_xpath)
        delivery_date_input.click()
        delivery_date_input.clear()
        delivery_date_input.send_keys(delivery_date)
        self.driver.find_element_by_xpath(self.submit_buttons_xpath).click()

    @allure.step("Wpisanie przewoznika")
    def set_carrier(self, carrier):
        self.logger.info("Wpisanie przewoznika")
        self.wait.until(ec.element_to_be_clickable((By.XPATH, self.carrier_xpath)))
        self.driver.find_element_by_xpath(self.carrier_xpath).click()
        self.wait.until(ec.element_to_be_clickable((By.XPATH, self.carrier_input_xpath)))
        carrier_input = self.driver.find_element_by_xpath(self.carrier_input_xpath)
        carrier_input.click()
        carrier_input.send_keys(carrier)
        carrier_xpath = "//li[contains(text(), '" + carrier + "')]"
        self.driver.find_element_by_xpath(carrier_xpath).click()
        self.driver.find_element_by_xpath(self.submit_buttons_xpath).click()

    @allure.step("Wpisanie stawki")
    def set_price(self, price):
        self.logger.info("Wpisanie stawki")
        self.wait.until(ec.element_to_be_clickable((By.XPATH, self.price_xpath)))
        self.driver.find_element_by_xpath(self.price_xpath).click()
        self.wait.until(ec.element_to_be_clickable((By.XPATH, self.price_input_xpath)))
        price_input = self.driver.find_element_by_xpath(self.price_input_xpath)
        price_input.click()
        price_input.send_keys(price)
        self.driver.find_element_by_xpath(self.submit_buttons_xpath).click()

    @allure.step("Wpisanie waluty")
    def set_currency(self, currency):
        self.logger.info("Wpisanie waluty")
        self.wait.until(ec.element_to_be_clickable((By.XPATH, self.currency_xpath)))
        self.driver.find_element_by_xpath(self.currency_xpath).click()
        if currency == "EUR":
            self.wait.until(ec.element_to_be_clickable((By.XPATH, self.currency_eur_xpath)))
            self.driver.find_element_by_xpath(self.currency_eur_xpath).click()
        elif currency == "pln":
            self.wait.until(ec.element_to_be_clickable((By.XPATH, self.currency_pln_xpath)))
            self.driver.find_element_by_xpath(self.currency_pln_xpath).click()

        self.driver.find_element_by_xpath(self.submit_buttons_xpath).click()

    @allure.step("Walidacja danych w wierszu")
    def validate_data(self, KS, KZ, loading_date, delivery_date, carrier, price):
        self.logger.info("Walidacja danych w wierszu")

        assert KS in self.driver.find_element_by_xpath(self.ks_xpath).text

        assert KZ in self.driver.find_element_by_xpath(self.kz_xpath).text

        assert loading_date == self.driver.find_element_by_xpath(self.loading_date_xpath).text

        assert delivery_date == self.driver.find_element_by_xpath(self.delivery_date_xpath).text

        assert carrier in self.driver.find_element_by_xpath(self.carrier_xpath).text

        assert price in self.driver.find_element_by_xpath(self.price_xpath).text

    @allure.step("Dodawanie notatki do wiersza")
    def add_note(self, text):
        self.logger.info("Dodawanie notatki do wiersza")
        self.driver.find_element_by_xpath(self.add_note_xpath).click()

        self.wait.until(ec.element_to_be_clickable((By.XPATH, self.note_area_xpath)))
        note_area = self.driver.find_element_by_xpath(self.note_area_xpath)
        note_area.click()
        note_area.send_keys(text)
        self.driver.find_element_by_xpath(self.save_note_xpath).click()

    @allure.step("Sprawdzenie dodania notatki")
    def check_note(self):
        try:
            self.driver.find_element_by_xpath("//tr[1]//a[contains(@class, 'btn-note-colored')]")
        except NoSuchElementException:
            return False, "Brak oznaczenia dodania notatki"

        return True, ""

    @allure.step("Przejscie do tworzenia awizacji z wiersza")
    def go_to_create_advice(self):
        self.logger.info("Przejscie do tworzenia awizacji z wiersza")
        self.driver.find_element_by_xpath(self.create_advice_xpath).click()

    @allure.step("Sprawdzenie widocznosci utworzonej aw w planerze")
    def check_visibility_advice(self, advice):
        self.logger.info("Sprawdzenie widocznosci utworzonej aw w planerze")
        try:
            self.driver.find_element_by_xpath("//td[@data-label='Nr AW']/a[contains(text(), '" + advice + "')]")
            return True
        except NoSuchElementException:
            return False

    @allure.step("Przejscie do nastepnej strony w planerze")
    def go_to_next_page(self):
        self.logger.info("Przejscie do nastepnej strony w planerze")
        self.driver.find_element_by_xpath(self.next_page_xpath).click()

    @allure.step("Przejscie do przekierowania awizacji z planera")
    def go_to_redirect_advice(self, advice):
        self.logger.info("Przejscie do przekierowanie awizacji z planera")
        redirect_xpath = "//a[contains(text(), '" + advice + "')]/../..//a[@title='Przekieruj awizację']"
        self.wait.until(ec.element_to_be_clickable((By.XPATH, redirect_xpath)))
        self.driver.find_element_by_xpath(redirect_xpath).click()

    @allure.step("Otwarcie filtrow")
    def open_filters(self):
        self.logger.info("Otwarcie filtrow")
        self.wait.until(ec.element_to_be_clickable((By.XPATH, self.open_filters_xpath)))
        self.driver.find_element_by_xpath(self.open_filters_xpath).click()

    @allure.step("Filtry: id")
    def filters_id(self, id_):
        self.logger.info("Filtry: id")
        self.wait.until(ec.element_to_be_clickable((By.XPATH, self.filters_row_id_xpath)))
        id_input = self.driver.find_element_by_xpath(self.filters_row_id_xpath)
        id_input.click()
        id_input.send_keys(id_)

    @allure.step("Filtry: produkt")
    def filters_product(self, product):
        self.logger.info("Filtry: produkt")
        self.wait.until(ec.element_to_be_clickable((By.XPATH, self.filters_product_xpath)))
        product_input = self.driver.find_element_by_xpath(self.filters_product_xpath)
        product_input.click()
        product_input.send_keys(product)
        product_option_xpath = "//li[contains(text(), '" + product + "')]"
        self.driver.find_element_by_xpath(product_option_xpath).click()

    @allure.step("Filtry: nazwa dostawcy")
    def filters_deliverer(self, deliverer):
        self.logger.info("Filtry: nazwa dostawcy")
        self.wait.until(ec.element_to_be_clickable((By.XPATH, self.filters_deliverer_xpath)))
        deliverer_input = self.driver.find_element_by_xpath(self.filters_deliverer_xpath)
        deliverer_input.click()
        deliverer_input.send_keys(deliverer)
        deliverer_option_xpath = "//li[text()='" + deliverer + "']"
        self.driver.find_element_by_xpath(deliverer_option_xpath).click()

    @allure.step("Filtry: adres odbioru")
    def filters_deliverer_address(self, deliverer_address):
        self.logger.info("Filtry: adres odbioru")
        self.wait.until(ec.element_to_be_clickable((By.XPATH, self.filters_deliverer_address_xpath)))
        address_input = self.driver.find_element_by_xpath(self.filters_deliverer_address_xpath)
        address_input.click()
        address_input.send_keys(deliverer_address)

    @allure.step("Filtry: data załadunku")
    def filters_loading_date(self, loading_date):
        self.logger.info("Filtry: data załadunku")
        self.wait.until(ec.element_to_be_clickable((By.XPATH, self.filters_loading_date_xpath)))
        loading_input = self.driver.find_element_by_xpath(self.filters_loading_date_xpath)
        loading_input.click()
        loading_input.send_keys(loading_date)

    @allure.step("Filtry: data dostawy")
    def filters_delivery_date(self, delivery_date):
        self.logger.info("Filtry: data dostawy")
        self.wait.until(ec.element_to_be_clickable((By.XPATH, self.filters_delivery_date_xpath)))
        delivery_input = self.driver.find_element_by_xpath(self.filters_delivery_date_xpath)
        delivery_input.click()
        delivery_input.send_keys(delivery_date)

    @allure.step("Filtry: nazwa odbiorcy")
    def filters_receiver(self, receiver):
        self.logger.info("Filtry: nazwa odbiorcy")
        self.wait.until(ec.element_to_be_clickable((By.XPATH, self.filters_receiver_xpath)))
        receiver_input = self.driver.find_element_by_xpath(self.filters_receiver_xpath)
        receiver_input.click()
        receiver_input.send_keys(receiver)
        receiver_option_xpath = "//li[contains(text(), '" + receiver + "')]"
        self.driver.find_element_by_xpath(receiver_option_xpath).click()

    @allure.step("Filtry: adres dostawy")
    def filters_receiver_address(self, receiver_address):
        self.logger.info("Filtry: adres dostawy")
        self.wait.until(ec.element_to_be_clickable((By.XPATH, self.filters_receiver_address_xpath)))
        address = self.driver.find_element_by_xpath(self.filters_receiver_address_xpath)
        address.click()
        address.send_keys(receiver_address)

    @allure.step("Filtry: przewoznik")
    def filters_carrier(self, carrier):
        self.logger.info("Filtry: przewoźnik")
        self.wait.until(ec.element_to_be_clickable((By.XPATH, self.filters_carrier_xpath)))
        carrier_input = self.driver.find_element_by_xpath(self.filters_carrier_xpath)
        carrier_input.click()
        carrier_input.send_keys(carrier)
        carrier_option_xpath = "//li[contains(text(), '" + carrier + "')]"
        self.driver.find_element_by_xpath(carrier_option_xpath).click()

    @allure.step("Filtry: stawka/t")
    def filters_price_per_t(self, price_from, price_to):
        self.logger.info("Filtry: stawka/t")
        self.wait.until(ec.element_to_be_clickable((By.XPATH, self.filters_price_per_t_from)))
        price_from_input = self.driver.find_element_by_xpath(self.filters_price_per_t_from)
        price_from_input.click()
        price_from_input.send_keys(price_from)

        price_to_input = self.driver.find_element_by_xpath(self.filters_price_per_t_to)
        price_to_input.click()
        price_to_input.send_keys(price_to)

    @allure.step("Filtry: stawka/t - waluta")
    def filters_price_per_t_currency(self, price_currency):
        self.logger.info("Filtry: stawka/t - waluta")
        self.wait.until(ec.element_to_be_clickable((By.XPATH, self.filters_price_per_t_currency_xpath)))
        self.driver.find_element_by_xpath(self.filters_price_per_t_currency_xpath).click()
        currency_option_xpath = "//li[contains(text(), '" + price_currency + "')]"
        self.driver.find_element_by_xpath(currency_option_xpath).click()

    @allure.step("Filtry: fracht")
    def filters_price(self, price_from, price_to):
        self.logger.info("Filtry: fracht")
        self.wait.until(ec.element_to_be_clickable((By.XPATH, self.filters_price_from_xpath)))
        price_from_input = self.driver.find_element_by_xpath(self.filters_price_from_xpath)
        price_from_input.click()
        price_from_input.send_keys(price_from)

        price_to_input = self.driver.find_element_by_xpath(self.filters_price_to_xpath)
        price_to_input.click()
        price_to_input.send_keys(price_to)

    @allure.step("Filtry: fracht - waluta")
    def filters_price_currency(self, price_currency):
        self.logger.info("Filtry: fracht - waluta")
        self.wait.until(ec.element_to_be_clickable((By.XPATH, self.filters_price_currency_xpath)))
        self.driver.find_element_by_xpath(self.filters_price_currency_xpath).click()
        currency_option_xpath = "//li[contains(text(), '" + price_currency + "')]"
        self.driver.find_element_by_xpath(currency_option_xpath).click()

    @allure.step("Filtry: nr pierwotny AW")
    def filters_original_advice_number(self, original_number):
        self.logger.info("Filtry: nr pierwotny AW")
        self.wait.until(ec.element_to_be_clickable((By.XPATH, self.filters_original_advice_xpath)))
        original_advice = self.driver.find_element_by_xpath(self.filters_original_advice_xpath)
        original_advice.click()
        original_advice.send_keys(original_number)

    @allure.step("Filtry: nr AW")
    def filters_advice_number(self, advice_number):
        self.logger.info("Filtry: nr AW")
        self.wait.until(ec.element_to_be_clickable((By.XPATH, self.filters_advice_xpath)))
        advice = self.driver.find_element_by_xpath(self.filters_advice_xpath)
        advice.click()
        advice.send_keys(advice_number)

    @allure.step("Filtry: KZ")
    def filters_kz(self, kz):
        self.logger.info("Filtry: KZ")
        self.wait.until(ec.element_to_be_clickable((By.XPATH, self.filters_kz_xpath)))
        kz_input = self.driver.find_element_by_xpath(self.filters_kz_xpath)
        kz_input.click()
        kz_input.send_keys(kz)
        kz_option_xpath = "//li[contains(text(), '" + kz + "')]"
        self.driver.find_element_by_xpath(kz_option_xpath).click()

    @allure.step("Filtry: KS")
    def filters_ks(self, ks):
        self.logger.info("Filtry: KS")
        self.wait.until(ec.element_to_be_clickable((By.XPATH, self.filters_ks_xpath)))
        ks_input = self.driver.find_element_by_xpath(self.filters_ks_xpath)
        ks_input.click()
        ks_input.send_keys(ks)
        ks_option_xpath = "//li[contains(text(), '" + ks + "')]"
        self.driver.find_element_by_xpath(ks_option_xpath).click()

    @allure.step("Filtry: status")
    def filters_status(self, status):
        self.logger.info("Filtry: status")
        self.wait.until(ec.element_to_be_clickable((By.XPATH, self.filters_status_xpath)))
        self.driver.find_element_by_xpath(self.filters_status_xpath).click()
        status_option_xpath = "//li[contains(text(), '" + status + "')]"
        self.driver.find_element_by_xpath(status_option_xpath).click()

    @allure.step("Filtry: osoba awizujaca")
    def filters_advice_person(self, person):
        self.logger.info("Filtry: osoba awizujaca")
        self.wait.until(ec.element_to_be_clickable((By.XPATH, self.filters_advicing_person)))
        person_input = self.driver.find_element_by_xpath(self.filters_advicing_person)
        person_input.click()
        person_input.send_keys(person)
        person_option_xpath = "//li[contains(text(), '" + person + "')]"
        self.driver.find_element_by_xpath(person_option_xpath).click()

    @allure.step("Filtry: ukryj dostarczone i anulowane")
    def filters_hide(self):
        self.logger.info("Filtry: ukryj dostarczone i anulowane")
        self.driver.find_element_by_xpath(self.filters_hide_xpath).click()

    @allure.step("Zastosowanie filtrow")
    def use_filters(self):
        self.logger.info("Zastosowanie filtrow")
        self.driver.find_element_by_xpath(self.use_filters_button_xpath).click()

    @allure.step("Usuwanie filtrow")
    def delete_filters(self):
        self.logger.info("Usuwanie filtrow")
        self.driver.find_element_by_xpath(self.delete_filters_xpath).click()
