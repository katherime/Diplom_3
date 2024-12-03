from locators.main_page_locators import MainPageLocators
from locators.registration_page_locators import RegistrationPageLocators
from locators.cabinet_page_locators import CabinetPageLocators
from pages.base_page import BasePage
from data import DefaultAccount
import allure


class LoginPage(BasePage):

    @allure.step('Переход по клику на «Лента заказов»')
    def login_to_personal_cabinet(self, driver):
        base_page = BasePage(driver)
        base_page.click_to_element(driver, MainPageLocators.BUTTON_PERSONAL_CABINET)
        base_page.add_text_to_element(RegistrationPageLocators.EMAIL_INPUT_FIELD, DefaultAccount.default_email)
        base_page.add_text_to_element(RegistrationPageLocators.PASSWORD_INPUT_FIELD, DefaultAccount.default_password)
        base_page.click_to_element(driver, RegistrationPageLocators.BUTTON_ENTERING_FORM)
        base_page.find_element_with_wait(MainPageLocators.BUTTON_PERSONAL_CABINET)

    @allure.step('Переход по клику в «Личный кабинет»')
    def transition_to_personal_cabinet(self, driver):
        base_page = BasePage(driver)
        base_page.find_element_with_wait(MainPageLocators.BUTTON_PERSONAL_CABINET)
        base_page.click_to_element(driver, MainPageLocators.BUTTON_PERSONAL_CABINET)
        base_page.find_element_with_wait(CabinetPageLocators.BUTTON_EXIT_FROM_ACCOUNT)


    @allure.step('Переход по клику в «История заказов»')
    def transition_to_order_history_in_personal_cabinet(self, driver):
        base_page = BasePage(driver)
        base_page.find_element_with_wait(CabinetPageLocators.BUTTON_HISTORY_OF_ORDERS)
        base_page.click_to_element(driver, CabinetPageLocators.BUTTON_HISTORY_OF_ORDERS)
        base_page.find_element_with_wait(CabinetPageLocators.LIST_HISTORY_OF_ORDERS)

    @allure.step('Переход по клику в «История заказов»')
    def transition_to_exit_from_account(self, driver):
        base_page = BasePage(driver)
        base_page.find_element_with_wait(CabinetPageLocators.BUTTON_EXIT_FROM_ACCOUNT)
        base_page.click_to_element(driver, CabinetPageLocators.BUTTON_EXIT_FROM_ACCOUNT)
        base_page.find_element_with_wait(RegistrationPageLocators.BUTTON_ENTERING_FORM)