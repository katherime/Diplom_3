from selenium.webdriver.common.by import By


class RecoveryPagePageLocators:

    # Поле ввода email
    EMAIL_INPUT_FIELD = By.XPATH, '//input[@name="name"]'

    # Кнопка для восстановления пароля
    BUTTON_RESET_PASSWORD = By.XPATH, "//button[contains(text(),'Восстановить')]"

    # Поле для восстановления пароля
    INPUT_RESET_PASSWORD = By.XPATH, "//div[@class='input pr-6 pl-6 input_type_password input_size_default']"

    # Поле для введения нового пароля
    INPUT_TEXT_RESET_PASSWORD = By.XPATH, "//button[contains(text(),'Пароль')]"

    # Кнопка для скрытия/открытия пароля
    SHOW_HIDE_BUTTON_PASSWORD_FIELD = By.XPATH, "//div[@class='input__icon input__icon-action']//*[name()='svg']"

    # Поле для введения пароля
    INPUT_PASSWORD = By.XPATH, "//label[contains(text(),'Пароль')]"

