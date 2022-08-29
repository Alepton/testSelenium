import time
from datetime import date
from selenium import webdriver
import chromedriver_binary
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


# запускаем браузер Хром - запуск будет в режиме окна и все действия будут происходить в нем
# browser = webdriver.Chrome()

# 2-й вариант запускаем Хром в безоконном режиме (все работает точно накже, но в фоне мы ничего не видим)
chrome_options = Options()
chrome_options.add_argument("--headless") # включаем безоконный режим

browser = webdriver.Chrome(options=chrome_options)
browser.maximize_window()

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
#print(t)
t = str(t) # преобразуем число в строку
today = f'{t[8]+t[9]}.{t[5]+t[6]}.{t[0]+t[1]+t[2]+t[3]}' # преобразуем дату к нужному формату 25.08.2022
#print(today)
input_data.send_keys(today)                      # заполняет поле дата

# нажимаем кнопку получения данных с сервера
get_date = browser.find_element(By.ID, "btGetReport")   # ищет кнопку по значению по ID
get_date.click()                                        # нажимает кнопку получить данные

# счетчик количества услуг
tr_count = 0

# находим class odd и class even
tr_odd = WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "odd")))
for s in tr_odd:
    tr_count += 1

tr_even = WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "even")))
for s in tr_even:
    tr_count += 1

# поиск кодов услуг
# code_list = browser.find_elements(By.TAG_NAME, 'tr')
# for el in code_list:
#     print(el.text)

# функция расчета з/п
def salary(master_id):

    salary_massage = f'{today}\n'
    # счетчик зп
    salary_count = 0
    # перебираем все строки с услугами и делаем нужную выборку
    for i in range(3, tr_count + 3):
        cost = browser.find_element(By.XPATH, f'//*[@id="ReportTable"]/tbody/tr[{i}]/td[5]').text # td[5] - стоимость услуги
        code = browser.find_element(By.XPATH, f'//*[@id="ReportTable"]/tbody/tr[{i}]/td[6]').text  # td[6] - код услуги
        title = browser.find_element(By.XPATH, f'//*[@id="ReportTable"]/tbody/tr[{i}]/td[7]').text  # td[7] - наименование услуги
        name = browser.find_element(By.XPATH, f'//*[@id="ReportTable"]/tbody/tr[{i}]/td[8]').text  # td[8] - имя мастера
        date_time = browser.find_element(By.XPATH, f'//*[@id="ReportTable"]/tbody/tr[{i}]/td[11]').text  # td[11] - дата и время
        if code == "3307" or code == "2050" or code == "2395":
            continue
        elif master_id == name:
            if code == "26":
                salary = float(6)
            else:
                salary = float(cost) / 2
            salary_massage += f"{date_time[11:16]} {title} {cost}р з/п={salary}р\n"
            salary_count += salary
        else:
            continue

        #print(f"{date_time[11:16]} {title} {cost}р {name}")
    print(salary_massage)
    print(f'Итого з/п = {salary_count}р')

salary('Алеся')



print(tr_count)

time.sleep(5) # ждем 5сек

browser.close() #закрываем сайт


# td[6] – код услуги
# td[7] – наименование услуги
# td[8] – имя мастера
# td[11] – дата и время платежа


