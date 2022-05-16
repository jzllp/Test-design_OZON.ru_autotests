# How to run:
#  1) Download driver for Chrome:
#     https://chromedriver.chromium.org/downloads
#  2) Install all required python packages library
#
#  3) Run in terminal with line:
#     python -m pytest -v --driver Chrome --driver-path <~>/chromedriver.exe tests/03_test_Card_Product.py


from pages.ozon import SearchMenu, ProductCard


def test_check_open_product_card_01(web_browser):
    """ Проверка Карточки продукта
    Проверяем: переход в карточку продукта по клику на название продукта. """

    page = SearchMenu(web_browser)

    page.search_searchMenu = 'велосипед'
    page.search_searchMenu_button.click()

    # Проверяем количество найденных товаров на странице
    assert page.search_products_titles.count() > 0, 'Минимальное количество товаров не найдено'

    page.search_first_item.scroll_to_element()
    page.search_first_item.click()

    # Делаем скриншот конечного результата
    page.screenshot('test_check_open_product_card_01.png')


def test_check_open_product_card_02(web_browser):
    """ Проверка Карточки продукта
    Проверяем: переход в карточку продукта по клику на фото. """

    page = SearchMenu(web_browser)

    page.search_searchMenu = 'Скутер'
    page.search_searchMenu_button.click()

    # Проверяем количество найденных товаров на странице
    assert page.search_products_titles.count() > 0, 'Минимальное количество товаров не найдено'

    page.search_first_photo.scroll_to_element()
    page.search_first_photo.click()

    # Делаем скриншот конечного результата
    page.screenshot('test_check_open_product_card_02.png')


def test_check_open_product_card_code(web_browser):
    """ Проверка Карточки продукта
    Проверяем: поиск продукта по Коду товара и переход в карточку. """

    page = SearchMenu(web_browser)
    page_card = ProductCard(web_browser)

    page.search_searchMenu = '24915135'
    page.search_searchMenu_button.click()

    # Проверяем количество найденных товаров на странице
    assert page.search_products_titles_mini.count() > 0, 'Минимальное количество товаров не найдено'

    page.search_photo_mini_result.click()

    # Проверяем равенство значения в запросе и в карточке
    assert page_card.search_product_kode.get_text()[12:] == '24915135', 'Код товара в запросе не соответствует коду ' \
                                                                        'продукта'


def test_check_open_product_card_title(web_browser):
    """ Проверка Карточки продукта
    Проверяем: соответствие названия продукта в результате поиска и в карточке товара. """

    page = SearchMenu(web_browser)
    page_card = ProductCard(web_browser)

    page.search_searchMenu = '24915135'
    page.search_searchMenu_button.click()

    # Проверяем количество найденных товаров на странице
    assert page.search_products_titles_mini.count() > 0, 'Минимальное количество товаров не найдено'

    item = page.search_item_mini_result.get_text()
    page.search_photo_mini_result.click()

    # Проверяем соответствие названия продукта в результате поиска и в карточке
    assert item == page_card.search_product_name.get_text(), 'Название продукта в результате поиска не соответствует ' \
                                                             'названию в карточке '


def test_check_open_product_card_attributes_1(web_browser):
    """ Проверка Карточки продукта
    Проверяем: выбор опций товара. """

    page = SearchMenu(web_browser)
    page_card = ProductCard(web_browser)

    page.search_searchMenu = '24915135'
    page.search_searchMenu_button.click()

    # Проверяем количество найденных товаров на странице
    assert page.search_products_titles_mini.count() > 0, 'Минимальное количество товаров не найдено'

    page.search_photo_mini_result.click()

    # Проверяем соответствие выбранного атрибута характеристикам
    assert page_card.search_product_400.get_text() == page_card.search_product_description.get_text(), \
        'Выбранная опция товара не соответствует описанию в характеристиках'


def test_check_open_product_card_attributes_2(web_browser):
    """ Проверка Карточки продукта
    Проверяем: выбор опций товара. """

    page = SearchMenu(web_browser)
    page_card = ProductCard(web_browser)

    page.search_searchMenu = '24915135'
    page.search_searchMenu_button.click()

    # Проверяем количество найденных товаров на странице
    assert page.search_products_titles_mini.count() > 0, 'Минимальное количество товаров не найдено'

    page.search_photo_mini_result.click()
    page_card.search_product_250.click()
    page.wait_page_loaded()
    # Проверяем соответствие выбранного атрибута характеристикам
    assert page_card.search_product_250_1.get_text() == page_card.search_product_description_1.get_text(), \
        'Выбранная опция товара не соответствует описанию в характеристиках'


