import logging
import allure
import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class PayoffsPage:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.wait = WebDriverWait(self.driver, 15)
        self.add_template_xpath = "//a[text()='Dodaj nowy']"
        self.receiver_xpath = "//span[@aria-labelledby='select2-recipient-id-container']"
        self.receiver_input_xpath = "//input[@class='select2-search__field']"
        self.template_name_xpath = "//label[text()='Nazwa szablonu']/../../input"
        self.upload_file_xpath = "//span[text()='Wybierz plik']/../input"
        self.column_in_file_css = "#excel-columns-draggable > div > span:nth-child(1)"
        self.fail_alert_xpath = "//div[contains(@class, 'alert')]"
        self.delete_import_file_xpath = "//a[@class='close fileinput-exists']"

        self.advice_number_css = "#bt-table > tbody > tr:nth-child(2) > td.their-label"
        self.sales_number_css = "#bt-table > tbody > tr:nth-child(3) > td.their-label"
        self.delivery_date_css = "#bt-table > tbody > tr:nth-child(4) > td.their-label"
        self.tonnage_css = "#bt-table > tbody > tr:nth-child(8) > td.their-label"
        self.vehicle_number_css = "#bt-table > tbody > tr:nth-child(7) > td.their-label"

        self.save_button_xpath = "//button[text()='Zapisz']"
        self.success_alert_xpath = "//div[contains(@class, 'alert-success')]"

        self.confirm_delete_xpath = "//a[text()='Usuń']"

        self.import_receiver_xpath = "//span[@aria-labelledby='select2-recipient-id-container']"
        self.import_receiver_input_xpath = "//input[@class='select2-search__field']"
        self.import_upload_file_xpath = "//input[@id='filename']"
        self.import_connecting_button_xpath = "//button[text()='Przejdź do łączenia pozycji']"

        self.connection_list_xpath = "//div[@class='m-entry --settlement']/div[@class='m-entry__main']" \
                                     "//span[contains(text(), 'KS')]"
        self.connection_list_advices_xpath = "//div[contains(@class, 'a-smallTable__row')]/p[1][contains(text(), 'AW')]"
        self.save_connections_xpath = "//a[contains(text(), 'Zapisz rozliczenie')]"

        self.differences_buttons_xpath = "//a[text()='Zobacz rozbieżności']"
        self.differences_input_xpath = "//div[@class='o-modal__inner']//h2[text()='Niezgodności']" \
                                       "/following-sibling::div//input[not(@disabled)]"
        self.differences_copy_import_button_xpath = "//div[@class='o-modal__inner']//h2[text()='Niezgodności']" \
                                                    "/following-sibling::div//a[text()='Skopiuj dane z importu']"
        self.differences_accept_advice_button_xpath = "//div[@class='o-modal__inner']//h2[text()='Niezgodności']" \
                                                      "/following-sibling::div//a[text()='Akceptuj dane awizacji']"
        self.differences_save_changes_button_xpath = "//div[@class='o-modal__inner']" \
                                                     "//a[text()='Potwierdź oznaczone zmiany']"

    @allure.step("Przejscie do tworzenia nowego szablonu")
    def create_template(self):
        self.logger.info("Przejscie do tworzenia nowego szablonu")
        self.wait.until(ec.element_to_be_clickable((By.XPATH, self.add_template_xpath)))
        self.driver.find_element_by_xpath(self.add_template_xpath).click()

    @allure.step("Uzupelnianie danych szablonu")
    # "na sztywno" ustawione pod plik testy
    def set_template_data(self, receiver, template_name, file):
        self.logger.info("Uzupelnianie danych szablonu")
        self.wait.until(ec.element_to_be_clickable((By.XPATH, self.receiver_xpath)))
        self.driver.find_element_by_xpath(self.receiver_xpath).click()
        receiver_option_xpath = "//li[contains(text(), '" + receiver + "')]"
        receiver_input = self.driver.find_element_by_xpath(self.receiver_input_xpath)
        receiver_input.click()
        receiver_input.send_keys(receiver)
        self.wait.until(ec.element_to_be_clickable((By.XPATH, receiver_option_xpath)))
        self.driver.find_element_by_xpath(receiver_option_xpath).click()

        name = self.driver.find_element_by_xpath(self.template_name_xpath)
        name.click()
        name.send_keys(template_name)

        self.driver.find_element_by_xpath(self.upload_file_xpath).send_keys(file)

        """
        f = open("C:\\Users\\Sara\\PycharmProjects\\TMS_testy\\utils\\drag_and_drop.js", "r")
        javascript = f.read()
        f.close()

        for i in range(5):
            col = self.driver.find_element(By.CSS_SELECTOR, self.column_in_file_css)
            self.logger.info(col.text)
            target = None
            if col.text == "Nr Aw":
                target = self.driver.find_element(By.CSS_SELECTOR, self.advice_number_css)
            elif col.text == "Nr KS":
                target = self.driver.find_element(By.CSS_SELECTOR, self.sales_number_css)
            elif col.text == "Data dostawy":
                target = self.driver.find_element(By.CSS_SELECTOR, self.delivery_date_css)
            elif col.text == "Tonaż wyładunkowy":
                target = self.driver.find_element(By.CSS_SELECTOR, self.tonnage_css)
            elif col.text == "Nr rejestracyjny":
                target = self.driver.find_element(By.CSS_SELECTOR, self.vehicle_number_css)

            actions = ActionChains(self.driver)

            def apply_style(s):
                self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                                           target, s)

            original_style = target.get_attribute('style')
            apply_style("border: 2px solid red;")
            time.sleep(10)
            apply_style(original_style)

            self.driver.execute_script(javascript, col, target)

            # actions.drag_and_drop(col, target).click(target).perform()   # nie działa
            """

    @allure.step("Zapisanie szablonu")
    def save_template(self):
        self.logger.info("Zapisanie szablonu")
        self.driver.find_element_by_xpath(self.save_button_xpath).click()
        self.wait.until(ec.visibility_of_element_located((By.XPATH, self.success_alert_xpath)))

    @allure.step("Edytowanie szablonu")
    def edit_template(self, name, receiver):
        self.logger.info("Edytowanie szablonu")
        edit_xpath = "//td[text()='" + name + "']/following-sibling::td[text()='" + receiver +\
                     "']/..//a[@title='Edycja']"
        self.wait.until(ec.element_to_be_clickable((By.XPATH, edit_xpath)))
        self.driver.find_element_by_xpath(edit_xpath).click()

    @allure.step("Edycja nazwy szablonu")
    def edit_template_name(self, new_name):
        self.logger.info("Edycja nazwy szablonu")
        self.wait.until(ec.element_to_be_clickable((By.XPATH, self.template_name_xpath)))
        name = self.driver.find_element_by_xpath(self.template_name_xpath)
        name.click()
        name.clear()
        name.send_keys(new_name)

    @allure.step("Usuwanie szablonu")
    def delete_template(self, title, receiver):
        self.logger.info("Usuwanie szablonu")
        delete_xpath = "//td[text()='" + title + "']/following-sibling::td[text()='" + receiver + \
                       "']/..//a[@data-btn-ok-label='Usuń']"
        self.wait.until(ec.element_to_be_clickable((By.XPATH, delete_xpath)))
        self.driver.find_element_by_xpath(delete_xpath).click()

    @allure.step("Potwierdzenie usuniecia")
    def confirm_delete(self):
        self.logger.info("Potwierdzenie usuniecia")
        self.wait.until(ec.element_to_be_clickable((By.XPATH, self.confirm_delete_xpath)))
        self.driver.find_element_by_xpath(self.confirm_delete_xpath).click()

    @allure.step("Walidacja uzupelniania danych szablonu")
    def validate_template_data(self, receiver, template_name, file, wrong_file):
        self.logger.info("Uzupelnianie danych szablonu")
        result = True
        msg = ""
        self.wait.until(ec.element_to_be_clickable((By.XPATH, self.receiver_xpath)))
        receiver_option_xpath = "//li[contains(text(), '" + receiver + "')]"
        receiver_input = self.driver.find_element_by_xpath(self.receiver_input_xpath)

        name = self.driver.find_element_by_xpath(self.template_name_xpath)
        name.click()
        name.send_keys(template_name)

        self.driver.find_element_by_xpath(self.upload_file_xpath).send_keys(file)

        self.driver.find_element_by_xpath(self.save_button_xpath).click()

        try:
            self.driver.find_element_by_xpath(self.fail_alert_xpath)
        except NoSuchElementException:
            result = False
            msg += "Zapisano bez podania odbiorcy."
            return result, msg
        time.sleep(2)

        self.driver.find_element_by_xpath(self.receiver_xpath).click()
        receiver_input.click()
        receiver_input.send_keys(receiver)
        self.wait.until(ec.element_to_be_clickable((By.XPATH, receiver_option_xpath)))
        self.driver.find_element_by_xpath(receiver_option_xpath).click()

        name.clear()

        try:
            self.driver.find_element_by_xpath(self.fail_alert_xpath)
        except NoSuchElementException:
            result = False
            msg += "Zapisano bez nazwy szablonu."
            return result, msg
        time.sleep(2)

        name.click()
        name.send_keys(template_name)

        self.driver.find_element_by_xpath(self.delete_import_file_xpath).click()

        try:
            self.driver.find_element_by_xpath(self.fail_alert_xpath)
        except NoSuchElementException:
            result = False
            msg += "Zapisano bez pliku."
            return result, msg
        time.sleep(2)

        # zły plik

    @allure.step("Wybor odbiorcy")
    def set_receiver_import(self, receiver):
        self.logger.info("Wybor odbiorcy")
        self.wait.until(ec.element_to_be_clickable((By.XPATH, self.import_receiver_xpath)))
        self.driver.find_element_by_xpath(self.import_receiver_xpath).click()
        receiver_input = self.driver.find_element_by_xpath(self.import_receiver_input_xpath)
        receiver_input.click()
        receiver_input.send_keys(receiver)
        receiver_option_xpath = "//li[contains(text(), '" + receiver + "')]"
        self.driver.find_element_by_xpath(receiver_option_xpath).click()

    @allure.step("Wybor szablonu")
    def set_template_import(self, template):
        self.logger.info("Wybor szablonu")
        template_option_xpath = "//select[@id='billing-template-id']/option[text()='" + template + "']"
        self.driver.find_element_by_xpath(template_option_xpath).click()

    @allure.step("Przeslanie pliku z rozliczeniem")
    def upload_payoff(self, file):
        self.logger.info("Przeslanie pliku z rozliczeniem")
        self.driver.find_element_by_xpath(self.import_upload_file_xpath).send_keys(file)

    @allure.step("Przejscie do laczenia pozycji")
    def go_to_connecting_positions(self):
        self.logger.info("Przejscie do laczenia pozycji")
        self.driver.find_element_by_xpath(self.import_connecting_button_xpath).click()

    @allure.step("Walidacja polaczen")
    def check_connections(self, connections_number, connections_dict):
        self.logger.info("Walidacja polaczen")
        connection_list_advices = self.driver.find_elements_by_xpath(self.connection_list_advices_xpath)
        connection_list = self.driver.find_elements_by_xpath(self.connection_list_xpath)
        if len(connection_list_advices) == connections_number:
            for i in range(len(connection_list)):
                con_xpath = "//div[" + str(i + 1) + "][@class='m-entry --settlement']//span[contains(text(), '" + \
                            connection_list[i].get_attribute("innerHTML") + "')]/../../../following-sibling::div//p[1]"
                con = self.driver.find_element_by_xpath(con_xpath)

                if con.get_attribute("innerHTML")[1:10] in \
                        connections_dict[connection_list[i].get_attribute("innerHTML")[4:]]:
                    continue
                else:
                    return False, "Nieprawidłowo połączony import: " + connection_list[i].get_attribute("innerHTML")[4:]

            return True, ""
        else:
            return False, "Nieprawidłowa liczba zaimportowanych pozycji: " + str(len(connection_list_advices))

    @allure.step("Usuwanie importu")
    def delete_import(self, title, receiver):
        self.logger.info("Usuwanie importu")
        delete_xpath = "//td[text()='" + title + "']/following-sibling::td[text()='" + receiver + \
                       "']/..//a[@data-btn-ok-label='Usuń']"
        self.wait.until(ec.element_to_be_clickable((By.XPATH, delete_xpath)))
        self.driver.find_element_by_xpath(delete_xpath).click()

    @allure.step("Zapisanie polaczen")
    def save_connections(self):
        self.logger.info("Zapisanie polaczen")
        self.driver.find_element_by_xpath(self.save_connections_xpath).click()

    @allure.step("Usuwanie pozycji z importu")
    def delete_import_line(self, line):
        self.logger.info("Usuwanie pozycji z importu")
        deletion_line = "//tr[" + line + "]//button[contains(@class, 'datatable-delete-button')]"
        self.driver.find_element_by_xpath(deletion_line).click()

    @allure.step("Porownywanie rozbieznosci")
    def compare_differences(self):
        self.logger.info("Porownywanie rozbieznosci")
        differences_list = self.driver.find_elements_by_xpath(self.differences_buttons_xpath)
        i = len(differences_list)
        for diff in differences_list:
            diff.click()
            if i == 3:
                diff_input = self.driver.find_element_by_xpath(self.differences_input_xpath)
                diff_input.click()
                diff_input.clear()
                diff_input.send_keys("12ABDE")
                time.sleep(1)
            if i == 2:
                self.driver.find_element_by_xpath(self.differences_copy_import_button_xpath).click()
            if i == 1:
                self.driver.find_element_by_xpath(self.differences_accept_advice_button_xpath).click()

            self.driver.find_element_by_xpath(self.differences_save_changes_button_xpath).click()
            i -= 1
            time.sleep(1)
