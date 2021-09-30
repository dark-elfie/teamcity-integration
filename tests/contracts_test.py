import pytest
from selenium.webdriver.common.keys import Keys
from pages.contracts_page import ContractsPage
from pages.advices_page import AdvicePage
from pages.side_bar import SideBar
from utils.cleaning_functions import DeletingFunctions
from test_data.contracts_data import ContractsData
from test_data.advices_data import AWData2
import allure


@pytest.mark.usefixtures("setup")
@pytest.mark.usefixtures("log_in_admin")
class TestContracts:

    @allure.title("Polacz kontrakty")
    def test_connect_contracts(self):
        side_bar = SideBar(self.driver)
        side_bar.get_in_contracts()
        contracts_page = ContractsPage(self.driver)
        contracts_page.set_sales_contract(ContractsData.sales_number)
        contracts_page.set_purchase_contract(ContractsData.purchase_number)
        contracts_page.connect_contracts()
        purchase_option_xpath = "//li/p/span[contains(text(), '" + ContractsData.purchase_number + "')]"
        assert len(self.driver.find_elements_by_xpath(purchase_option_xpath)) == 1

    @allure.title("Tworzenie awizacji do polaczonych kontraktow")
    def test_create_advice(self):
        side_bar = SideBar(self.driver)
        side_bar.get_in_contracts()
        contracts_page = ContractsPage(self.driver)
        contracts_page.set_sales_contract(ContractsData.sales_number)
        contracts_page.create_advice(ContractsData.purchase_number)
        advice_page = AdvicePage(self.driver)
        advice_page.go_to_carriage()
        advice_page.add_carrier()
        advice_page.add_carriage_data_schedule(AWData2.loading_date, AWData2.delivery_date, AWData2.vehicle_number,
                                               AWData2.driver_name, AWData2.driver_last_name, AWData2.id_type,
                                               AWData2.id_number, AWData2.driver_phone, AWData2.price_per_tone,
                                               AWData2.schedule)
        advice_page.go_to_summary()
        advice_page.validate_data_schedule(ContractsData.sales_number, ContractsData.purchase_number,
                                           AWData2.loading_date, AWData2.delivery_date, AWData2.vehicle_number,
                                           AWData2.driver_name, AWData2.driver_last_name, AWData2.id_type,
                                           AWData2.id_number, AWData2.driver_phone, AWData2.price_per_tone,
                                           AWData2.schedule)
        advice_page.save()
        assert self.driver.title == "Szczegóły awizacji | Agrii TMS" or self.driver.title == "Awizacje | Agrii TMS"

    @allure.title("Widocznosc polaczonych kontraktow")
    def test_visibility(self):
        # sprawdzanie widoczności w kontrakcie sprzedaży
        side_bar = SideBar(self.driver)
        side_bar.get_in_advices()
        contracts_page = ContractsPage(self.driver)
        ks_xpath = "//a[contains(text(), '" + ContractsData.purchase_number + "')]/../..//a[contains(text(), '" + \
                   ContractsData.sales_number + "')]"
        self.driver.find_element_by_xpath(ks_xpath).click()
        kz_visibility = contracts_page.visibility_in_sales(ContractsData.purchase_number)
        assert kz_visibility

        # sprawdzanie widoczności w kontrakcie zakupu
        self.driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
        side_bar.get_in_advices()
        kz_xpath = "//a[contains(text(), '" + ContractsData.sales_number + "')]/../..//a[contains(text(), '" + \
                   ContractsData.purchase_number + "')]"
        self.driver.find_element_by_xpath(kz_xpath).click()
        ks_visibility = contracts_page.visibility_in_purchase(ContractsData.sales_number)
        assert ks_visibility

    @allure.title("Usuwam utworzona awizacje")
    def test_delete_advice(self):
        DeletingFunctions.delete_aw(self.driver, ContractsData.sales_number, ContractsData.purchase_number)

    @allure.title("Rozlacz kontrakty")
    def test_disconnect(self):
        side_bar = SideBar(self.driver)
        side_bar.get_in_contracts()
        contracts_page = ContractsPage(self.driver)
        contracts_page.set_sales_contract(ContractsData.sales_number)
        contracts_page.disconnect_contracts(ContractsData.purchase_number)
        purchase_option_xpath = "//li/p/span[contains(text(), '" + ContractsData.purchase_number + "')]"
        assert len(self.driver.find_elements_by_xpath(purchase_option_xpath)) == 0
