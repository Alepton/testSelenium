import time
from datetime import date
from selenium import webdriver
import chromedriver_binary
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome() # запускаем браузер Хром - запуск будет в режиме окна и все действия будут происходить в нем

# chromdriver должен быть таким же версии как и тот что на компе

browser.get('http://chio.proekt-sp.ru/lk_login.html')

input_login = browser.find_element(By.ID, "login")  # ищет значение поля по ID
input_login.send_keys("novopolochsk")               # заполняет логин novopolochsk

input_password = browser.find_element(By.ID, "pass")
input_password.send_keys("nk129675")                # заполняет пароль nk129675

# находим и кликаем по кнопке
login_button = browser.find_element(By.ID, "btLogin")
login_button.click()

# находим и кликаемна кнопку визиты моих клиентов
load_page = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="table_main_menu"]/tbody/tr[4]/th/div')))
load_page.click()

# находи  поле дата id = date
# WebDriverWait будет ждать пока не появиться соответсвующее поле
input_data = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "date")))  # ищет значение по ID
t = date.today()  # берет значение текущей даты в форомате 2022-08-25
print(t)
t = str(t) # преобразуем число в строку
today = f'{t[8]+t[9]}.{t[5]+t[6]}.{t[0]+t[1]+t[2]+t[3]}' # преобразуем дату к нужному формату 25.08.2022
print(today)
input_data.send_keys(today)                      # заполняет поле дата

# нажимаем кнопку получения данных с сервера
get_date = browser.find_element(By.ID, "btGetReport")   # ищет кнопку по значению по ID
get_date.click()                                        # нажимает кнопку получить данные

time.sleep(15) # открываем сайт на 15сек

browser.close() #закрываем сайт

