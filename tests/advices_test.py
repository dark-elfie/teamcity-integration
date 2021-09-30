import os
import time
import pytest
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from utils.cleaning_functions import DeletingFunctions, CreatingFunctions
from pages.advices_page import AdvicePage
from pages.side_bar import SideBar
from test_data.advices_data import AWData, AWData2
from test_data.contracts_data import ContractsData
import allure


@pytest.mark.usefixtures("setup")
@pytest.mark.usefixtures("log_in_admin")
class TestAdvices:

    @allure.title("Stworz nowa awizacje")
    @pytest.mark.singleAw
    def test_add(self):
        side_bar = SideBar(self.driver)
        side_bar.get_in_advices()
        advice_page = AdvicePage(self.driver)
        advice_page.add_new()
        advice_page.add_receiver(AWData.receiver, AWData.receiver_contact, AWData.receiver_address)
        advice_page.add_deliverer(AWData.deliverer, AWData.deliverer_contact, AWData.deliverer_address)
        advice_page.go_to_carriage()
        advice_page.add_carrier()
        advice_page.add_carriage_data(AWData.loading_date, AWData.loading_time_from, AWData.loading_time_to,
                                      AWData.delivery_date, AWData.delivery_time_from, AWData.delivery_time_to,
                                      AWData.vehicle_number, AWData.driver_name, AWData.driver_last_name,
                                      AWData.id_type, AWData.id_number, AWData.driver_phone, AWData.price_per_tone)
        advice_page.go_to_summary()
        advice_page.validate_data(AWData.receiver, AWData.deliverer, AWData.loading_date, AWData.loading_time_from,
                                  AWData.loading_time_to, AWData.delivery_date, AWData.delivery_time_from,
                                  AWData.delivery_time_to, AWData.vehicle_number, AWData.driver_name,
                                  AWData.driver_last_name, AWData.id_type, AWData.id_number, AWData.driver_phone,
                                  AWData.price_per_tone)
        advice_page.save()
        time.sleep(1)
        assert self.driver.title == "Szczegóły awizacji | Agrii TMS" or self.driver.title == "Awizacje | Agrii TMS"

    @allure.title("Edytuj awizacje")
    @allure.description("Test obejmuje zmianę adresu dostawy oraz stawki transportowej")
    def test_edit(self):
        side_bar = SideBar(self.driver)
        side_bar.get_in_advices()
        advice_page = AdvicePage(self.driver)
        advice_page.edit_first()
        advice_page.edit_receiver_address()
        advice_page.go_to_carriage()
        advice_page.edit_carrier_price_per_ton(125)
        advice_page.go_to_summary()
        advice_page.save_edited()
        assert self.driver.title == "Szczegóły awizacji | Agrii TMS" or self.driver.title == "Awizacje | Agrii TMS"

    @allure.title("Edytuj awizacje (szczegoly aw)")
    @allure.description("Test obejmuje zmianę adresu dostawy oraz stawki transportowej, wejście do ekranu edycji "
                        "z widoku szczegółów awizacji")
    def test_edit_from_aw(self):
        side_bar = SideBar(self.driver)
        side_bar.get_in_advices()
        advice_page = AdvicePage(self.driver)
        advice_page.get_into_aw()
        advice_page.edit_opened_aw()
        advice_page.edit_receiver_address()
        advice_page.go_to_carriage()
        advice_page.edit_carrier_price_per_ton(500)
        advice_page.go_to_summary()
        advice_page.save_edited()
        assert self.driver.title == "Szczegóły awizacji | Agrii TMS"

    @allure.title("Zmiana statusu awizacji")
    def test_change_status(self):
        side_bar = SideBar(self.driver)
        side_bar.get_in_advices()
        advice_page = AdvicePage(self.driver)
        advice_page.get_into_aw()
        advice_page.change_advice_status("Zweryfikowana")
        time.sleep(1)
        assert self.driver.find_element_by_xpath("//a[@data-title='Wybierz status']").text == "Zweryfikowana"
        advice_page.change_advice_status("Nowa")

    @allure.title("Usun awizacje")
    @pytest.mark.singleAw
    def test_delete(self):
        side_bar = SideBar(self.driver)
        side_bar.get_in_advices()
        advice_page = AdvicePage(self.driver)
        advice_page.delete(AWData.receiver_short, AWData.deliverer_short)
        advice_page.confirm_delete()
        assert self.driver.find_element_by_xpath("//div[text()='Pomyślnie usunięto.']").is_displayed()

    @allure.title("Stworz nowa awizacje (z grafikiem)")
    def test_add_aw_schedule(self):
        side_bar = SideBar(self.driver)
        side_bar.get_in_advices()
        advice_page = AdvicePage(self.driver)
        advice_page.add_new()
        advice_page.add_receiver_without_contact_address(AWData2.receiver)
        advice_page.add_deliverer_without_contact_address(AWData2.deliverer)
        advice_page.go_to_carriage()
        advice_page.add_carrier()
        advice_page.add_carriage_data_schedule(AWData2.loading_date, AWData2.delivery_date, AWData2.vehicle_number,
                                               AWData2.driver_name, AWData2.driver_last_name, AWData2.id_type,
                                               AWData2.id_number, AWData2.driver_phone, AWData2.price_per_tone,
                                               AWData2.schedule)
        advice_page.go_to_summary()
        advice_page.validate_data_schedule(AWData2.receiver, AWData2.deliverer, AWData2.loading_date,
                                           AWData2.delivery_date, AWData2.vehicle_number, AWData2.driver_name,
                                           AWData2.driver_last_name, AWData2.id_type, AWData2.id_number,
                                           AWData2.driver_phone, AWData2.price_per_tone, AWData2.schedule)
        advice_page.save()
        assert self.driver.title == "Szczegóły awizacji | Agrii TMS" or self.driver.title == "Awizacje | Agrii TMS"

    @allure.title("Klonowanie awizacji")
    def test_clone_aw(self):
        side_bar = SideBar(self.driver)
        side_bar.get_in_advices()
        advice_page = AdvicePage(self.driver)
        advice_page.clone_aw(AWData2.receiver, AWData2.deliverer)
        advice_page.go_to_carriage()
        advice_page.add_carriage_data_clone(AWData2.delivery_date, AWData2.schedule)
        advice_page.go_to_summary()
        advice_page.save()
        assert self.driver.title == "Szczegóły awizacji | Agrii TMS" or self.driver.title == "Awizacje | Agrii TMS"

    @allure.title("Eksportowanie listy awizacji (xlsx)")
    def test_export_aw_xlsx(self):
        side_bar = SideBar(self.driver)
        side_bar.get_in_advices()
        advice_page = AdvicePage(self.driver)
        advice_page.export_xlsx()
        seconds = 0
        dl_wait = True
        now = datetime.now()
        dt = now.strftime("%Y-%m-%d %H_%M")
        while dl_wait and seconds < 10:
            time.sleep(1)
            dl_wait = True
            for fname in os.listdir("C:\\Users\\Sara\\Downloads"):
                if ("Awizacje-" + dt) in fname:
                    if fname.endswith('.xlsx'):
                        dl_wait = False
            seconds += 1
        if seconds < 10:
            assert True
        else:
            assert False, "Błąd pobierania pliku"

    @allure.title("Eksportowanie listy awizacji (csv)")
    def test_export_aw_cvs(self):
        side_bar = SideBar(self.driver)
        side_bar.get_in_advices()
        advice_page = AdvicePage(self.driver)
        advice_page.export_csv()
        seconds = 0
        dl_wait = True
        now = datetime.now()
        dt = now.strftime("%Y-%m-%d %H_%M")
        while dl_wait and seconds < 10:
            time.sleep(1)
            dl_wait = True
            for fname in os.listdir("C:\\Users\\Sara\\Downloads"):
                if ("Awizacje-" + dt) in fname:
                    if fname.endswith('.csv'):
                        dl_wait = False
            seconds += 1
        if seconds < 10:
            assert True
        else:
            assert False, "Błąd pobierania pliku"

    @allure.title("Filtrowanie listy awizacji")
    def test_filters(self):
        side_bar = SideBar(self.driver)
        side_bar.get_in_advices()
        advice_page = AdvicePage(self.driver)
        advice_page.open_filters()
        advice_page.set_filter_driver_name("Jan")
        advice_page.set_filter_advice_status("Dostarczona")
        advice_page.use_filters()
        side_bar.get_in_advices()
        advice_page.delete_filters()
        # assert
        '''walidacja wyników (nie da się sprawdzić wszystkich bezpośrednio)'''

    @allure.title("*Sprzatanie utworzonych awizacji*")
    def test_clean_aw(self):
        DeletingFunctions.delete_aw(self.driver, AWData2.receiver, AWData2.deliverer)
        self.driver.find_element_by_xpath("//li[@class='active']//span[text()='Kokpit']").click()
        DeletingFunctions.delete_aw(self.driver, AWData2.receiver, AWData2.deliverer)
        DeletingFunctions.delete_connection(self.driver, ContractsData.sales_number, ContractsData.purchase_number)

    @allure.title("Przekierowanie awizacji")
    def test_redirect_advice(self):
        CreatingFunctions.create_aw(self.driver, AWData.receiver, AWData.receiver_contact, AWData.receiver_address,
                                    AWData.deliverer, AWData.deliverer_contact, AWData.deliverer_address,
                                    AWData.loading_date, AWData.loading_time_from, AWData.loading_time_to,
                                    AWData.delivery_date, AWData.delivery_time_from, AWData.delivery_time_to,
                                    AWData.vehicle_number, AWData.driver_name, AWData.driver_last_name, AWData.id_type,
                                    AWData.id_number, AWData.driver_phone, AWData.price_per_tone)
        advice_page = AdvicePage(self.driver)
        time.sleep(0.5)
        if self.driver.title == "Awizacje | Agrii TMS":
            advice_page.get_into_aw()
        first_advice = advice_page.get_advice_number()

        side_bar = SideBar(self.driver)
        advice_page.go_to_redirect_advice()
        advice_page.redirect_advice("Anulowana")
        advice_page.redirect_add_note("Transakcja anulowana")
        advice_page.go_to_new_advice()
        advice_page.go_to_carriage()
        time.sleep(1.5)
        advice_page.go_to_summary()
        advice_page.save()
        self.driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
        time.sleep(2.5)
        side_bar.open_side_bar()
        side_bar.get_in_advices()
        advice_page.get_into_aw()
        second_advice = advice_page.get_advice_number()

        side_bar.get_in_advices()
        first_status = advice_page.get_advice_status_from_list(first_advice)
        assert first_status == "Anulowana"
        second_status = advice_page.get_advice_status_from_list(second_advice)
        assert second_status == "Nowa"

        DeletingFunctions.delete_aw_number(self.driver, second_advice)

    @allure.title("Zmiana statusu awizacji po przekierowaniu")
    def test_status_redirect(self):
        side_bar = SideBar(self.driver)
        side_bar.get_in_advices()
        advice_page = AdvicePage(self.driver)
        advice_page.get_into_aw()
        time.sleep(1)
        assert self.driver.find_element_by_xpath("//a[@data-title='Wybierz status']").text == "Anulowana"
        advice_page.change_advice_status("Nowa")
        first_advice = advice_page.get_advice_number()
        side_bar.get_in_advices()
        DeletingFunctions.delete_aw_number(self.driver, first_advice)
