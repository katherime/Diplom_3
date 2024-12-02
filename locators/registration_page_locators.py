from selenium.webdriver.common.by import By


class RegistrationPageLocators:

    ### Страница регистрации/входа в аккаунт
    # Поле ввода имени
    NAME_INPUT_FIELD = By.XPATH, '//label[ text()="Имя" ]/parent::div/input'

    # Поле ввода email
    EMAIL_INPUT_FIELD = By.XPATH, '//label[ text()="Email" ]/parent::div/input'

    # Поле ввода пароля
    PASSWORD_INPUT_FIELD = By.XPATH, '//label[ text()="Пароль" ]/parent::div/input'

    # Кнопка регистрации
    BUTTON_REGISTRATION = By.XPATH, '//button[ text()="Зарегистрироваться"]'

    # Кнопка "Войти" в аккаунт
    BUTTON_ENTERING_FORM = By.XPATH, '//button[ text()="Войти"]'

    # Заголовок "Вход" на странице ввода в аккаунт
    ENTER_AFTER_REGISTRATION = By.XPATH, '//h2[text()="Вход"]'

    # Заголовок с предупреждением о некорректном пароле
    WARNING_WRONG_PASSWORD = By.XPATH, '//p[text()="Некорректный пароль"]'

    # Заголовок с предупреждением о некорректном пароле
    BUTTON_RECOVERY_PASSWORD = By.XPATH, '//a[text()="Восстановить пароль"]'

