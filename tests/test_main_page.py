import urls
import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import data
from pages.main_page import MainPage


class TestMainPage:

    @allure.title('Тестирование перехода по клику на «Конструктор»')
    def test_transition_to_constructor_page(self, driver, open_main_stellar_burgers):
        main_page = MainPage(driver)
        main_page.transition_to_history_of_orders(driver)
        main_page.transition_to_constructor(driver)
        assert driver.current_url == urls.stellar_burgers_main

    @allure.title('Тестирование перехода по клику на «Лента заказов»')
    def test_transition_to_history_of_orders(self, driver, open_main_stellar_burgers):
        main_page = MainPage(driver)
        main_page.transition_to_history_of_orders(driver)
        assert driver.current_url == urls.stellar_burgers_feed

    @allure.title('Тестирование появления всплывающего окна при клике на ингредиент')
    def test_open_ingredient_popup(self, driver, open_main_stellar_burgers):
        main_page = MainPage(driver)
        main_page.open_popup_about_ingredient(driver)
        assert driver.current_url == urls.stellar_ingredient_popup

    @allure.title('Тестирование закрытия всплывающего окна при клике на ингредиент')
    def test_close_ingredient_popup(self, driver, open_main_stellar_burgers):
        base_page = BasePage(driver)
        main_page = MainPage(driver)
        main_page.open_popup_about_ingredient_and_close(driver)
        popup_ingredient = base_page.find_element_no_wait(MainPageLocators.POPUP_WINDOW_INGREDIENT)
        base_page.find_element_with_wait(MainPageLocators.BUTTON_TOP_ELEMENT_OF_BURGER)
        base_page.click_to_element(driver, MainPageLocators.BUTTON_TOP_ELEMENT_OF_BURGER)
        popup_display = popup_ingredient.is_displayed()
        assert popup_display is not True

    @allure.title('При добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента')
    def test_add_ingredient_increase_counter(self, driver, open_main_stellar_burgers):
        base_page = BasePage(driver)
        base_page.find_element_with_wait(MainPageLocators.BUTTON_FIRST_INGREDIENT)
        base_page.drag_and_drop_element(driver, MainPageLocators.BUTTON_FIRST_INGREDIENT,
                                        MainPageLocators.BUTTON_TOP_ELEMENT_OF_BURGER)
        number_ingredient = base_page.get_text_from_element(MainPageLocators.COUNTER_OF_FIRST_INGREDIENT)
        assert number_ingredient == data.number_counter_after_add_two_ingredient

    @allure.title('Залогиненный пользователь может оформить заказ')
    def test_login_user_can_make_order(self, driver, login_to_cabinet):
        base_page = BasePage(driver)
        base_page.find_element_with_wait(MainPageLocators.BUTTON_FIRST_INGREDIENT)
        base_page.drag_and_drop_element(driver, MainPageLocators.BUTTON_FIRST_INGREDIENT,
                                        MainPageLocators.BUTTON_TOP_ELEMENT_OF_BURGER)
        base_page.click_to_element(driver, MainPageLocators.BUTTON_MAKE_ORDER)
        base_page.find_element_with_wait(MainPageLocators.NUMBER_OF_MAKED_ORDER)
        text = base_page.get_text_from_element(MainPageLocators.TEXT_ABOUT_MAKING_ORDER)
        assert text == data.text_successful_order
