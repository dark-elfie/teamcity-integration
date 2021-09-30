import time
import pytest
from selenium.webdriver.common.keys import Keys

from pages.advices_page import AdvicePage
from pages.side_bar import SideBar
from pages.payoffs_page import PayoffsPage
from test_data.payoffs_data import PayoffsData
from utils.cleaning_functions import DeletingFunctions
import allure


@pytest.mark.usefixtures("setup")
@pytest.mark.usefixtures("log_in_admin")
class TestPayoffs:

    """ Szablony rozliczeń """
    @allure.title("Dodawanie nowego szablonu rozliczen")
    def test_add_payoff_template(self):
        side_bar = SideBar(self.driver)
        side_bar.get_in_payoffs_templates()
        payoffs_page = PayoffsPage(self.driver)
        payoffs_page.create_template()
        payoffs_page.set_template_data(PayoffsData.receiver, PayoffsData.template_name, PayoffsData.template_file)
        payoffs_page.save_template()
        assert self.driver.title == "Szablony rozliczeń | Agrii TMS"

    @allure.title("Edycja szablonu rozliczen")
    def test_edit_payoff_template(self):
        side_bar = SideBar(self.driver)
        side_bar.get_in_payoffs_templates()
        payoffs_page = PayoffsPage(self.driver)
        payoffs_page.edit_template(PayoffsData.template_name, PayoffsData.receiver)
        payoffs_page.edit_template_name(PayoffsData.template_name_change)
        payoffs_page.save_template()
        assert self.driver.title == "Szablony rozliczeń | Agrii TMS"

    @allure.title("Usuwanie szablonu rozliczen")
    def test_delete_payoff_template(self):
        side_bar = SideBar(self.driver)
        side_bar.get_in_payoffs_templates()
        payoffs_page = PayoffsPage(self.driver)
        payoffs_page.delete_template(PayoffsData.template_name_change, PayoffsData.receiver)
        payoffs_page.confirm_delete()
        assert self.driver.find_element_by_xpath("//div[text()='Pomyślnie usunięto.']")

    @allure.title("Weryfikacja danych w szablonie")
    def test_validate_payoff_template(self):
        side_bar = SideBar(self.driver)
        side_bar.get_in_payoffs_templates()
        payoffs_page = PayoffsPage(self.driver)
        payoffs_page.create_template()


    """ importowanie i łączenie rozliczeń """

    @allure.title("Importowanie pliku z rozliczeniami")
    def test_import_payoff_file(self):
        side_bar = SideBar(self.driver)
        side_bar.get_in_payoffs_import()
        payoffs_page = PayoffsPage(self.driver)
        payoffs_page.set_receiver_import(PayoffsData.payoff_receiver)
        payoffs_page.set_template_import(PayoffsData.payoff_name)
        payoffs_page.upload_payoff(PayoffsData.payoff_file)
        assert len(self.driver.find_elements_by_xpath("//table[@id='billing-table']/tbody/tr")) == 2

    @allure.title("Automatyczne laczenie pliku z rozliczeniami")
    def test_automatic_connect_payoff_file(self):
        side_bar = SideBar(self.driver)
        side_bar.get_in_payoffs_import()
        payoffs_page = PayoffsPage(self.driver)
        payoffs_page.set_receiver_import(PayoffsData.payoff_receiver)
        payoffs_page.set_template_import(PayoffsData.payoff_name)
        payoffs_page.upload_payoff(PayoffsData.payoff_file)
        payoffs_page.go_to_connecting_positions()
        result, msg = payoffs_page.check_connections(2, PayoffsData.connections_dict)
        assert result, msg

    @allure.title("Zmiana statusu w trakcie rozliczenia")
    def test_status_payoff(self):
        side_bar = SideBar(self.driver)
        side_bar.get_in_advices()
        advice_page = AdvicePage(self.driver)
        advice_page.get_into_aw_number("AW/004462")
        time.sleep(1)
        assert self.driver.find_element_by_xpath("//a[@data-title='Wybierz status']").text == "W rozliczeniu"
        side_bar.get_in_advices()
        advice_page.delete_filters()

    @allure.title("Usuwanie importu")
    def test_delete_payoff_file(self):
        side_bar = SideBar(self.driver)
        side_bar.get_in_advices()
        advice_page = AdvicePage(self.driver)
        advice_page.delete_filters()
        side_bar.get_in_payoffs_import_list()
        payoffs_page = PayoffsPage(self.driver)
        payoffs_page.delete_import(PayoffsData.payoff_name, PayoffsData.payoff_receiver)
        payoffs_page.confirm_delete()
        assert self.driver.find_element_by_xpath("//div[text()='Pomyślnie usunięto.']")

    @allure.title("Usuwanie pozycji z importu")
    def test_delete_payoff_line(self):
        side_bar = SideBar(self.driver)
        side_bar.get_in_payoffs_import()
        payoffs_page = PayoffsPage(self.driver)
        payoffs_page.set_receiver_import(PayoffsData.payoff_receiver)
        payoffs_page.set_template_import(PayoffsData.payoff_name)
        payoffs_page.upload_payoff(PayoffsData.payoff_file_2)
        payoffs_page.delete_import_line(str(3))
        assert len(self.driver.find_elements_by_xpath("//table[@id='billing-table']/tbody/tr")) == 2
        payoffs_page.go_to_connecting_positions()
        assert len(self.driver.find_elements_by_xpath("//div[@class='m-entry --settlement']")) == 2

    @allure.title("Zapisanie laczenia pliku z rozliczeniami")
    @pytest.mark.not_reusable
    def test_connect_payoff_file(self):
        side_bar = SideBar(self.driver)
        side_bar.get_in_payoffs_import()
        payoffs_page = PayoffsPage(self.driver)
        payoffs_page.set_receiver_import(PayoffsData.payoff_receiver)
        payoffs_page.set_template_import(PayoffsData.payoff_name)
        payoffs_page.upload_payoff(PayoffsData.payoff_file)
        payoffs_page.go_to_connecting_positions()
        result, msg = payoffs_page.check_connections(2, PayoffsData.connections_dict)
        assert result, msg
        payoffs_page.save_connections()
        assert "Podgląd rozliczenia" in self.driver.title

    @allure.title("Zmiana statusu po zapisaniu rozliczenia")
    @pytest.mark.not_reusable
    def test_status_save_payoff(self):
        side_bar = SideBar(self.driver)
        side_bar.get_in_advices()
        advice_page = AdvicePage(self.driver)
        advice_page.get_into_aw_number("AW/004462")
        time.sleep(1)
        assert self.driver.find_element_by_xpath("//a[@data-title='Wybierz status']").text == "Dostarczona"
        side_bar.get_in_advices()
        self.driver.find_element_by_xpath("//input[@id='fullsearch-delegate']").clear()
        self.driver.find_element_by_xpath("//input[@id='fullsearch-delegate']").send_keys(Keys.ENTER)

    @allure.title("Importowanie po Lp")
    def test_import_payoff_file_lp(self):
        side_bar = SideBar(self.driver)
        side_bar.get_in_payoffs_import()
        payoffs_page = PayoffsPage(self.driver)
        payoffs_page.set_receiver_import(PayoffsData.payoff_receiver)
        payoffs_page.set_template_import(PayoffsData.payoff_name)
        payoffs_page.upload_payoff(PayoffsData.payoff_file_2)
        assert len(self.driver.find_elements_by_xpath("//table[@id='billing-table']/tbody/tr")) == 1
        DeletingFunctions.delete_payoff(self.driver, PayoffsData.payoff_name, PayoffsData.payoff_receiver)

    @allure.title("Porownywanie rozbieznosci")
    def test_comparing_differences(self):
        side_bar = SideBar(self.driver)
        side_bar.get_in_payoffs_import()
        payoffs_page = PayoffsPage(self.driver)
        payoffs_page.set_receiver_import(PayoffsData.payoff_diff_receiver)
        payoffs_page.set_template_import(PayoffsData.payoff_diff_name)
        payoffs_page.upload_payoff(PayoffsData.payoff_diff_file)
        payoffs_page.go_to_connecting_positions()
        assert self.driver.find_element_by_xpath("//a[contains(@class, 'disabled')]")
        payoffs_page.compare_differences()
        assert len(self.driver.find_elements_by_xpath("//div[contains(@class, '--ready')]")) == 3
        DeletingFunctions.delete_payoff(self.driver, PayoffsData.payoff_diff_name, PayoffsData.payoff_diff_receiver)
