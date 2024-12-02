from selenium.webdriver.common.by import By


class MainPageLocators:

    ### Главная страница
    # Заголовок "Соберите бургер" на главной странице
    MAIN_H1_CONSTRUCTOR = By.XPATH, '//h1[text()="Соберите бургер"]'

    # Кнопка перехода в личный кабинет
    BUTTON_PERSONAL_CABINET = By.XPATH, '//p[text()="Личный Кабинет"]'

    # Кнопка перехода в аккаунт
    BUTTON_ENTER_TO_ACCOUNT = By.XPATH, '//button[text()=\'Войти в аккаунт\']'

    # Кнопка "Конструктор"
    BUTTON_CONSTRUCTOR = By.XPATH, "//p[contains(text(),'Конструктор')]"

    # Кнопка оформления заказа бургера после входа в аккаунт
    BUTTON_MAKE_ORDER = By.XPATH, "//button[contains(text(),'Оформить заказ')]"

    # Кнопка перехода в Ленту заказов
    BUTTON_ORDERS_FEED = By.XPATH, "//p[contains(text(),'Лента Заказов')]"

    ### Ингредиенты
    # Открытие окна первого ингредиента в списке
    BUTTON_FIRST_INGREDIENT = By.XPATH, " (//a[@class='BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8'])[1]"

    # Кнопка закрытия окна ингредиента
    BUTTON_CLOSE_INGREDIENT_POPUP = By.XPATH, "//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']"

    # Верхний блок добавления ингредиента
    BUTTON_TOP_ELEMENT_OF_BURGER = By.XPATH,"//div[@class = 'constructor-element constructor-element_pos_top']"

    # Каунтер первого ингредиента в списке
    COUNTER_OF_FIRST_INGREDIENT = By.XPATH, "//p[@class = 'counter_counter__num__3nue1']"

    # Номер полученного заказа после оформления заказа
    NUMBER_OF_MAKED_ORDER = By.CSS_SELECTOR, '.Modal_modal__title_shadow__3ikwq.Modal_modal__title__2L34m.text.text_type_digits-large.mb-8'

    # Номер полученного заказа после оформления заказа
    TEXT_ABOUT_MAKING_ORDER = By.XPATH, "//div[@class='Modal_modal__textContainer__9TwLS']"

    # Номер полученного заказа после оформления заказа
    POPUP_WINDOW_INGREDIENT = By.XPATH, "//ul[@class='Modal_modal__statsList__6cEm5']"

    # Блок подробностей об ингредиенте
    DETAILS_OF_INGREDIENT = By.XPATH, "//p[@class='text text_type_main-medium mb-8']"

