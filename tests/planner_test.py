import time
import pytest
from selenium.webdriver.common.keys import Keys
from pages.side_bar import SideBar
from pages.planner_page import PlannerPage
from pages.advices_page import AdvicePage
from test_data.planner_data import PlannerData
from test_data.advices_data import AWData
from utils.cleaning_functions import DeletingFunctions, CreatingFunctions
import allure


@pytest.mark.usefixtures("setup")
@pytest.mark.usefixtures("log_in_admin")
class TestPlanner:

    @allure.title("Dodawanie nowego wiersza w planerze")
    def test_add_new_line(self):
        side_bar = SideBar(self.driver)
        side_bar.get_in_planner()
        planner_page = PlannerPage(self.driver)
        if self.driver.find_element_by_xpath("//li[contains(@class, 'page-item active')]/a").text != "1":
            self.driver.find_element_by_xpath("//li[contains(@class, 'page-item')]/a[text()='1']").click()
        planner_page.add_new_line()
        planner_page.set_ks(PlannerData.KS)
        planner_page.set_kz(PlannerData.KZ)
        planner_page.set_loading_date(PlannerData.loading_date)
        planner_page.set_delivery_date(PlannerData.delivery_date)
        planner_page.set_carrier(PlannerData.carrier)
        planner_page.set_price(PlannerData.price)
        planner_page.set_currency(PlannerData.currency)
        planner_page.validate_data(PlannerData.KS, PlannerData.KZ, PlannerData.loading_date, PlannerData.delivery_date,
                                   PlannerData.carrier, PlannerData.price)
        # asercje w funkcji validate_data()

    @allure.title("Dodawanie notatki do wiersza")
    def test_add_note(self):
        side_bar = SideBar(self.driver)
        side_bar.get_in_planner()
        planner_page = PlannerPage(self.driver)
        planner_page.add_note(PlannerData.note)
        out, msg = planner_page.check_note()
        assert out, msg

    @allure.title("Dodawanie nowych awizacji z poziomu planera")
    def test_add_advice_planner(self):
        side_bar = SideBar(self.driver)
        side_bar.get_in_planner()
        planner_page = PlannerPage(self.driver)
        planner_page.go_to_create_advice()
        advice_page = AdvicePage(self.driver)
        advice_page.go_to_carriage()
        advice_page.add_carrier()
        advice_page.add_carriage_data_planner(AWData.vehicle_number, AWData.driver_name, AWData.driver_last_name,
                                              AWData.id_type, AWData.id_number, AWData.driver_phone,
                                              PlannerData.schedule)
        advice_page.go_to_summary()
        advice_page.validate_data(PlannerData.KS, PlannerData.KZ, PlannerData.loading_date, "00:00", "00:00",
                                  PlannerData.delivery_date, "00:00", "00:00", AWData.vehicle_number,
                                  AWData.driver_name, AWData.driver_last_name, AWData.id_type, AWData.id_number,
                                  AWData.driver_phone, int(PlannerData.price))
        advice_page.save()
        assert self.driver.title == "Planer | Agrii TMS"
        side_bar.open_side_bar()
        self.driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
        DeletingFunctions.delete_aw(self.driver, PlannerData.KS, PlannerData.KZ)

    @allure.title("Wyswielanie w planerze awizacji (spoza planera)")
    def test_advices_visibility(self):
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
        advice = advice_page.get_advice_number()
        side_bar = SideBar(self.driver)
        self.driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
        time.sleep(0.5)
        side_bar.get_in_planner()
        planner_page = PlannerPage(self.driver)
        if self.driver.find_element_by_xpath("//li[contains(@class, 'page-item active')]/a").text != "1":
            self.driver.find_element_by_xpath("//li[contains(@class, 'page-item')]/a[text()='1']").click()
        out = planner_page.check_visibility_advice(advice)
        if not out:
            planner_page.go_to_next_page()
            out = planner_page.check_visibility_advice(advice)

        assert out
        side_bar.open_side_bar()
        self.driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
        DeletingFunctions.delete_aw(self.driver, AWData.receiver_short, AWData.deliverer_short)

    @allure.title("Przekierowanie awizacji z planera")
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
        self.driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
        time.sleep(0.5)
        side_bar.get_in_planner()
        planner_page = PlannerPage(self.driver)
        if self.driver.find_element_by_xpath("//li[contains(@class, 'page-item active')]/a").text != "1":
            self.driver.find_element_by_xpath("//li[contains(@class, 'page-item')]/a[text()='1']").click()

        self.driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.END)
        planner_page.go_to_redirect_advice(first_advice)
        advice_page.redirect_advice("Anulowana")
        advice_page.redirect_add_note("Transakcja anulowana")
        advice_page.go_to_new_advice()
        advice_page.go_to_carriage()
        time.sleep(2.5)
        advice_page.go_to_summary()
        advice_page.save()
        self.driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
        time.sleep(1.5)
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

        time.sleep(1)
        advice_page.get_into_aw()
        advice_page.change_advice_status("Nowa")
        side_bar.get_in_advices()
        DeletingFunctions.delete_aw_number(self.driver, first_advice)

    @allure.title("Filtrowanie plannera")
    def test_filters_planner(self):
        side_bar = SideBar(self.driver)
        side_bar.get_in_planner()
        planner_page = PlannerPage(self.driver)
        planner_page.open_filters()
        planner_page.filters_id("1605")
        planner_page.filters_product("pszko")
        planner_page.filters_deliverer("Fudala Marian")
        planner_page.filters_deliverer_address("62-080 Kobylniki, Szkolna 29")
        planner_page.filters_loading_date("2021-09-20 - 2021-09-20")
        planner_page.filters_delivery_date("2021-09-20 - 2021-09-22")
        planner_page.filters_receiver("Glencore Polska Sp. z o.o.")
        planner_page.filters_receiver_address("80-280 Gdańsk, Cypriana Kamila Norwida 2")
        planner_page.filters_carrier("A.T.S. Transport Siuta Andrzej")
        planner_page.filters_price_per_t("120", "165")
        planner_page.filters_price_per_t_currency("pln")
        planner_page.filters_price("3500", "4000")
        planner_page.filters_price_currency("pln")
        planner_page.filters_kz("KZ/007819")
        planner_page.filters_ks("KS/004411")
        planner_page.filters_advice_person("Sara")
        planner_page.use_filters()
        time.sleep(1)
        # assert
        planner_page.delete_filters()

        time.sleep(2)
        planner_page.open_filters()
        planner_page.filters_original_advice_number("AW/004226")
        planner_page.filters_advice_number("AW/004227")
        planner_page.filters_status("Zweryfikowana")
        planner_page.use_filters()
        time.sleep(1)
        # assert
        planner_page.delete_filters()
        assert False
