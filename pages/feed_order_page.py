import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from locators.cabinet_page_locators import CabinetPageLocators
from locators.feed_order_page_locators import OrderFeedPageLocators


class FeedOrderPage(BasePage):

    @allure.step('Переход по клику на «Лента заказов»')
    def return_number_order(self, driver):
        base_page = BasePage(driver)
        text = base_page.get_text_from_element(MainPageLocators.NUMBER_OF_MAKED_ORDER)
        while text == '9999':
            base_page.find_element_with_wait(MainPageLocators.NUMBER_OF_MAKED_ORDER)
            text = base_page.get_text_from_element(MainPageLocators.NUMBER_OF_MAKED_ORDER)
        number_order = text
        return number_order

    @allure.step('Открытие последнего заказа в списке и получение данных из блока')
    def open_last_order_in_feed(self, driver):
        base_page = BasePage(driver)
        base_page.find_element_with_wait(OrderFeedPageLocators.FIRST_BLOCK_ORDER)
        base_page.click_to_element(driver, OrderFeedPageLocators.FIRST_BLOCK_ORDER)
        text_order_window = base_page.get_text_from_element(OrderFeedPageLocators.TEXT_POPUP_OF_INGREDIENT)
        return text_order_window

    @allure.step('Открытие последнего заказа в списке')
    def get_number_of_order_in_feed(self, driver):
        base_page = BasePage(driver)
        base_page.click_to_element(driver, OrderFeedPageLocators.FIRST_BLOCK_ORDER)
        number_of_order_in_feed = base_page.get_text_from_element(OrderFeedPageLocators.NUMBER_ORDER_IN_FEED)
        return number_of_order_in_feed

    @allure.step('Получить значение числа всех заказов, сделанных за все время')
    def return_number_all_orders(self, driver):
        base_page = BasePage(driver)
        base_page.find_element_with_wait(OrderFeedPageLocators.COUNTER_ALL_ORDERS_FOR_ALL_TIME)
        number_of_all_orders = base_page.get_text_from_element(OrderFeedPageLocators.COUNTER_ALL_ORDERS_FOR_ALL_TIME)
        return number_of_all_orders

    @allure.step('Получить значение числа всех заказов, сделанных за сегодня')
    def return_number_all_order_today(self, driver):
        base_page = BasePage(driver)
        base_page.find_element_with_wait(OrderFeedPageLocators.COUNTER_ALL_ORDERS_FOR_TODAY)
        number_of_all_orders = base_page.get_text_from_element(OrderFeedPageLocators.COUNTER_ALL_ORDERS_FOR_TODAY)
        return number_of_all_orders

    @allure.step('Получить значение числа заказов, находящихся в работе')
    def return_number_orders_in_work(self, driver):
        base_page = BasePage(driver)
        base_page.find_element_with_wait(OrderFeedPageLocators.COUNTER_ORDERS_IN_WORK)
        base_page.get_text_from_element(OrderFeedPageLocators.COUNTER_ORDERS_IN_WORK)
        number_of_all_orders = base_page.get_text_from_element(OrderFeedPageLocators.COUNTER_ORDERS_IN_WORK)
        return number_of_all_orders