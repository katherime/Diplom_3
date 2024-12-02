import urls
import pytest
import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.feed_order_page import FeedOrderPage
from locators.cabinet_page_locators import CabinetPageLocators
from locators.feed_order_page_locators import OrderFeedPageLocators
import data
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestFeedOrders:

    @allure.title('Если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_popup_in_feed_of_orders(self, driver, open_main_stellar_burgers):
        feed_order = FeedOrderPage(driver)
        main_page = MainPage(driver)
        main_page.transition_to_history_of_orders(driver)
        text_order_window = feed_order.open_last_order_in_feed(driver)
        assert text_order_window == data.text_details_of_ingredient

    @allure.title('Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_user_orders_appears_in_history_of_orders(self, driver, create_order_and_return_number_order):
        main_page = MainPage(driver)
        feed_order = FeedOrderPage(driver)
        number_of_order = create_order_and_return_number_order
        main_page.transition_to_history_of_orders(driver)
        number_of_order_in_feed = feed_order.get_number_of_order_in_feed(driver)
        assert number_of_order_in_feed == f"#0{number_of_order}"

    @allure.title('При создании нового заказа счётчик "Выполнено за всё время" увеличивается')
    def test_update_counter_all_orders(self, driver, login_to_cabinet):
        main_page = MainPage(driver)
        feed_order = FeedOrderPage(driver)
        main_page.transition_to_history_of_orders(driver)
        number_of_all_orders_before_new_order = feed_order.return_number_all_orders(driver)
        main_page.transition_to_constructor(driver)
        main_page.making_order_from_main_page(driver)
        main_page.transition_to_history_of_orders(driver)
        number_of_all_orders_after_new_order = feed_order.return_number_all_orders(driver)
        assert number_of_all_orders_before_new_order < number_of_all_orders_after_new_order

    @allure.title('При создании нового заказа счётчик "Выполнено за сегодня" увеличивается,')
    def test_update_counter_today_orders(self, driver, login_to_cabinet):
        main_page = MainPage(driver)
        feed_order = FeedOrderPage(driver)
        main_page.transition_to_history_of_orders(driver)
        number_of_today_orders_before_new_order = feed_order.return_number_all_order_today(driver)
        main_page.transition_to_constructor(driver)
        main_page.making_order_from_main_page(driver)
        main_page.transition_to_history_of_orders(driver)
        number_of_today_orders_after_new_order = feed_order.return_number_all_order_today(driver)
        assert number_of_today_orders_before_new_order < number_of_today_orders_after_new_order

    @allure.title('После оформления заказа его номер появляется в разделе В работе')
    def test_update_counter_in_work_orders(self, driver, create_order_and_return_number_order):
        main_page = MainPage(driver)
        feed_order = FeedOrderPage(driver)
        main_page.transition_to_history_of_orders(driver)
        number_of_order = create_order_and_return_number_order
        main_page.transition_to_constructor(driver)
        main_page.transition_to_history_of_orders(driver)
        number_of_today_orders_after_new_order = feed_order.return_number_orders_in_work(driver)
        assert number_of_order in number_of_today_orders_after_new_order

