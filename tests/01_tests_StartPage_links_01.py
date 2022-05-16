# How to run:
#  1) Download driver for Chrome:
#     https://chromedriver.chromium.org/downloads
#  2) Install all required python packages library
#
#  3) Run in terminal with line:
#     python -m pytest -v --driver Chrome --driver-path <~>/chromedriver.exe tests/01_tests_StartPage_links_01.py


from pages.ozon import HeaderNavigation, ProfileMenu, HeaderHorizontalMenu, HeaderCatalog


def test_check_header_navigation_link_for_business(web_browser):
    """ Проверка корректности пути ссылки "Ozon для бизнеса" из header navigation. """

    page = HeaderNavigation(web_browser)

    page.search_ozone_for_business.click()

    # Проверяем ссылку на страницу 'Ozon для бизнеса'
    assert page.get_current_url() == 'https://www.ozon.ru/business/?perehod=header', \
        'Неверный путь страницы "Ozon для бизнеса"'


def test_check_header_navigation_link_mobile_app(web_browser):
    """ Проверка корректности пути ссылки "Мобильное приложение" из header navigation. """

    page = HeaderNavigation(web_browser)

    page.search_mobile_app.click()

    # Проверяем ссылку на страницу 'Мобильное приложение'
    assert page.get_current_url() == 'https://www.ozon.ru/info/appspromo/', \
        'Неверный путь страницы "Мобильное приложение"'


def test_check_header_navigation_link_sell_on_ozon(web_browser):
    """ Проверка корректности пути ссылки "Продавайте на Ozon" из header navigation. """

    page = HeaderNavigation(web_browser)

    page.search_sell_on_ozon.click()

    # Проверяем ссылку на страницу 'Продавайте на Ozon'
    assert page.get_current_url() == 'https://seller.ozon.ru/?utm_source=ozonru_web&utm_medium=link&utm_campaign' \
                                     '=header_nachat_prodavat_na_ozon%2F', \
        'Неверный путь страницы "Продавайте на Ozon"'


def test_check_header_navigation_link_make_money_with_ozon(web_browser):
    """ Проверка корректности пути ссылки "Зарабатывай с Ozon" из header navigation. """

    page = HeaderNavigation(web_browser)

    page.search_make_money_with_ozon.click()

    # Проверяем ссылку на страницу 'Зарабатывай с Ozon'
    assert page.get_current_url() == 'https://business.ozon.ru/?perehod=header', \
        'Неверный путь страницы "Зарабатывай с Ozon"'


def test_check_header_navigation_link_birth_certificates(web_browser):
    """ Проверка корректности пути ссылки "Подарочные сертификаты" из header navigation. """

    page = HeaderNavigation(web_browser)

    page.search_birth_certificates.click()

    # Проверяем ссылку на страницу 'Подарочные сертификаты'
    assert page.get_current_url()[0:109] == 'https://www.ozon.ru/product/elektronnyy-podarochnyy-sertifikat-million' \
                                            '-podarkov-135382627/?perehod=header&sh=', \
        'Неверный путь страницы "Подарочные сертификаты"'


def test_check_header_navigation_link_helpme(web_browser):
    """ Проверка корректности пути ссылки "Помощь" из header navigation. """

    page = HeaderNavigation(web_browser)

    page.search_helpme.click()

    # Проверяем ссылку на страницу 'Помощь'
    assert page.get_current_url() == 'https://docs.ozon.ru/common/', 'Неверный путь страницы "Помощь"'


def test_check_header_navigation_link_pick_up_points(web_browser):
    """ Проверка корректности пути ссылки "Пункты выдачи" из header navigation. """

    page = HeaderNavigation(web_browser)

    page.search_pick_up_points.click()

    # Проверяем ссылку на страницу 'Пункты выдачи'
    assert page.get_current_url()[0:24] == 'https://www.ozon.ru/geo/', 'Неверный путь страницы "Пункты выдачи"'


def test_check_link_login(web_browser):
    """ Проверка корректности пути ссылки "Войти" из блока "меню профиля". """

    page = ProfileMenu(web_browser)

    page.search_login.click()

    # Проверяем меню авторизации
    assert page.search_login_menu.find(), 'Ошибка, меню авторизации не найдено"'


def test_check_invitation_login(web_browser):
    """ Проверка всплывающего меню авторизации
    Проверяем: активацию всплывающего приглашения авторизации. """

    page_pf = ProfileMenu(web_browser)

    page_pf.search_login.right_mouse_click()

    # Проверяем активацию всплывающего меню
    assert page_pf.search_invitation_login.is_visible(), 'Всплывающее меню не активизировалось'


def test_check_link_orders(web_browser):
    """ Проверка корректности пути ссылки "Заказы" из блока "меню профиля". """

    page = ProfileMenu(web_browser)

    page.search_orders.click()

    # Проверяем ссылку на страницу 'Заказы'
    assert page.get_current_url() == 'https://www.ozon.ru/my/orderlist', 'Неверный путь страницы "Заказы"'


def test_check_link_favorites(web_browser):
    """ Проверка корректности пути ссылки "Избранное" из блока "меню профиля". """

    page = ProfileMenu(web_browser)

    page.search_favorites.click()

    # Проверяем ссылку на страницу 'Избранное'
    assert page.get_current_url() == "https://www.ozon.ru/my/favorites", 'Неверный путь страницы "Избранное"'


def test_check_link_cart(web_browser):
    """ Проверка корректности пути ссылки "Корзина" из блока "меню профиля". """

    page = ProfileMenu(web_browser)

    page.search_cart.click()

    # Проверяем ссылку на страницу 'Корзина'
    assert page.get_current_url() == "https://www.ozon.ru/cart", 'Неверный путь страницы "Корзина"'


def test_check_header_link_fashion(web_browser):
    """ Проверка корректности пути ссылки "TOP Fashion" из header "horizontalMenu". """

    page = HeaderHorizontalMenu(web_browser)

    page.search_fashion.click()

    # Проверяем ссылку на страницу 'TOP Fashion'
    assert page.get_current_url() == "https://www.ozon.ru/highlight/top-fashion/", 'Неверный путь страницы "TOP ' \
                                                                                   'Fashion" '


def test_check_header_link_premium(web_browser):
    """ Проверка корректности пути ссылки "Premium" из header "horizontalMenu". """

    page = HeaderHorizontalMenu(web_browser)

    page.search_premium.click()

    # Проверяем ссылку на страницу 'Premium'
    assert page.get_current_url() == "https://www.ozon.ru/highlight/premium/", 'Неверный путь страницы "Premium"'


def test_check_header_link_travel(web_browser):
    """ Проверка корректности пути ссылки "Ozon Travel" из header "horizontalMenu". """

    page = HeaderHorizontalMenu(web_browser)

    page.search_travel.click()

    # Проверяем ссылку на страницу 'Ozon Travel'
    assert page.get_current_url() == "https://www.ozon.ru/travel/?perehod=ozon_menu_header", \
        'Неверный путь страницы "Ozon Travel"'


def test_check_header_link_myCash(web_browser):
    """ Проверка корректности пути ссылки "Ozon Счет" из header "horizontalMenu". """

    page = HeaderHorizontalMenu(web_browser)

    page.search_myCash.click()

    # Проверяем ссылку на страницу 'Ozon Счет'
    assert page.get_current_url() == "https://finance.ozon.ru/?perehod=headernew", 'Неверный путь страницы "Ozon Счет"'


def test_check_header_link_live(web_browser):
    """ Проверка корректности пути ссылки "LIVE" из header "horizontalMenu". """

    page = HeaderHorizontalMenu(web_browser)

    page.search_live.click()

    # Проверяем ссылку на страницу 'LIVE'
    assert page.get_current_url() == "https://www.ozon.ru/live/", 'Неверный путь страницы "LIVE"'


def test_check_header_link_stock(web_browser):
    """ Проверка корректности пути ссылки "Акции" из header "horizontalMenu". """

    page = HeaderHorizontalMenu(web_browser)

    page.search_stock.click()

    # Проверяем ссылку на страницу 'Акции'
    assert page.get_current_url() == "https://www.ozon.ru/highlight/globalpromo/", 'Неверный путь страницы "Акции"'


def test_check_header_link_brands(web_browser):
    """ Проверка корректности пути ссылки "Бренды" из header "horizontalMenu". """

    page = HeaderHorizontalMenu(web_browser)

    page.search_brands.click()

    # Проверяем ссылку на страницу 'Бренды'
    assert page.get_current_url() == "https://www.ozon.ru/brand/", 'Неверный путь страницы "Бренды"'


def test_check_header_link_shops(web_browser):
    """ Проверка корректности пути ссылки "Магазины" из header "horizontalMenu". """

    page = HeaderHorizontalMenu(web_browser)

    page.search_shops.click()

    # Проверяем ссылку на страницу 'Магазины'
    assert page.get_current_url() == "https://www.ozon.ru/seller/", 'Неверный путь страницы "Магазины"'


def test_check_header_link_certificates(web_browser):
    """ Проверка корректности пути ссылки "Подарочные сертификаты" из header "horizontalMenu". """

    page = HeaderHorizontalMenu(web_browser)

    page.search_certificates.click()

    # Проверяем ссылку на страницу 'Подарочные сертификаты'
    assert page.get_current_url()[0:107] == 'https://www.ozon.ru/product/elektronnyy-podarochnyy-sertifikat-million' \
                                            '-podarkov-135382627/?perehod=menu&sh=', \
        'Неверный путь страницы "Подарочные сертификаты"'


def test_check_header_link_electronics(web_browser):
    """ Проверка корректности пути ссылки "Электроника" из header "horizontalMenu". """

    page = HeaderHorizontalMenu(web_browser)

    page.search_electronics.click()

    # Проверяем ссылку на страницу 'Электроника'
    assert page.get_current_url() == "https://www.ozon.ru/category/elektronika-15500/", 'Неверный путь страницы ' \
                                                                                        '"Электроника" '


def test_check_header_link_clothing(web_browser):
    """ Проверка корректности пути ссылки "Одежда и обувь" из header "horizontalMenu". """

    page = HeaderHorizontalMenu(web_browser)

    page.search_clothing.click()

    # Проверяем ссылку на страницу 'Одежда и обувь'
    assert page.get_current_url() == "https://www.ozon.ru/category/zhenskaya-odezhda-7501/", 'Неверный путь страницы ' \
                                                                                             '"Одежда и обувь" '


def test_check_header_link_child_products(web_browser):
    """ Проверка корректности пути ссылки "Детские товары" из header "horizontalMenu". """

    page = HeaderHorizontalMenu(web_browser)

    page.search_child_products.click()

    # Проверяем ссылку на страницу 'Детские товары'
    assert page.get_current_url() == "https://www.ozon.ru/category/detskie-tovary-7000/", 'Неверный путь страницы ' \
                                                                                          '"Детские товары" '


def test_check_header_link_child_house_and_garden(web_browser):
    """ Проверка корректности пути ссылки "Дом и сад" из header "horizontalMenu". """

    page = HeaderHorizontalMenu(web_browser)

    page.search_house_and_garden.click()

    # Проверяем ссылку на страницу 'Дом и сад'
    assert page.get_current_url() == "https://www.ozon.ru/category/dom-i-sad-14500/", 'Неверный путь страницы ' \
                                                                                      '"Дом и сад" '


def test_check_header_link_child_best_price(web_browser):
    """ Проверка корректности пути ссылки "Зона лучших цен" из header "horizontalMenu". """

    page = HeaderHorizontalMenu(web_browser)

    page.search_best_price.click()

    # Проверяем ссылку на страницу 'Зона лучших цен'
    assert page.get_current_url() == "https://www.ozon.ru/highlight/zona-luchshih-tsen-273550/", \
        'Неверный путь страницы "Зона лучших цен"'


def test_check_header_catalog_links(web_browser):
    """ Проверка возможности 'клика' на основные категории в меню 'Каталог'. """

    page = HeaderCatalog(web_browser)

    # Проверяем активацию меню каталога
    page.search_button_all_categories.click()
    assert page.search_menu_categories.is_visible(), 'Ошибка, меню каталога не в поле видимости"'

    # Проверяем возможность клика на категорию продукта
    assert page.search_menu_electronics.is_clickable(), 'Категория "Электроника" не доступна для клика'
    assert page.search_menu_clothes.is_clickable(), 'Категория "Одежда" не доступна для клика'
    assert page.search_menu_shoes.is_clickable(), 'Категория "Обувь" не доступна для клика'
    assert page.search_menu_house_and_garden.is_clickable(), 'Категория "Дом и сад" не доступна для клика'
    assert page.search_menu_child_products.is_clickable(), 'Категория "Детские товары" не доступна для клика'
    assert page.search_menu_beauty_and_health.is_clickable(), 'Категория "Красота и здоровье" не доступна для клика'
    assert page.search_menu_appliances.is_clickable(), 'Категория "Бытовая техника" не доступна для клика'
    assert page.search_menu_sports_and_recreation.is_clickable(), 'Категория "Спорт и отдых" не доступна для клика'
    assert page.search_menu_construction_and_repair.is_clickable(), 'Категория "Строительство и ремонт" не доступна ' \
                                                                    'для клика '
    assert page.search_menu_food.is_clickable(), 'Категория "Аптека" не доступна для клика'
    assert page.search_menu_pharmacy.is_clickable(), 'Категория "Продукты питания" не доступна для клика'
    assert page.search_menu_goods_or_pets.is_clickable(), 'Категория "Товары для животных" не доступна для клика'
    assert page.search_menu_books.is_clickable(), 'Категория "Книги" не доступна для клика'
    assert page.search_menu_tourism.is_clickable(), 'Категория "Туризм рыбалка охота" не доступна для клика'
    assert page.search_menu_auto_products.is_clickable(), 'Категория "Автотовары" не доступна для клика'
    assert page.search_menu_furniture.is_clickable(), 'Категория "Мебель" не доступна для клика'
    assert page.search_menu_hobby.is_clickable(), 'Категория "Хобби и творчество" не доступна для клика'
    assert page.search_menu_jewelry.is_clickable(), 'Категория "Ювелирные украшения" не доступна для клика'
    assert page.search_menu_accessories.is_clickable(), 'Категория "Аксессуары" не доступна для клика'
    assert page.search_menu_games.is_clickable(), 'Категория "Игры" не доступна для клика'
    assert page.search_menu_stationery.is_clickable(), 'Категория "Канцелярские товары" не доступна для клика'
    assert page.search_menu_for_adults.is_clickable(), 'Категория "Товары для взрослых" не доступна для клика'
    assert page.search_menu_antiques.is_clickable(), 'Категория "Антиквариат и коллекционирование" не доступна для ' \
                                                     'клика '
    assert page.search_menu_digital_goods.is_clickable(), 'Категория "Цифровые товары" не доступна для клика'
    assert page.search_menu_household_chemicals.is_clickable(), 'Категория "Бытовая химия и гигиена" не доступна для ' \
                                                                'клика '
    assert page.search_menu_music.is_clickable(), 'Категория "Музыка и видео" не доступна для клика'
    assert page.search_menu_cars.is_clickable(), 'Категория "Автомобили и мототехника" не доступна для клика'
    assert page.search_menu_cigarettes.is_clickable(), 'Категория "Электронные сигареты и товары для курения" не ' \
                                                       'доступна для клика '
    assert page.search_menu_discounted_goods.is_clickable(), 'Категория "Уценённые товары" не доступна для клика'

