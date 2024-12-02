import allure
import urls
import data
from locators.main_page_locators import MainPageLocators
from locators.registration_page_locators import RegistrationPageLocators
from locators.recovery_page_locators import RecoveryPagePageLocators
from pages.base_page import BasePage
from pages.recovery_page import RecoveryPage
from selenium.webdriver.common.by import By
from data import DefaultAccount


class TestRecoveryPasswordPage:

    @allure.title('Тестирование перехода на страницу восстановления пароля по кнопке «Восстановить пароль», '
                  'ввод почты и клик по кнопке «Восстановить»')
    def test_transition_to_recovery_password_page(self, driver, open_main_stellar_burgers):
        recovery_page = RecoveryPage(driver)
        recovery_page.transition_to_recovery_password(driver)
        assert driver.current_url == urls.stellar_burgers_reset_password

    @allure.title('Тестирование подсвечивание поля ввода и скрытия/открытия пароля')
    def test_activate_field_for_recovery_password(self, driver, open_main_stellar_burgers):
        base_page = BasePage(driver)
        recovery_page = RecoveryPage(driver)
        recovery_page.transition_to_recovery_password(driver)
        recovery_page.click_hide_show_password(driver)
        element_status = base_page.find_element_with_wait(RecoveryPagePageLocators.INPUT_PASSWORD)
        assert data.class_focused_field in element_status.get_attribute("class")
