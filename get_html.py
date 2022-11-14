from selenium import webdriver
import time
from selenium.webdriver.common.by import By

# Подключаем драйвер/указываем путь
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(executable_path="D:\Code\grin_2\chromedriver.exe")


def get_html(url):
    try:
        # Переходим по ссылке
        driver.get(url=url)
        time.sleep(2)

        # Ищем "капчу" (потверждение) и "Согласашаемся"
        new_id = driver.find_element(By.ID, "content_disclaimer")
        new_id.find_element(By.XPATH, "//*/div/div/div/div[1]/div/a[1]").click()
        time.sleep(2)

        # Проставляем нужные нам параметры
        # Начало месяца
        driver.find_element(By.ID, 'd1day').send_keys(3)
        time.sleep(1)
        driver.find_element(By.ID, 'd1day').send_keys(1)    

        # Конец месяца
        select_day = driver.find_element(By.ID, 'd2day')
        select_day.find_element(By.XPATH, '//*[@id="d2day"]/option[31]').click()
        driver.find_element(By.ID, 'd2day').send_keys(31)

        # Сам месяц
        driver.find_element(By.ID, 'd2month').send_keys('о')

        # Показываем таблицу
        driver.find_element(By.XPATH, '//*[@id="currency-rate-container"]/form/div[4]/div[2]/div/div[5]/input').click()
        time.sleep(2)

        # Сохраняем таблицу
        html = driver.page_source

        # Проставляем нужные нам параметры
        # Название валюты
        driver.find_element(By.ID, 'ctl00_PageContent_CurrencySelect').send_keys('j')
        time.sleep(2)

        # Начало месяца
        driver.find_element(By.ID, 'd1day').send_keys(3)
        time.sleep(2)
        driver.find_element(By.ID, 'd1day').send_keys(1)
    
        # Конец месяца
        select_day = driver.find_element(By.ID, 'd2day')
        select_day.find_element(By.XPATH, '//*[@id="d2day"]/option[31]').click()
        driver.find_element(By.ID, 'd2day').send_keys(31)

        # Сам месяц
        driver.find_element(By.ID, 'd2month').send_keys('о')
        time.sleep(2)

        # Показываем таблицу
        driver.find_element(By.XPATH, '//*[@id="currency-rate-container"]/form/div[4]/div[2]/div/div[5]/input').click()
        time.sleep(2)

        # Сохраняем таблицу
        html_2 = driver.page_source
        return html, html_2

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()