# Test-design_OZON.ru_autotests
Данный проект содержит в себе автоматизированные тесты по проверке функционала сайта ozon.ru

Автотесты написанны на Python с использованием PyTest, Selenium и PageObject.

How to run:

1) Download driver for Chrome:
https://chromedriver.chromium.org/downloads

2) Install all required python packages library

3) Run in terminal with line:
python -m pytest -v --driver Chrome --driver-path <~>/chromedriver.exe tests/<enter the name of the file with autotests>.py


  Автотесты находятся в папке tests.
  
  Файл 01_tests_StartPage_links_01.py
  - содедржит в себе автотесты проверяющие корректность ссылок и переходов в меню стартовой страницы сайта;
  
  Файл 02_tests_StartPage_Search_Menu.py - содедржит в себе автотесты проверяющие функционал модуля поиска товаров и сортировку по типу товаров на сайте;
  
  Файл 03_test_Card_Product.py - содедржит в себе автотесты проверяющие функционал карточки товаров представленных на сайте;
 
  Файл 04_test_ProfileMenu_Favorites.py - содедржит в себе автотесты проверяющие функционал модуля 'Избранное' раздела меню профеля;
  
  Файл 05_tests_ProfileMenu_Cart.py - содедржит в себе автотесты проверяющие функционал модуля 'Корзина' раздела меню профеля;
  
  Файл 06_tests_ProfileMenu_LogIn.py - содедржит в себе автотесты проверяющие некоторый функционал модуля 'авторизации на сайте' раздела меню профеля;
  
  Файл ozon.py - содедржит в себе базу локаторов сайта используемых в автотестах данного проекта.
