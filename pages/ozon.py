import os
from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class StartPage(WebPage):
    """ Базовый класс стартовой страницы Ozon. """

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://ozon.ru/'

        super().__init__(web_driver, url)


class HeaderNavigation(StartPage):
    """ Наследуемый класс StartPage
    Локаторы ссылок из блока header navigation. """

    # Ищем ссылку на страницу 'Ozon для бизнеса'
    search_ozone_for_business = WebElement(xpath='//a[@href="/business/?perehod=header"]')

    # Ищем ссылку на страницу 'Мобильное приложение'
    search_mobile_app = WebElement(xpath='//a[@href="/info/appspromo/"]')

    # Ищем ссылку на страницу 'Продавайте на Ozon'
    search_sell_on_ozon = WebElement(xpath='//a[@href="https://seller.ozon.ru/?utm_source=ozonru_web&utm_medium=link'
                                           '&utm_campaign=header_nachat_prodavat_na_ozon/"]')

    # Ищем ссылку на страницу 'Зарабатывай с Ozon'
    search_make_money_with_ozon = WebElement(xpath='//a[@href="//business.ozon.ru/?perehod=header"]')

    # Ищем ссылку на страницу 'Подарочные сертификаты'
    search_birth_certificates = WebElement(xpath='//a[@href="/context/detail/id/135382627/?perehod=header"]')

    # Ищем ссылку на страницу 'Помощь'
    search_helpme = WebElement(xpath='//a[@href="//docs.ozon.ru/common/"]')

    # Ищем ссылку на страницу 'Пункты выдачи'
    search_pick_up_points = WebElement(xpath='//a[@href="/info/map/"]')


class ProfileMenu(StartPage):
    """ Наследуемый класс StartPage
    Локаторы ссылок из блока "меню профиля". """

    # Ищем активацию меню авторизации
    search_login = WebElement(xpath='//div[@class="gu7 k0c ba4j"]')

    # Ищем меню авторизации
    search_login_menu = WebElement(xpath='//div[@data-widget="ozonIdIframe"]')

    # Ищем всплывающее меню авторизации
    search_invitation_login = WebElement(xpath='//div[@class="ui-k ui-k7 ui-k9 ui-k0"]')

    # Ищем ссылку на страницу 'Заказы'
    search_orders = WebElement(xpath='//a[@href="/my/orderlist"]')

    # Ищем ссылку на страницу 'Избранное'
    search_favorites = WebElement(xpath='//a[@href="/my/favorites"]')

    # Ищем ссылку на страницу 'Корзина'
    search_cart = WebElement(xpath='//a[@href="/cart"]')


class HeaderHorizontalMenu(StartPage):
    """ Наследуемый класс StartPage
    Локаторы ссылок из блока header "horizontalMenu". """

    # Ищем ссылку на страницу 'TOP Fashion'
    search_fashion = WebElement(xpath='//a[@href="/highlight/top-fashion/"]')

    # Ищем ссылку на страницу 'Premium'
    search_premium = WebElement(xpath='//li/a[@href="/highlight/premium/"]')

    # Ищем ссылку на страницу 'Ozon Travel'
    search_travel = WebElement(xpath='//a[@href="https://www.ozon.ru/travel?perehod=ozon_menu_header"]')

    # Ищем ссылку на страницу 'Ozon Счет'
    search_myCash = WebElement(xpath='//a[@href="https://finance.ozon.ru/?perehod=headernew"]')

    # Ищем ссылку на страницу 'LIVE'
    search_live = WebElement(xpath='//a[@href="/live/"]')

    # Ищем ссылку на страницу 'Акции'
    search_stock = WebElement(xpath='//a[@href="/highlight/globalpromo/"]')

    # Ищем ссылку на страницу 'Бренды'
    search_brands = WebElement(xpath='//a[@href="/brand/"]')

    # Ищем ссылку на страницу 'Магазины'
    search_shops = WebElement(xpath='//a[@href="/seller/"]')

    # Ищем ссылку на страницу 'Сертификаты'
    search_certificates = WebElement(xpath='//a[@href="/context/detail/id/135382627/?perehod=menu"]')

    # Ищем ссылку на страницу 'Электроника'
    search_electronics = WebElement(xpath='//li/a[@href="/category/elektronika-15500/"]')

    # Ищем ссылку на страницу 'Одежда и обувь'
    search_clothing = WebElement(xpath='//a[@href="/category/zhenskaya-odezhda-7501/"]')

    # Ищем ссылку на страницу 'Детские товары'
    search_child_products = WebElement(xpath='//li/a[@href="/category/detskie-tovary-7000/"]')

    # Ищем ссылку на страницу 'Дом и сад'
    search_house_and_garden = WebElement(xpath='//li/a[@href="/category/dom-i-sad-14500/"]')

    # Ищем ссылку на страницу 'Зона лучших цен'
    search_best_price = WebElement(xpath='//li/a[@href="/highlight/zona-luchshih-tsen-273550/"]')


class HeaderCatalog(StartPage):
    """ Наследуемый класс StartPage
    Локаторы ссылок из блока header "Каталог". """

    # Ищем кнопку 'Каталог'
    search_button_all_categories = WebElement(xpath='//span[@class="ui-c4 ui-c6"]')

    # Ищем меню каталога
    search_menu_categories = WebElement(xpath='//div[@class="ec6"]')

    # Ищем категорию 'Электроника'
    search_menu_electronics = WebElement(xpath='//div/a[@href="/category/elektronika-15500/"]')

    # Ищем категорию 'Одежда'
    search_menu_clothes = WebElement(xpath='//a[@href="/category/odezhda-obuv-i-aksessuary-7500/"]')

    # Ищем категорию 'Обувь'
    search_menu_shoes = WebElement(xpath='//a[@href="/category/obuv-17777/"]')

    # Ищем категорию 'Дом и сад'
    search_menu_house_and_garden = WebElement(xpath='//a[@href="/category/dom-i-sad-14500/"]')

    # Ищем категорию 'Детские товары'
    search_menu_child_products = WebElement(xpath='//a[@href="/category/detskie-tovary-7000/"]')

    # Ищем категорию 'Красота и здоровье'
    search_menu_beauty_and_health = WebElement(xpath='//a[@href="/category/krasota-i-zdorove-6500/"]')

    # Ищем категорию 'Бытовая техника'
    search_menu_appliances = WebElement(xpath='//a[@href="/category/bytovaya-tehnika-10500/"]')

    # Ищем категорию 'Спорт и отдых'
    search_menu_sports_and_recreation = WebElement(xpath='//a[@href = "/category/sport-i-otdyh-11000/"]')

    # Ищем категорию 'Строительство и ремонт'
    search_menu_construction_and_repair = WebElement(xpath='//a[@href="/category/stroitelstvo-i-remont-9700/"]')

    # Ищем категорию 'Продукты питания'
    search_menu_food = WebElement(xpath='//a[@href="/category/produkty-pitaniya-9200/"]')

    # Ищем категорию 'Аптека'
    search_menu_pharmacy = WebElement(xpath='//a[@href="/category/apteka-6000/"]')

    # Ищем категорию 'Товары для животных'
    search_menu_goods_or_pets = WebElement(xpath='//a[@href="/category/tovary-dlya-zhivotnyh-12300/"]')

    # Ищем категорию 'Книги'
    search_menu_books = WebElement(xpath='//a[@href="/category/knigi-16500/"]')

    # Ищем категорию 'Туризм рыбалка охота'
    search_menu_tourism = WebElement(xpath='//a[@href="/category/ohota-rybalka-turizm-33332/"]')

    # Ищем категорию 'Автотовары'
    search_menu_auto_products = WebElement(xpath='//a[@href="/category/avtotovary-8500/"]')

    # Ищем категорию 'Мебель'
    search_menu_furniture = WebElement(xpath='//a[@href="/category/mebel-15000/"]')

    # Ищем категорию 'Хобби и творчество'
    search_menu_hobby = WebElement(xpath='//a[@href="/category/hobbi-i-tvorchestvo-13500/"]')

    # Ищем категорию 'Ювелирные украшения'
    search_menu_jewelry = WebElement(xpath='//a[@href="/category/yuvelirnye-ukrasheniya-50001/"]')

    # Ищем категорию 'Аксессуары'
    search_menu_accessories = WebElement(xpath='//a[@href="/category/aksessuary-7697/"]')

    # Ищем категорию 'Игры'
    search_menu_games = WebElement(xpath='//a[@href="/category/igry-i-soft-13300/"]')

    # Ищем категорию 'Канцелярские товары'
    search_menu_stationery = WebElement(xpath='//a[@href="/category/kantselyarskie-tovary-18000/"]')

    # Ищем категорию 'Товары для взрослых'
    search_menu_for_adults = WebElement(xpath='//a[@href="/category/tovary-dlya-vzroslyh-9000/"]')

    # Ищем категорию 'Антиквариат и коллекционирование'
    search_menu_antiques = WebElement(xpath='//a[@href="/category/antikvariat-vintazh-iskusstvo-8000/"]')

    # Ищем категорию 'Цифровые товары'
    search_menu_digital_goods = WebElement(xpath='//a[@href="/category/tsifrovye-tovary-32056/"]')

    # Ищем категорию 'Бытовая химия и гигиена'
    search_menu_household_chemicals = WebElement(xpath='//a[@href="/category/bytovaya-himiya-14572/"]')

    # Ищем категорию 'Музыка и видео'
    search_menu_music = WebElement(xpath='//a[@href="/category/muzyka-i-video-13100/"]')

    # Ищем категорию 'Автомобили и мототехника'
    search_menu_cars = WebElement(xpath='//a[@href="/category/avtomobili-i-mototsikly-34452/"]')

    # Ищем категорию 'Электронные сигареты и товары для курения'
    search_menu_cigarettes = WebElement(xpath='//a[@href="/category/elektronnye-sigarety-i-tovary-dlya-kureniya-35659'
                                              '/"]')

    # Ищем категорию 'Уценённые товары'
    search_menu_discounted_goods = WebElement(xpath='//a[@href="/category/utsenennye-tovary-77777/"]')


class SearchMenu(StartPage):
    """ Наследуемый класс StartPage
    Локаторы меню поиска. """

    # Ищем поле поиска товаров
    search_searchMenu = WebElement(xpath='//input[@placeholder="Искать на Ozon"]')

    # Ищем кнопку поиска
    search_searchMenu_button = WebElement(xpath='//form[@action="/search"]/button')

    # Ищем товары в результате поиска
    search_products_titles = ManyWebElements(xpath='//div[@class="s1i"]/a[@href!=""]')

    # Ищем товары в результате поиска мини таблицы
    search_products_titles_mini = ManyWebElements(xpath='//div[@class="ui3"]/div/a[@href!=""]')

    # Ищем подкатегорию "По типу" "Электровелосипед"
    search_products_sort_type = WebElement(xpath='//span[@href="/category/velosipedy-11002/?from_global=true&text=%D0'
                                                 '%B2%D0%B5%D0%BB%D0%BE%D1%81%D0%B8%D0%BF%D0%B5%D0%B4&type=58050"]')

    # Ищем подкатегорию "Бренды" "Stels"
    search_products_sort_brands = WebElement(xpath='//a[@href="/category/velosipedy-11002/?from_global=true&text=%D0'
                                                   '%B2%D0%B5%D0%BB%D0%BE%D1%81%D0%B8%D0%BF%D0%B5%D0%B4&brand'
                                                   '=146704364"]')

    # Ищем поле ввода номера страницы
    search_page_input = WebElement(xpath='//input[@class="ui-h5 ui-h7"]')

    # Ищем кнопку "Перейти"
    search_go_button = WebElement(xpath='//span/span[@class="ui-g0" and contains(text(), "Перейти")]')

    # Ищем страницу "50"
    search_page_50 = WebElement(xpath='//div/a[@href!="" and contains(text(), "50")]')

    # Ищем название первого товара в поиске
    search_first_item = WebElement(xpath='//div[@class="s1i"]/a[@href!=""]')

    # Ищем фото первого товара в поиске
    search_first_photo = WebElement(xpath='//div[@class="iq8 i8q"]/img[@src!=""]')

    # Ищем фото второго товара в поиске
    search_second_photo = WebElement(xpath='//div[@class="i0s si0"][2]//div[@class="iq8 i8q"]/img[@src!=""]')

    # Ищем фото первого товара в результатах мини таблицы
    search_photo_mini_result = WebElement(xpath='//div[@class="ir9 r9i"]/a[@href!=""]')

    # Ищем название первого товара в результатах мини таблицы
    search_item_mini_result = WebElement(xpath='//div[@class="si"]/a/span/span')

    # Ищем кнопку 'В корзину 'в результатах поиска
    search_btn_cart_result = WebElement(xpath='//div[@class="vc7 c8v r3i"]//button[@class="ui-c3"]')


class ProductCard(StartPage):
    """ Наследуемый класс StartPage
    Локаторы карточки продукта. """

    # Ищем название продукта
    search_product_name = WebElement(xpath='//h1[@class="nl7"]')

    # Ищем Код товара в карточке
    search_product_kode = WebElement(xpath='//span[@class="k6s s6k"]')

    # Ищем атрибут товара 'объем 400'
    search_product_400 = WebElement(xpath='//div[3]/div[2]/div[2]/div[1]/button[1]')

    # Ищем атрибут товара 'объем 250'
    search_product_250 = WebElement(xpath='//div[3]/div[2]/div[1]/div/button')
    search_product_250_1 = WebElement(xpath='//div[4]/div[2]/div[1]/div/button')

    # Ищем характеристики товара 'объем'
    search_product_description = WebElement(xpath='//div[2]/div[1]/div[2]/div[1]/div[1]/dl[4]/dd[1]')
    search_product_description_1 = WebElement(xpath='//div[@class="x5j"]/dl[4]/dd')

    # Ищем пункт "В избранное"
    search_btn_favorites = WebElement(xpath='//div[@class="qj ui-c1"]')

    # Ищем пункт "В избранное" в миниатюре товара
    search_btn_favorites_mini = WebElement(xpath='//div[@class="ui-j8 si3"]')

    # Ищем кнопку 'Добавить в корзину'
    search_btn_cart = WebElement(xpath='//div[@class="ui-c1 ui-g8"]/button[@class="ui-c3 ui-g8"]')


class Cart(StartPage):
    """ Наследуемый класс StartPage
    Локаторы страницы корзина. """

    # Ищем товары в корзине
    search_products_cart = ManyWebElements(xpath='//div[@class="an9"]')

    # Ищем название товара в корзине
    search_title_product_in_cart = ManyWebElements(xpath='//a[@class="tsBodyM o8a"]/span[1]')

    # Ищем пункт 'Удалить' в корзине
    search_del_in_cart_1 = WebElement(xpath='//div[@class="an1 ui-c1"][2]/button[@class="ui-c3"]')

    # Ищем кнопку 'Удалить' в корзине
    search_del_in_cart_2 = WebElement(xpath='//div[@class="a7m ui-c1"]/button[@class="ui-c3"]')

    # Ищем стоимость товаров в корзине
    search_cost_of_goods = ManyWebElements(xpath='//span[@class="d8e e8d d0f tsBodyLBold n4a"]')

    # Ищем итоговою сумму в корзине
    search_basket_cart = WebElement(xpath='//div[@class="at8"]/span[2]')


class LogIn(StartPage):
    """ Наследуемый класс StartPage
    Локаторы страницы 'Ozon ID'. """

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://www.ozon.ru/ozonid'

        super().__init__(web_driver, url)

    # Ищем поле ввода номера телефона
    search_phone = WebElement(xpath='//input[@type="phone"]')

    # Ищем приглашение ввода проверочного кода
    search_security_code = WebElement(xpath='//div[@class="b8ha"]')

    # Ищем кнопку войти
    search_btn_login = WebElement(xpath='//div[@class="bah7 ui-c1 ui-g8"]/button')
