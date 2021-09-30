import time

from pages.advices_page import AdvicePage
from pages.contracts_page import ContractsPage
from pages.payoffs_page import PayoffsPage
from pages.side_bar import SideBar


class CreatingFunctions:

    @staticmethod
    def create_aw(driver, receiver, receiver_contact, receiver_address, deliverer, deliverer_contact, deliverer_address,
                  loading_date, loading_time_from, loading_time_to, delivery_date, delivery_time_from, delivery_time_to,
                  vehicle_number, driver_name, driver_last_name, id_type, id_number, driver_phone, price_per_tone):
        side_bar = SideBar(driver)
        side_bar.get_in_advices()
        advice_page = AdvicePage(driver)
        advice_page.add_new()
        advice_page.add_receiver(receiver, receiver_contact, receiver_address)
        advice_page.add_deliverer(deliverer, deliverer_contact, deliverer_address)
        advice_page.go_to_carriage()
        advice_page.add_carrier()
        advice_page.add_carriage_data(loading_date, loading_time_from, loading_time_to, delivery_date,
                                      delivery_time_from, delivery_time_to, vehicle_number, driver_name,
                                      driver_last_name, id_type, id_number, driver_phone, price_per_tone)
        advice_page.go_to_summary()
        advice_page.validate_data(receiver, deliverer, loading_date, loading_time_from, loading_time_to,
                                  delivery_date, delivery_time_from, delivery_time_to, vehicle_number, driver_name,
                                  driver_last_name, id_type, id_number, driver_phone, price_per_tone)
        advice_page.save()


class DeletingFunctions:

    @staticmethod
    def delete_aw(driver, receiver, deliverer):
        side_bar = SideBar(driver)
        side_bar.get_in_advices()
        advice_page = AdvicePage(driver)
        advice_page.delete(receiver, deliverer)
        advice_page.confirm_delete()

    @staticmethod
    def delete_aw_number(driver, advice_number):
        advice_page = AdvicePage(driver)
        advice_page.delete_number(advice_number)
        advice_page.confirm_delete()

    @staticmethod
    def delete_connection(driver, sales_number, purchase_number):
        side_bar = SideBar(driver)
        side_bar.get_in_contracts()
        contracts_page = ContractsPage(driver)
        time.sleep(1)
        contracts_page.set_sales_contract(sales_number)
        contracts_page.disconnect_contracts(purchase_number)
        purchase_option_xpath = "//li/p/span[contains(text(), '" + purchase_number + "')]"

    @staticmethod
    def delete_payoff(driver, payoff_name, payoff_receiver):
        side_bar = SideBar(driver)
        side_bar.get_in_payoffs_import_list()
        payoffs_page = PayoffsPage(driver)
        payoffs_page.delete_import(payoff_name, payoff_receiver)
        payoffs_page.confirm_delete()
        assert driver.find_element_by_xpath("//div[text()='Pomyślnie usunięto.']")
