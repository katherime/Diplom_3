import allure
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Найти элемент с ожиданием')
    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 14).until(
            expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Найти элемент без ожидания')
    def find_element_no_wait(self, locator):
        return self.driver.find_element(*locator)

    @allure.step('Клик по элементу')
    def click_to_element(self, driver, locator):
        if driver.name == 'chrome':
            WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(locator))
            self.driver.find_element(*locator).click()
        else:
            WebDriverWait(self.driver, 13).until(expected_conditions.visibility_of_element_located(locator))
            element = self.driver.find_element(*locator)
            actions = ActionChains(self.driver)
            actions.move_to_element(element).click(element).perform()

    @allure.step('Добавить текст в элемент')
    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    @allure.step('Получить текст из элемента')
    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    @allure.step('Скролл до элемента')
    def scrolling_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Перенос элемента в другое место')
    def drag_and_drop_element(self, driver, locator_from, locator_to):
        if driver.name == 'chrome':
            self.find_element_with_wait(locator_from)
            self.find_element_with_wait(locator_to)
            element_from = self.driver.find_element(*locator_from)
            element_to = self.driver.find_element(*locator_to)
            actions = ActionChains(driver)
            actions.click_and_hold(element_from).move_to_element(element_to).release().perform()
        else:
            self.find_element_with_wait(locator_from)
            self.find_element_with_wait(locator_to)
            element_from = self.driver.find_element(*locator_from)
            element_to = self.driver.find_element(*locator_to)
            self.driver.execute_script("""
            var source = arguments[0];
            var target = arguments[1];
            var evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragstart", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            source.dispatchEvent(evt);
            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragenter", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);
            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragover", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);
            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("drop", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);
            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragend", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            source.dispatchEvent(evt);
            """, element_from, element_to)