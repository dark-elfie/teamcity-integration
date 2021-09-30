import time
import pytest
from selenium.webdriver.common.keys import Keys
from pages.contracts_page import ContractsPage
from pages.advices_page import AdvicePage
from pages.schedules_page import SchedulePage
from pages.side_bar import SideBar
from utils.cleaning_functions import DeletingFunctions
from test_data.contracts_data import ContractsData
from test_data.advices_data import AWData2
from test_data.schedules_data import ScheduleData
import allure


@pytest.mark.usefixtures("setup")
@pytest.mark.usefixtures("log_in_admin")
class TestSchedules:

    @allure.title("Tworzenie grafiku")
    def test_add_schedule(self):
        side_bar = SideBar(self.driver)
        side_bar.get_in_sales_contracts()
        contracts_page = ContractsPage(self.driver)
        contracts_page.get_into_sales_contract(ScheduleData.KS)
        contracts_page.open_schedules()
        contracts_page.add_new_schedule(False, ScheduleData.date_from, ScheduleData.date_to, ScheduleData.grain_trader)
        time.sleep(2)
        contracts_page.validate_schedule(ScheduleData.date_from, ScheduleData.date_to, ScheduleData.grain_trader)
        # asserty w validate_schedule

    @allure.title("Edycja grafiku z KS")
    def test_edit_schedule(self):
        side_bar = SideBar(self.driver)
        side_bar.get_in_sales_contracts()
        contracts_page = ContractsPage(self.driver)
        contracts_page.get_into_sales_contract(ScheduleData.KS)
        contracts_page.open_schedules()
        contracts_page.get_in_schedule(ScheduleData.date_from, ScheduleData.date_to, ScheduleData.grain_trader)
        time.sleep(2)
        contracts_page.edit_schedule(ScheduleData.edit_date_from, ScheduleData.edit_date_to,
                                     ScheduleData.edit_grain_trader)
        time.sleep(2)
        contracts_page.validate_schedule(ScheduleData.edit_date_from, ScheduleData.edit_date_to,
                                         ScheduleData.edit_grain_trader)

    @allure.title("Edycja grafiku z listy")
    def test_edit_schedule_from_list(self):
        side_bar = SideBar(self.driver)
        side_bar.get_in_schedules()
        time.sleep(2)
        schedule_page = SchedulePage(self.driver)
        schedule_page.get_in_edit_schedule(ScheduleData.KS, ScheduleData.edit_date_from, ScheduleData.edit_grain_trader)
        time.sleep(2)
        schedule_page.edit_schedule(ScheduleData.edit_list_date_from, ScheduleData.edit_list_date_to,
                                    ScheduleData.edit_list_grain_trader, ScheduleData.edit_list_is_scheduleless,
                                    ScheduleData.edit_list_tonnage, ScheduleData.edit_list_pin)
        time.sleep(5)
        schedule_page.save_schedule()
        schedule_page.validate_schedule_list(ScheduleData.KS, ScheduleData.edit_list_date_from,
                                             ScheduleData.edit_list_grain_trader)

    @allure.title("Widocznosc grafiku na liscie")
    def test_schedule_visibility(self):
        side_bar = SideBar(self.driver)
        side_bar.get_in_schedules()
        schedule_page = SchedulePage(self.driver)
        out, msg = schedule_page.check_visibility(ScheduleData.KS, ScheduleData.edit_list_date_from,
                                                  ScheduleData.edit_list_grain_trader)
        assert out, msg

    @allure.title("Usuwanie grafiku z KS")
    def test_delete_schedule_from_sales(self):
        side_bar = SideBar(self.driver)
        side_bar.get_in_sales_contracts()
        contracts_page = ContractsPage(self.driver)
        contracts_page.get_into_sales_contract(ScheduleData.KS)
        contracts_page.open_schedules()
        contracts_page.delete_schedule_KS(ScheduleData.edit_list_date_from, ScheduleData.edit_list_date_to,
                                          ScheduleData.edit_list_grain_trader)
        contracts_page.confirm_delete_schedule()
        assert self.driver.find_element_by_xpath("//div[text()='Pomyślnie usunięto.']")

    @allure.title("Tworzenie wielu grafikow")
    def test_add_many_schedules(self):
        side_bar = SideBar(self.driver)
        side_bar.get_in_sales_contracts()
        contracts_page = ContractsPage(self.driver)
        contracts_page.get_into_sales_contract(ScheduleData.KS)
        contracts_page.open_schedules()
        contracts_page.add_many_schedules(ScheduleData.many_non_schedule, ScheduleData.many_date_from,
                                          ScheduleData.many_date_to, ScheduleData.many_grain_trader,
                                          len(ScheduleData.many_non_schedule))
        time.sleep(2)
        contracts_page.validate_many_schedules(ScheduleData.many_non_schedule, ScheduleData.many_date_from,
                                               ScheduleData.many_date_to, ScheduleData.many_grain_trader,
                                               len(ScheduleData.many_non_schedule))
        # asserty w validate_many_schedules

    @allure.title("Usuwanie grafiku z listy")
    def test_delete_schedule_from_list(self):
        side_bar = SideBar(self.driver)
        side_bar.get_in_schedules()
        schedule_page = SchedulePage(self.driver)
        for i in range(len(ScheduleData.many_non_schedule)):
            schedule_page.delete_schedule(ScheduleData.KS, ScheduleData.many_date_from[i],
                                          ScheduleData.many_grain_trader[i])
            schedule_page.confirm_delete()
            assert self.driver.find_element_by_xpath("//div[text()='Pomyślnie usunięto.']")
            time.sleep(1)

    @allure.title("Stosowanie filtrów")
    def test_use_filters(self):
        side_bar = SideBar(self.driver)
        side_bar.get_in_schedules()
        schedule_page = SchedulePage(self.driver)
        schedule_page.open_filters_schedules()
        schedule_page.filters_grain_trader("MIKOŁAJ KUBSIK")
        schedule_page.filters_receiver("grygier")
        schedule_page.filters_address("Wonieść")
        schedule_page.filters_ks_number("KS/004511")
        schedule_page.filters_product("KUKUR 3305")
        schedule_page.filters_schedule_date("2021-08-04 - 2021-08-10")
        schedule_page.filters_advice_status("Dostarczona")
        schedule_page.filters_delivery_date("2021-08-12 - 2021-08-12")
        schedule_page.filters_planned_grain_trader("Adam Grzelec")
        schedule_page.use_filters()
        time.sleep(1)
        schedule_page.delete_filters()
        assert False
