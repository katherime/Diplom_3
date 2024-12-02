from selenium.webdriver.common.by import By


class CabinetPageLocators:

    # Кнопка "Выход" из аккаунта
    BUTTON_EXIT_FROM_ACCOUNT = By.XPATH, "//button[text()='Выход']"

    # Кнопка перехода в "Историю заказов"
    BUTTON_HISTORY_OF_ORDERS = By.XPATH, "//a[contains(text(),'История заказов')]"

    # Блок История заказов
    LIST_HISTORY_OF_ORDERS = By.XPATH, "(//li[@class='OrderHistory_listItem__2x95r mb-6'])[1]"

    # Номер заказа в личном кабинете
    NUMBER_ORDER_IN_PERSONAL_CABINET = By.XPATH, "//p[@class='text text_type_digits-default']"
