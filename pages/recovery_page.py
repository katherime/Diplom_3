from locators.main_page_locators import MainPageLocators
from locators.registration_page_locators import RegistrationPageLocators
from locators.recovery_page_locators import RecoveryPagePageLocators
from locators.cabinet_page_locators import CabinetPageLocators
from pages.base_page import BasePage
from data import DefaultAccount
import allure


class RecoveryPage(BasePage):

    @allure.step('Переход в окно восстановления пароля')
    def transition_to_recovery_password(self, driver):
        base_page = BasePage(driver)
        base_page.click_to_element(driver, MainPageLocators.BUTTON_PERSONAL_CABINET)
        base_page.click_to_element(driver, RegistrationPageLocators.BUTTON_RECOVERY_PASSWORD)
        base_page.click_to_element(driver, RegistrationPageLocators.EMAIL_INPUT_FIELD)
        base_page.add_text_to_element(RegistrationPageLocators.EMAIL_INPUT_FIELD, DefaultAccount.default_email)
        base_page.click_to_element(driver, RecoveryPagePageLocators.BUTTON_RESET_PASSWORD)
        base_page.find_element_with_wait(RecoveryPagePageLocators.INPUT_RESET_PASSWORD)

    @allure.step('Клик по кнопке скрытия/открытия пароля')
    def click_hide_show_password(self, driver):
        base_page = BasePage(driver)
        base_page.find_element_with_wait(RecoveryPagePageLocators.SHOW_HIDE_BUTTON_PASSWORD_FIELD)
        base_page.click_to_element(driver, RecoveryPagePageLocators.SHOW_HIDE_BUTTON_PASSWORD_FIELD)