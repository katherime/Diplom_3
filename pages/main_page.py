import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.registration_page_locators import RegistrationPageLocators
from pages.base_page import BasePage
from data import DefaultAccount
import urls


class MainPage(BasePage):

    @allure.step('Переход по клику на «Лента заказов»')
    def transition_to_history_of_orders(self, driver):
        base_page = BasePage(driver)
        base_page.find_element_with_wait(MainPageLocators.BUTTON_ORDERS_FEED)
        base_page.click_to_element(driver, MainPageLocators.BUTTON_ORDERS_FEED)

    @allure.step('Переход по клику на «Конструктор»')
    def transition_to_constructor(self, driver):
        base_page = BasePage(driver)
        base_page.find_element_with_wait(MainPageLocators.BUTTON_CONSTRUCTOR)
        base_page.click_to_element(driver, MainPageLocators.BUTTON_CONSTRUCTOR)

    @allure.step('Создание заказа на главной странице')
    def making_order_from_main_page(self, driver):
        base_page = BasePage(driver)
        base_page.find_element_with_wait(MainPageLocators.BUTTON_FIRST_INGREDIENT)
        base_page.drag_and_drop_element(driver, MainPageLocators.BUTTON_FIRST_INGREDIENT,
                                        MainPageLocators.BUTTON_TOP_ELEMENT_OF_BURGER)
        base_page.find_element_with_wait(MainPageLocators.BUTTON_MAKE_ORDER)
        base_page.click_to_element(driver, MainPageLocators.BUTTON_MAKE_ORDER)
        text = base_page.get_text_from_element(MainPageLocators.NUMBER_OF_MAKED_ORDER)
        while text == '9999':
            base_page.find_element_with_wait(MainPageLocators.NUMBER_OF_MAKED_ORDER)
            text = base_page.get_text_from_element(MainPageLocators.NUMBER_OF_MAKED_ORDER)
        base_page.find_element_with_wait(MainPageLocators.BUTTON_CLOSE_INGREDIENT_POPUP)
        base_page.click_to_element(driver, MainPageLocators.BUTTON_CLOSE_INGREDIENT_POPUP)

    @allure.step('Открытие и закрытие popup с данными об ингредиенте')
    def open_popup_about_ingredient_and_close(self, driver):
        base_page = BasePage(driver)
        base_page.find_element_with_wait(MainPageLocators.BUTTON_FIRST_INGREDIENT)
        base_page.click_to_element(driver, MainPageLocators.BUTTON_FIRST_INGREDIENT)
        base_page.find_element_with_wait(MainPageLocators.DETAILS_OF_INGREDIENT)
        base_page.find_element_with_wait(MainPageLocators.BUTTON_CLOSE_INGREDIENT_POPUP)
        base_page.click_to_element(driver, MainPageLocators.BUTTON_CLOSE_INGREDIENT_POPUP)
        base_page.find_element_with_wait(MainPageLocators.BUTTON_CONSTRUCTOR)
        base_page.find_element_with_wait(MainPageLocators.BUTTON_TOP_ELEMENT_OF_BURGER)
        base_page.drag_and_drop_element(driver, MainPageLocators.BUTTON_FIRST_INGREDIENT,
                                        MainPageLocators.BUTTON_TOP_ELEMENT_OF_BURGER)

    @allure.step('Открытие popup с данными об ингредиенте')
    def open_popup_about_ingredient(self, driver):
        base_page = BasePage(driver)
        base_page.find_element_with_wait(MainPageLocators.BUTTON_FIRST_INGREDIENT)
        base_page.click_to_element(driver, MainPageLocators.BUTTON_FIRST_INGREDIENT)
        base_page.find_element_with_wait(MainPageLocators.BUTTON_FIRST_INGREDIENT)
