# How to run:
#  1) Download driver for Chrome:
#     https://chromedriver.chromium.org/downloads
#  2) Install all required python packages library
#
#  3) Run in terminal with line:
#     python -m pytest -v --driver Chrome --driver-path <~>/chromedriver.exe tests/05_tests_ProfileMenu_Cart.py


from pages.ozon import ProfileMenu, SearchMenu, ProductCard, Cart


def test_check_adding_product_to_cart_in_card(web_browser):
    """ Проверка страницы Корзина
    Проверяем: добавление товара в корзину из карточки товара. """

    page = SearchMenu(web_browser)
    page_card = ProductCard(web_browser)
    page_pf = ProfileMenu(web_browser)
    page_cart = Cart(web_browser)

    page.search_searchMenu = 'Скутер'
    page.search_searchMenu_button.click()

    # Проверяем количество найденных товаров на странице
    assert page.search_products_titles.count() > 0, 'Минимальное количество товаров не найдено'

    page.search_first_photo.scroll_to_element()
    page.search_first_photo.click()
    page_card.search_btn_cart.click()
    page_pf.search_cart.click()
    page.refresh()

    # Проверяем количество найденных товаров в корзине
    assert page_cart.search_products_cart.count() == 1, 'Минимальное количество товаров не найдено'


def test_check_adding_some_products_to_cart(web_browser):
    """ Проверка страницы Корзина
    Проверяем: добавление нескольких товаров в корзину из карточки товара. """

    page = SearchMenu(web_browser)
    page_card = ProductCard(web_browser)
    page_pf = ProfileMenu(web_browser)
    page_cart = Cart(web_browser)

    page.search_searchMenu = 'Скутер'
    page.search_searchMenu_button.click()

    # Проверяем количество найденных товаров на странице
    assert page.search_products_titles.count() > 0, 'Минимальное количество товаров не найдено'

    page.search_first_photo.scroll_to_element()
    page.search_first_photo.click()
    page_card.search_btn_cart.click()
    page.go_back()
    page.search_second_photo.scroll_to_element()
    page.search_second_photo.click()
    page_card.search_btn_cart.click()
    page_pf.search_cart.click()
    page.refresh()

    # Проверяем количество найденных товаров в корзине
    assert page_cart.search_products_cart.count() == 2, 'Минимальное количество товаров не найдено'


def test_check_adding_product_to_cart_2(web_browser):
    """ Проверка страницы Корзина
    Проверяем: добавление товара в корзину из результата поиска. """

    page = SearchMenu(web_browser)
    page_pf = ProfileMenu(web_browser)
    page_cart = Cart(web_browser)

    page.search_searchMenu = 'Скутер'
    page.search_searchMenu_button.click()

    # Проверяем количество найденных товаров на странице
    assert page.search_products_titles.count() > 0, 'Минимальное количество товаров не найдено'

    page.search_first_photo.scroll_to_element()
    page.search_btn_cart_result.click()
    page_pf.search_cart.click()
    page.refresh()

    # Проверяем количество найденных товаров в корзине
    assert page_cart.search_products_cart.count() == 1, 'Минимальное количество товаров не найдено'


def test_check_adding_product_to_cart_3(web_browser):
    """ Проверка страницы Корзина
    Проверяем: добавление товара в корзину и проверка его валидности. """

    page = SearchMenu(web_browser)
    page_card = ProductCard(web_browser)
    page_pf = ProfileMenu(web_browser)
    page_cart = Cart(web_browser)

    page.search_searchMenu = 'Скутер'
    page.search_searchMenu_button.click()

    # Проверяем количество найденных товаров на странице
    assert page.search_products_titles.count() > 0, 'Минимальное количество товаров не найдено'

    page.search_first_photo.scroll_to_element()
    page.search_first_photo.click()
    page_card.search_btn_cart.click()
    title = page_card.search_product_name.get_text()
    page_pf.search_cart.click()
    page.refresh()

    # Проверяем название товара в карточке товара и в корзине
    assert title == page_cart.search_title_product_in_cart.get_text()[0], 'Название товара в карточке товара и в ' \
                                                                          'корзине не совпадают'


def test_check_del_product_in_cart(web_browser):
    """ Проверка страницы Корзина
    Проверяем: удаление товара из корзины. """

    page = SearchMenu(web_browser)
    page_pf = ProfileMenu(web_browser)
    page_cart = Cart(web_browser)

    page.search_searchMenu = 'Скутер'
    page.search_searchMenu_button.click()

    # Проверяем количество найденных товаров на странице
    assert page.search_products_titles.count() > 0, 'Минимальное количество товаров не найдено'

    page.search_first_photo.scroll_to_element()
    page.search_btn_cart_result.click()
    page_pf.search_cart.click()
    page.refresh()

    # Проверяем количество найденных товаров в корзине до удаления
    assert page_cart.search_products_cart.count() == 1, 'Минимальное количество товаров не найдено'

    page_cart.search_del_in_cart_1.click()
    page_cart.search_del_in_cart_2.click()
    page.wait_page_loaded()

    # Проверяем количество найденных товаров на странице после удаления
    assert page_cart.search_products_cart.count() == 0, 'В корзине остался товар'


def test_check_cart_amount(web_browser):
    """ Проверка страницы Корзина
    Проверяем: сумму товаров и общую сумму в корзине. """

    page = SearchMenu(web_browser)
    page_card = ProductCard(web_browser)
    page_pf = ProfileMenu(web_browser)
    page_cart = Cart(web_browser)

    page.search_searchMenu = 'Скутер'
    page.search_searchMenu_button.click()

    # Проверяем количество найденных товаров на странице
    assert page.search_products_titles.count() > 0, 'Минимальное количество товаров не найдено'

    page.search_first_photo.scroll_to_element()
    page.search_first_photo.click()
    page_card.search_btn_cart.click()
    page.go_back()
    page.search_second_photo.scroll_to_element()
    page.search_second_photo.click()
    page_card.search_btn_cart.click()
    page_pf.search_cart.click()
    page.refresh()

    # Извлекаем сумму каждого товара
    price_1 = []
    for i in page_cart.search_cost_of_goods.get_text()[0]:
        if i.isnumeric():
            price_1.append(int(i))

    price_2 = []
    for i in page_cart.search_cost_of_goods.get_text()[1]:
        if i.isnumeric():
            price_2.append(int(i))

    # Извлекаем общую сумму корзины
    price_cart = []
    for i in page_cart.search_basket_cart.get_text():
        if i.isnumeric():
            price_cart.append(int(i))

    # Сравниваем сумму продуктов и общую сумму корзины
    assert int(''.join(map(str, price_1))) + int(''.join(map(str, price_2))) == int(''.join(map(str, price_cart))), \
        'Сумма товаров не соответствует сумме корзины'

