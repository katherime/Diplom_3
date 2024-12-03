from selenium.webdriver.common.by import By


class OrderFeedPageLocators:

    # Каунтер "Выполнено за все время"
    MAIN_H1_CONSTRUCTOR = By.CSS_SELECTOR, "div[class='undefined mb-15'] p[class='OrderFeed_number__2MbrQ text text_type_digits-large']"

    # Первый блок в ленте заказов
    FIRST_BLOCK_ORDER = By.XPATH, "(//li[@class='OrderHistory_listItem__2x95r mb-6'])[1]"

    DETAILS_OF_INGREDIENTS_ABOUT_ORDER = By.XPATH, "//h2[@class='Modal_list__2sHWc']"

    # Окно с подробностями об ингредиенте
    TEXT_POPUP_OF_INGREDIENT = By.XPATH, "//p[@class='text text_type_main-medium mb-8']"

    # Окно с подробностями об ингредиенте
    NUMBER_INGREDIENT = By.XPATH, "//p[@class='text text_type_digits-default']"

    # Код заказа в окне с подробностями об ингредиенте
    NUMBER_ORDER_IN_FEED = By.XPATH, "//p[@class='text text_type_digits-default mb-10 mt-5']"

    # Счётчик Выполнено за всё время
    COUNTER_ALL_ORDERS_FOR_ALL_TIME = By.CSS_SELECTOR, "div[class='undefined mb-15'] p[class='OrderFeed_number__2MbrQ text text_type_digits-large']"

    # Счётчик Выполнено за сегодня
    COUNTER_ALL_ORDERS_FOR_TODAY = By.CSS_SELECTOR, "div:nth-child(3) p:nth-child(2)"

    # Блок заказов в работе
    COUNTER_ORDERS_IN_WORK = By.CSS_SELECTOR, "ul[class='OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi'] li[class='text text_type_digits-default mb-2']"
