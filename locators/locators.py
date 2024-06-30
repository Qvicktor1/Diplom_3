from selenium.webdriver.common.by import By


class MainPageLocators:
    account_button_header = (By.XPATH, ".//a[@href='/account']")  # кнопка "Личный кабинет" в шапке
    constructor_button_header = (By.XPATH, ".//p[text()='Конструктор']")  # кнопка "Конструктор" в шапке
    feed_button_header = (By.XPATH, ".//a[@href='/feed']")  # кнопка "Лента заказов" в шапке
    compile_burger_header = (By.XPATH, ".//h1[text()='Соберите бургер']")  # заголовок "Соберите бургер" на главной странице
    place_order_button = (By.XPATH, ".//button[text()='Оформить заказ']")  # кнопка "Оформить заказ" на главной
    fluoric_bun_name = (By.XPATH, ".//p[text()='Флюоресцентная булка R2-D3']")  # название булки
    fluoric_bun_counter = (By.XPATH, ".//img[@alt='Флюоресцентная булка R2-D3']/../div[@class='counter_counter__ZNLkj counter_default__28sqi']")  # счетчик булки
    ingredient_name = (By.XPATH, ".//p[text()='Мясо бессмертных моллюсков Protostomia']")  # название ингредиента
    ingredient_counter = (By.XPATH, ".//img[@alt='Мясо бессмертных моллюсков Protostomia']/../div[@class = 'counter_counter__ZNLkj counter_default__28sqi']")  # счетчик ингредиента
    ingredient_details_header = (By.XPATH, ".//h2[text()='Детали ингредиента']")  # заголовок всплывающего окна "Детали ингредиента"
    ingredient_details_close_button = (By.XPATH, ".//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']")  # кнопка закрытия всплывающего окна "Детали ингредиента"
    constructor_upper_bun_placeholder = (By.XPATH, ".//span[text()='Перетяните булочку сюда (верх)']")
    order_identifier_header = (By.XPATH, ".//p[text()='идентификатор заказа']")  # надпись "идентификатор заказа" во всплывающем окне с подтверждением заказа
    order_number = (By.XPATH, ".//p[text()='идентификатор заказа']/../h2")  # номер заказа во всплывающем окне с подтверждением заказа
    order_number_window_close_button = (By.XPATH, ".//button[@type='button']")  # кнопка закрытия всплывающего окна с подтверждением заказа


class FeedPageLocators:
    feed_header = (By.XPATH, ".//h1[text()='Лента заказов']")  # заголовок "Лента заказов" в ленте заказов
    composition_header = (By.XPATH, ".//p[text()='Cостав']")  # надпись "Состав" на всплывающем окне с деталями заказа
    completed_all_time_counter = (By.XPATH, ".//p[text()='Выполнено за все время:']/../p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']")  # Счетчик заказов "Выполнено за все время"
    completed_today_counter = (By.XPATH, ".//p[text()='Выполнено за сегодня:']/../p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']")  # Счетчик заказов "Выполнено за сегодня"
    in_progress_number = (By.XPATH, ".//ul[@class='OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi']/li")  # Номер заказа в разделе "В работе"
    order_number_template = (By.XPATH, ".//p[(text()='#')]")

class LoginPageLocators:
    sign_in_button = (By.XPATH, ".//button[text()='Войти']")  # кнопка "Войти" в форме авторизации
    email_input_field = (By.XPATH, ".//h2[text()='Вход']/..//label[text() = 'Email']/../input")  # поле ввода "Email" в форме авторизации
    password_input_field = (By.XPATH, ".//h2[text()='Вход']/..//label[text() = 'Пароль']/../input")  # поле ввода "Пароль" в форме авторизации
    forgot_password_button_login = (By.XPATH, ".//a[text()='Восстановить пароль']")  # кнопка "Восстановить пароль" в форме авторизации


class ProfilePageLocators:
    profile_url = (By.XPATH, ".//a[text()='Профиль']")  # ссылка "Профиль" в личном кабинете
    orders_history_url = (By.XPATH, ".//a[text()='История заказов']")  # ссылка "История заказов" в личном кабинете
    exit_button = (By.XPATH, ".//button[text()='Выход']")  # кнопка "Выход" в личном кабинете


class HistoryPageLocators:
    order_number_history = (By.XPATH, ".//p[contains(text(), '#')]")  # номер заказа в "Истории заказов"


class ForgotPasswordPageLocators:
    email_entry_field_fpp = (By.XPATH, ".//input[@type='text']")  # поле ввода почты на странице "Восстановление пароля"
    recover_button_fpp = (By.XPATH, ".//button[text()='Восстановить']")  # кнопка "Восстановить" на странице "Восстановление пароля"


class ResetPasswordPageLocators:
    show_password_button = (By.XPATH, ".//div[@class='input__icon input__icon-action']")  # кнопка "Показать/скрыть пароль" на странице Ввода нового пароля
    password_field_highlight = (By.XPATH, ".//input[@type='text']")  # подсветка поля ввода пароля