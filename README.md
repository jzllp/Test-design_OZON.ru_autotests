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
  
