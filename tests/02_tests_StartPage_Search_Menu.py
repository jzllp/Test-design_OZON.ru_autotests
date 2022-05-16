# How to run:
#  1) Download driver for Chrome:
#     https://chromedriver.chromium.org/downloads
#  2) Install all required python packages library
#
#  3) Run in terminal with line:
#     python -m pytest -v --driver Chrome --driver-path <~>/chromedriver.exe tests/02_tests_StartPage_Search_Menu.py


from pages.ozon import SearchMenu


def test_check_search_menu_max_product(web_browser):
    """ Проверка меню поиска товаров
    Проверяем, что на страницу загрузилось максимально допустимое число искомых товаров. """

    page = SearchMenu(web_browser)

    page.search_searchMenu = 'телевизор'
    page.search_searchMenu_button.click()
    page.wait_page_loaded()

    # Проверяем количество найденных товаров на странице
    assert page.search_products_titles.count() == 36


def test_check_search_menu_correct_query(web_browser):
    """ Проверка меню поиска товаров
    Проверяем: соответствие искомого товара результату поиска. """

    page = SearchMenu(web_browser)

    page.search_searchMenu = 'велосипед'
    page.search_searchMenu_button.click()

    # Проверяем нашлись ли товары
    assert page.search_products_titles.count() > 0, 'Минимальное количество товаров не найдено'
    # Проверяем, что в названии найденных товаров присутствует название искомого товара
    for title in page.search_products_titles.get_text():
        msg = 'Название товаров в запросе не соответствуют результату поиска "{}"'.format(title)
        assert 'велосипед' in title.lower(), msg


def test_check_search_menu_register_query(web_browser):
    """ Проверка меню поиска товаров
    Проверяем: соответствие искомого товара в верхнем регистре результату поиска. """

    page = SearchMenu(web_browser)

    page.search_searchMenu = 'ВЕЛОСИПЕД'
    page.search_searchMenu_button.click()

    # Проверяем нашлись ли товары
    assert page.search_products_titles.count() > 0, 'Минимальное количество товаров не найдено'

    # Проверяем, что в названии найденных товаров присутствует название искомого товара
    for title in page.search_products_titles.get_text():
        msg = 'Название товаров в запросе не соответствуют результату поиска "{}"'.format(title)
        assert 'велосипед' in title.lower(), msg


def test_check_search_menu_Not_correct_register_query(web_browser):
    """ Проверка меню поиска товаров
    Проверяем: соответствие искомого товара в различном регистре результату поиска. """

    page = SearchMenu(web_browser)

    page.search_searchMenu = 'вЕлОсИпЕд'
    page.search_searchMenu_button.click()

    # Проверяем нашлись ли товары
    assert page.search_products_titles.count() > 0, 'Минимальное количество товаров не найдено'

    # Проверяем, что в названии найденных товаров присутствует название искомого товара
    for title in page.search_products_titles.get_text():
        msg = 'Название товаров в запросе не соответствуют результату поиска "{}"'.format(title)
        assert 'велосипед' in title.lower(), msg


def test_check_search_menu_Not_correct_query_result(web_browser):
    """ Проверка меню поиска товаров
    Проверяем: соответствие искомого товара с неправильной раскладкой клавиатуру результату поиска. """

    page = SearchMenu(web_browser)

    page.search_searchMenu = 'dtkjcbgtl'
    page.search_searchMenu_button.click()

    # Проверяем количество найденных товаров на странице
    assert page.search_products_titles.count() > 0, 'Минимальное количество товаров не найдено'

    # Проверяем, что в названии найденных товаров присутствует название искомого товара
    for title in page.search_products_titles.get_text():
        msg = 'Название товаров в запросе не соответствуют результату поиска "{}"'.format(title)
        assert 'велосипед' in title.lower(), msg


def test_check_search_menu_no_field(web_browser):
    """ Проверка меню поиска товаров
    Проверяем: возможность активации поиска без ввода данных в меню запроса. """

    page = SearchMenu(web_browser)
    page.search_searchMenu_button.click()

    # Проверяем активацию поиска
    assert page.get_current_url() == "https://www.ozon.ru/", 'Ошибка, поиск активировался" '


def test_check_search_menu_spec_character_query_result(web_browser):
    """ Проверка меню поиска товаров
    Проверяем: соответствие искомого товара со спецсимволами результату поиска. """

    page = SearchMenu(web_browser)

    page.search_searchMenu = '&&&'
    page.search_searchMenu_button.click()
    page.scroll_down()

    # Проверяем количество найденных товаров на странице
    assert page.search_products_titles.count() == 0, 'Ошибка, есть найденные товары'


def test_check_search_menu_category_filter_type(web_browser):
    """ Проверка сортировки товаров
    Проверяем: сортировку подкатегорий "Тип" товаров. """

    page = SearchMenu(web_browser)

    page.search_searchMenu = 'велосипед'
    page.search_searchMenu_button.click()
    page.search_products_sort_type.click()
    page.wait_page_loaded()

    # Проверяем нашлись ли товары
    assert page.search_products_titles.count() > 0, 'Минимальное количество товаров не найдено'

    # Проверяем, что в названии найденных товаров присутствует название искомого товара
    for title in page.search_products_titles.get_text():
        msg = 'Название товаров в запросе не соответствуют результату поиска "{}"'.format(title)
        assert 'электровелосипед' in title.lower(), msg


def test_check_search_menu_category_filter_brands(web_browser):
    """ Проверка сортировки товаров
    Проверяем: сортировку подкатегорий "Бренды" товаров. """

    page = SearchMenu(web_browser)

    page.search_searchMenu = 'велосипед'
    page.search_searchMenu_button.click()
    page.search_products_sort_brands.click()
    page.wait_page_loaded()

    # Проверяем нашлись ли товары
    assert page.search_products_titles.count() > 0, 'Минимальное количество товаров не найдено'

    # Проверяем, что в названии найденных товаров присутствует название искомого товара
    for title in page.search_products_titles.get_text():
        msg = 'Название товаров в запросе не соответствуют результату поиска "{}"'.format(title)
        assert 'велосипед' in title.lower(), msg


def test_check_search_menu_go_to_page_50(web_browser):
    """ Проверка меню поиска товаров
    Проверяем: соответствие искомого товара результату поиска на 50-й странице. """

    page = SearchMenu(web_browser)

    page.search_searchMenu = 'велосипед'
    page.search_searchMenu_button.click()
    page.search_go_button.scroll_to_element()
    page.search_page_input.send_keys('50')
    page.search_go_button.click()
    page.wait_page_loaded()
    page.search_page_50.scroll_to_element()

    # Проверяем нашлись ли товары
    assert page.search_products_titles.count() > 0, 'Минимальное количество товаров не найдено'

    # Проверяем, что в названии найденных товаров присутствует название искомого товара
    for title in page.search_products_titles.get_text():
        msg = 'Название товаров в запросе не соответствуют результату поиска "{}"'.format(title)
        assert 'велосипед' in title.lower(), msg

