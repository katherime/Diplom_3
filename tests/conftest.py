import pytest
import urls
from pages.main_page import MainPage
from selenium import webdriver
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from pages.login_page import LoginPage
from pages.feed_order_page import FeedOrderPage


@pytest.fixture
def chrome():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def firefox():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


@pytest.fixture(params=["chrome", "firefox"])
def driver(request, chrome, firefox):
    if request.param == 'chrome':
        return chrome
    else:
        return firefox


@pytest.fixture
def open_main_stellar_burgers(driver):
    driver.get(urls.stellar_burgers_main)
    return driver


@pytest.fixture
def login_to_cabinet(driver):
    driver.get(urls.stellar_burgers_main)
    login_page = LoginPage(driver)
    login_page.login_to_personal_cabinet(driver)


@pytest.fixture
def create_order_and_return_number_order(driver, login_to_cabinet):
    base_page = BasePage(driver)
    feed_order = FeedOrderPage(driver)
    base_page.find_element_with_wait(MainPageLocators.BUTTON_FIRST_INGREDIENT)
    base_page.drag_and_drop_element(driver, MainPageLocators.BUTTON_FIRST_INGREDIENT,
                                    MainPageLocators.BUTTON_TOP_ELEMENT_OF_BURGER)
    base_page.click_to_element(driver, MainPageLocators.BUTTON_MAKE_ORDER)
    number_order = feed_order.return_number_order(driver)
    base_page.find_element_with_wait(MainPageLocators.BUTTON_CLOSE_INGREDIENT_POPUP)
    base_page.click_to_element(driver, MainPageLocators.BUTTON_CLOSE_INGREDIENT_POPUP)
    return number_order
