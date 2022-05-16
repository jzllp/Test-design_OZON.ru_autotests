# How to run:
#  1) Download driver for Chrome:
#     https://chromedriver.chromium.org/downloads
#  2) Install all required python packages library
#
#  3) Run in terminal with line:
#     python -m pytest -v --driver Chrome --driver-path <~>/chromedriver.exe tests/06_tests_ProfileMenu_LogIn.py


# При тестировании следует учитывать ограничение на количество попыток запроса проверочного кода.
# В случае их превышении автотесты с валидным значением номера телефона выдадут некорректный результат.
# Ограничение на количество попыток имеет временный характер.


from pages.ozon import LogIn


def test_check_input_phone_01(web_browser):
    """ Проверка меню авторизации 'Ozon ID'
    Проверяем: ввод валидного номера телефона в поле ввода телефона. """

    page = LogIn(web_browser)

    page.search_phone.send_keys('9000000000')
    page.search_btn_login.click()
    page.wait_page_loaded()
    # Проверяем активацию поля ввода проверочного кода
    assert page.search_security_code.get_text() == 'Введите код', 'Валидный номер телефона не прошел валидацию'


def test_check_input_phone_2(web_browser):
    """ Проверка меню авторизации 'Ozon ID'
    Проверяем: ввод невалидного (9 знаков) номера телефона в поле ввода телефона. """

    page = LogIn(web_browser)

    page.search_phone.send_keys('900000000')
    page.search_btn_login.click()
    page.wait_page_loaded()
    # Проверяем активацию поля ввода проверочного кода
    assert page.search_security_code.get_text() == 'Введите свой номер телефона, чтобы войти', \
        'Невалидный номер телефона прошел валидацию'


def test_check_input_phone_03(web_browser):
    """ Проверка меню авторизации 'Ozon ID'
    Проверяем: ввод валидного (валидный номер с добавлением одной цифры) номера телефона в поле ввода телефона. """

    page = LogIn(web_browser)

    page.search_phone.send_keys('90000000001')
    page.search_btn_login.click()
    page.wait_page_loaded()
    # Проверяем активацию поля ввода проверочного кода
    assert page.search_security_code.get_text() == 'Введите код', 'Валидный номер телефона не прошел валидацию'


def test_check_input_phone_4(web_browser):
    """ Проверка меню авторизации 'Ozon ID'
    Проверяем: ввод невалидного (9 знаков + буква) номера телефона в поле ввода телефона. """

    page = LogIn(web_browser)

    page.search_phone.send_keys('900000000д')
    page.search_btn_login.click()
    page.wait_page_loaded()
    # Проверяем активацию поля ввода проверочного кода
    assert page.search_security_code.get_text() == 'Введите свой номер телефона, чтобы войти', \
        'Невалидный номер телефона прошел валидацию'


def test_check_input_phone_5(web_browser):
    """ Проверка меню авторизации 'Ozon ID'
    Проверяем: ввод невалидного (9 знаков + буква) номера телефона в поле ввода телефона. """

    page = LogIn(web_browser)

    page.search_phone.send_keys('900000000L')
    page.search_btn_login.click()
    page.wait_page_loaded()
    # Проверяем активацию поля ввода проверочного кода
    assert page.search_security_code.get_text() == 'Введите свой номер телефона, чтобы войти', \
        'Невалидный телефона прошел валидацию'


def test_check_input_phone_6(web_browser):
    """ Проверка меню авторизации 'Ozon ID'
    Проверяем: ввод невалидного (9 знаков + символ) номера телефона в поле ввода телефона. """

    page = LogIn(web_browser)

    page.search_phone.send_keys('900000000$')
    page.search_btn_login.click()
    page.wait_page_loaded()
    # Проверяем активацию поля ввода проверочного кода
    assert page.search_security_code.get_text() == 'Введите свой номер телефона, чтобы войти', \
        'Невалидный номер телефона прошел валидацию'


def test_check_input_phone_7(web_browser):
    """ Проверка меню авторизации 'Ozon ID'
    Проверяем: ввод невалидного (9 знаков + пробел) номера телефона в поле ввода телефона. """

    page = LogIn(web_browser)

    page.search_phone.send_keys('900000000 ')
    page.search_btn_login.click()
    page.wait_page_loaded()
    # Проверяем активацию поля ввода проверочного кода
    assert page.search_security_code.get_text() == 'Введите свой номер телефона, чтобы войти', \
        'Невалидный номер телефона прошел валидацию'


def test_check_input_phone_8(web_browser):
    """ Проверка меню авторизации 'Ozon ID'
    Проверяем: ввод невалидного (10 буков) номера телефона в поле ввода телефона. """

    page = LogIn(web_browser)

    page.search_phone.send_keys('фывщзйцукш')
    page.search_btn_login.click()
    page.wait_page_loaded()
    # Проверяем активацию поля ввода проверочного кода
    assert page.search_security_code.get_text() == 'Введите свой номер телефона, чтобы войти', \
        'Невалидный номер телефона прошел валидацию'


def test_check_input_phone_9(web_browser):
    """ Проверка меню авторизации 'Ozon ID'
    Проверяем: ввод невалидного (10 буков) номера телефона в поле ввода телефона. """

    page = LogIn(web_browser)

    page.search_phone.send_keys('ZMXNCVBAJP')
    page.search_btn_login.click()
    page.wait_page_loaded()
    # Проверяем активацию поля ввода проверочного кода
    assert page.search_security_code.get_text() == 'Введите свой номер телефона, чтобы войти', \
        'Невалидный номер телефона прошел валидацию'


def test_check_input_phone_10(web_browser):
    """ Проверка меню авторизации 'Ozon ID'
    Проверяем: ввод невалидного (10 спецсимволов) номера телефона в поле ввода телефона. """

    page = LogIn(web_browser)

    page.search_phone.send_keys('!!!***^&^&')
    page.search_btn_login.click()
    page.wait_page_loaded()
    # Проверяем активацию поля ввода проверочного кода
    assert page.search_security_code.get_text() == 'Введите свой номер телефона, чтобы войти', \
        'Невалидный номер телефона прошел валидацию'


def test_check_input_phone_11(web_browser):
    """ Проверка меню авторизации 'Ozon ID'
    Проверяем: ввод невалидного (10 пробелов) номера телефона в поле ввода телефона. """

    page = LogIn(web_browser)

    page.search_phone.send_keys('          ')
    page.search_btn_login.click()
    page.wait_page_loaded()
    # Проверяем активацию поля ввода проверочного кода
    assert page.search_security_code.get_text() == 'Введите свой номер телефона, чтобы войти', \
        'Невалидный номер телефона прошел валидацию'


def test_check_input_phone_12(web_browser):
    """ Проверка меню авторизации 'Ozon ID'
    Проверяем: Вход без ввода номера телефона. """

    page = LogIn(web_browser)

    page.search_btn_login.click()
    page.wait_page_loaded()
    # Проверяем активацию поля ввода проверочного кода
    assert page.search_security_code.get_text() == 'Введите свой номер телефона, чтобы войти', \
        'Активировалось меню валидации'


def test_check_input_phone_13(web_browser):
    """ Проверка меню авторизации 'Ozon ID'
    Проверяем: ввод валидного (255 цифр) номера телефона в поле ввода телефона. """

    page = LogIn(web_browser)

    phone = "9" * 255
    page.search_phone.send_keys(phone)
    page.search_btn_login.click()
    page.wait_page_loaded()
    # Проверяем активацию поля ввода проверочного кода
    assert page.search_security_code.get_text() == 'Введите код', 'Валидный номер телефона не прошел валидацию'
