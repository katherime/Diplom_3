import urls
import pytest
import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from pages.login_page import LoginPage
from locators.cabinet_page_locators import CabinetPageLocators
from locators.registration_page_locators import RegistrationPageLocators


class TestPersonalCabinet:

    @allure.title('Тестирование перехода по клику в «Личный кабинет»')
    def test_transition_to_personal_cabinet_page(self, driver, open_main_stellar_burgers):
        login_page = LoginPage(driver)
        login_page.login_to_personal_cabinet(driver)
        login_page.transition_to_personal_cabinet(driver)
        assert driver.current_url == urls.stellar_burgers_personal_cabinet

    @allure.title('Тестирование перехода в раздел «История заказов')
    def test_transition_to_history_of_orders(self, driver, open_main_stellar_burgers):
        login_page = LoginPage(driver)
        base_page = BasePage(driver)
        login_page.login_to_personal_cabinet(driver)
        base_page.find_element_with_wait(MainPageLocators.BUTTON_PERSONAL_CABINET)
        base_page.click_to_element(driver, MainPageLocators.BUTTON_PERSONAL_CABINET)
        login_page.transition_to_order_history_in_personal_cabinet(driver)
        assert driver.current_url == urls.stellar_burgers_history_of_orders

    @allure.title('Тестирование выхода из аккаунта')
    def test_exit_from_account(self, driver, open_main_stellar_burgers):
        login_page = LoginPage(driver)
        base_page = BasePage(driver)
        login_page.login_to_personal_cabinet(driver)
        base_page.find_element_with_wait(MainPageLocators.BUTTON_PERSONAL_CABINET)
        base_page.click_to_element(driver, MainPageLocators.BUTTON_PERSONAL_CABINET)
        login_page.transition_to_exit_from_account(driver)
        assert driver.current_url == urls.stellar_burgers_login
