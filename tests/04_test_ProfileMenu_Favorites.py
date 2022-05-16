# How to run:
#  1) Download driver for Chrome:
#     https://chromedriver.chromium.org/downloads
#  2) Install all required python packages library
#
#  3) Run in terminal with line:
#     python -m pytest -v --driver Chrome --driver-path <~>/chromedriver.exe tests/04_test_ProfileMenu_Favorites.py


from pages.ozon import ProfileMenu, SearchMenu, ProductCard


def test_check_adding_products_to_favorites(web_browser):
    """ Проверка страницы Избранное
    Проверяем: добавление товара в избранное из карточки товаров. """

    page = SearchMenu(web_browser)
    page_card = ProductCard(web_browser)
    page_pf = ProfileMenu(web_browser)

    page.search_searchMenu = 'Скутер'
    page.search_searchMenu_button.click()

    # Проверяем количество найденных товаров на странице
    assert page.search_products_titles.count() > 0, 'Минимальное количество товаров не найдено'

    page.search_first_photo.scroll_to_element()
    page.search_first_photo.click()
    page_card.search_btn_favorites.click()
    page_pf.search_favorites.click()

    # Проверяем количество найденных товаров на странице
    assert page.search_products_titles_mini.count() > 0, 'Минимальное количество товаров не найдено'


def test_check_remove_item_from_favorites(web_browser):
    """ Проверка страницы Избранное
    Проверяем: удаление товар из избранное. """

    page = SearchMenu(web_browser)
    page_card = ProductCard(web_browser)
    page_pf = ProfileMenu(web_browser)

    page.search_searchMenu = 'Скутер'
    page.search_searchMenu_button.click()

    # Проверяем количество найденных товаров на странице
    assert page.search_products_titles.count() > 0, 'Минимальное количество товаров не найдено'

    page.search_first_photo.scroll_to_element()
    page.search_first_photo.click()
    page_card.search_btn_favorites.click()
    page_pf.search_favorites.click()
    page_card.search_btn_favorites_mini.click()
    page.refresh()

    # Проверяем количество найденных товаров на странице
    assert page.search_products_titles_mini.count() == 0, 'Товары остались в "листе" избранное'


def test_check_transition_from_favorites_to_card(web_browser):
    """ Проверка страницы Избранное
    Проверяем: переход из избранного в карточку товара. """

    page = SearchMenu(web_browser)
    page_card = ProductCard(web_browser)
    page_pf = ProfileMenu(web_browser)

    page.search_searchMenu = 'Скутер'
    page.search_searchMenu_button.click()

    # Проверяем количество найденных товаров на странице
    assert page.search_products_titles.count() > 0, 'Минимальное количество товаров не найдено'

    page.search_first_photo.scroll_to_element()
    page.search_first_photo.click()
    page_card.search_btn_favorites.click()
    page_pf.search_favorites.click()
    item = page.search_item_mini_result.get_text()
    page.search_photo_mini_result.click()

    # Проверяем соответствие названия продукта в 'избранное' и в карточке
    assert item == page_card.search_product_name.get_text(), 'Название продукта в "избранное" не соответствует ' \
                                                             'названию в карточке '


def test_check_adding_from_search_to_favorites(web_browser):
    """ Проверка страницы Избранное
    Проверяем: добавление товара из результата поиска в избранное. """

    page = SearchMenu(web_browser)
    page_card = ProductCard(web_browser)
    page_pf = ProfileMenu(web_browser)

    page.search_searchMenu = 'Скутер'
    page.search_searchMenu_button.click()

    # Проверяем количество найденных товаров на странице
    assert page.search_products_titles.count() > 0, 'Минимальное количество товаров не найдено'

    page.search_first_photo.scroll_to_element()
    page_card.search_btn_favorites_mini.click()
    page_pf.search_favorites.click()

    # Проверяем количество найденных товаров на странице
    assert page.search_products_titles_mini.count() > 0, 'Минимальное количество товаров не найдено'

