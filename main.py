import time
from datetime import date
from selenium import webdriver
import chromedriver_binary
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import telebot
from telebot import types
import os

bot = telebot.TeleBot('5669254611:AAH3HMo0swKrZHwjYUIegUFcND0o7wC1L0I')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    btn1 = types.KeyboardButton('Алеся')
    btn2 = types.KeyboardButton('Даша')
    btn3 = types.KeyboardButton('Виктория')
    btn4 = types.KeyboardButton('Мартина')
    btn5 = types.KeyboardButton('Ольга')
    btn6 = types.KeyboardButton('Наталья')
    btn7 = types.KeyboardButton('Анастасия')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
    send_mess = f"<b>Привет {message.from_user.first_name} {message.from_user.last_name}</b>\nЯ помогу вам посмотреть ваши стрижки за сегодня\nВыберите имя мастера?"
    bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)



@bot.message_handler(content_types=['text'])
def mess(message):
    get_message_bot = message.text.strip()


    def final_message(master_name):
        bot.send_message(message.chat.id, 'Получаю данные с сервера, это может занять несколько минут, пожалуйста подождите...', parse_mode='html')
        bot.send_message(message.chat.id, salary(master_name), parse_mode='html')

    if get_message_bot == 'Алеся':
        final_message('Алеся')

    elif get_message_bot == 'Даша':
        master_name = 'Даша'
        bot.send_message(message.chat.id, 'Получаю данные с сервера, пожалуйста подождите...', parse_mode='html')
        bot.send_message(message.chat.id, salary(master_name), parse_mode='html')
    elif get_message_bot == 'Виктория':
        master_name = 'Виктория'
        bot.send_message(message.chat.id, 'Получаю данные с сервера, пожалуйста подождите...', parse_mode='html')
        bot.send_message(message.chat.id, salary(master_name), parse_mode='html')
    elif get_message_bot == 'Мартина':
        master_name = 'Мартина'
        bot.send_message(message.chat.id, 'Получаю данные с сервера, пожалуйста подождите...', parse_mode='html')
        bot.send_message(message.chat.id, salary(master_name), parse_mode='html')
    elif get_message_bot == 'Ольга':
        master_name = 'Ольга'
        bot.send_message(message.chat.id, 'Получаю данные с сервера, пожалуйста подождите...', parse_mode='html')
        bot.send_message(message.chat.id, salary(master_name), parse_mode='html')
    elif get_message_bot == 'Наталья':
        master_name = 'Наталья'
        bot.send_message(message.chat.id, 'Получаю данные с сервера, пожалуйста подождите...', parse_mode='html')
        bot.send_message(message.chat.id, salary(master_name), parse_mode='html')
    elif get_message_bot == 'Анастасия':
        master_name = 'Анастасия'
        bot.send_message(message.chat.id, 'Получаю данные с сервера, пожалуйста подождите...', parse_mode='html')
        bot.send_message(message.chat.id, salary(master_name), parse_mode='html')
    else:
        bot.send_message(message.chat.id, 'Что-то пошло не так) Выберите имя мастера, нажав кнопку ниже', parse_mode='html')
    bot.send_message('657253505', f"{message.from_user.first_name} {message.from_user.last_name} chat_id: {message.chat.id}", parse_mode='html')
# функция расчета з/п
def salary(master_id):
    # запускаем браузер Хром - запуск будет в режиме окна и все действия будут происходить в нем
    #driver = webdriver.Chrome()

    # 2-й вариант запускаем Хром в безоконном режиме (все работает точно накже, но в фоне мы ничего не видим)
    # chrome_options = Options()
    # chrome_options.add_argument("--headless") # включаем безоконный режим
    # driver = webdriver.Chrome(options=chrome_options)
    # driver.maximize_window()

    # 3-й вариант код для запуска на heroku
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    driver.maximize_window()


    # chromdriver должен быть таким же версии как и тот что на компе

    driver.get('http://chio.proekt-sp.ru/lk_login.html')

    input_login = driver.find_element(By.ID, "login")  # ищет значение поля по ID
    input_login.send_keys("novopolochsk")               # заполняет логин novopolochsk

    input_password = driver.find_element(By.ID, "pass")
    input_password.send_keys("nk129675")                # заполняет пароль nk129675

    # находим и кликаем по кнопке
    login_button = driver.find_element(By.ID, "btLogin")
    login_button.click()

    # находим и кликаемна кнопку визиты моих клиентов
    load_page = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="table_main_menu"]/tbody/tr[4]/th/div')))
    load_page.click()

    # находи  поле дата id = date
    # WebDriverWait будет ждать пока не появиться соответсвующее поле
    input_data = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "date")))  # ищет значение по ID
    t = date.today()  # берет значение текущей даты в форомате 2022-08-25
    #print(t)
    t = str(t) # преобразуем число в строку
    today = f'{t[8]+t[9]}.{t[5]+t[6]}.{t[0]+t[1]+t[2]+t[3]}' # преобразуем дату к нужному формату 25.08.2022
    #print(today)

    input_data.send_keys(today)                      # заполняет поле дата
    time.sleep(1)  # ждем 1сек

    # нажимаем кнопку получения данных с сервера
    get_date = driver.find_element(By.ID, "btGetReport")   # ищет кнопку по значению по ID
    get_date.click()                                        # нажимает кнопку получить данные

    # счетчик количества услуг
    tr_count = 0

    # находим class odd и class even
    tr_odd = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "odd")))
    for s in tr_odd:
        tr_count += 1

    tr_even = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "even")))
    for s in tr_even:
        tr_count += 1

    # поиск кодов услуг
    # code_list = browser.find_elements(By.TAG_NAME, 'tr')
    # for el in code_list:
    #     print(el.text)

    # итоговое сообщение
    salary_massage = f'{today}\n'
    # счетчик зп
    salary_count = 0
    # перебираем все строки с услугами и делаем нужную выборку
    for i in range(3, tr_count + 3):
        cost = driver.find_element(By.XPATH, f'//*[@id="ReportTable"]/tbody/tr[{i}]/td[5]').text # td[5] - стоимость услуги
        code = driver.find_element(By.XPATH, f'//*[@id="ReportTable"]/tbody/tr[{i}]/td[6]').text  # td[6] - код услуги
        title = driver.find_element(By.XPATH, f'//*[@id="ReportTable"]/tbody/tr[{i}]/td[7]').text  # td[7] - наименование услуги
        name = driver.find_element(By.XPATH, f'//*[@id="ReportTable"]/tbody/tr[{i}]/td[8]').text  # td[8] - имя мастера
        date_time = driver.find_element(By.XPATH, f'//*[@id="ReportTable"]/tbody/tr[{i}]/td[11]').text  # td[11] - дата и время
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
    salary_massage += f'Итого з/п = {salary_count}р'
    #print(salary_massage)




    #print(tr_count)
    time.sleep(5) # ждем 5сек
    driver.close() #закрываем сайт

    # td[6] – код услуги
    # td[7] – наименование услуги
    # td[8] – имя мастера
    # td[11] – дата и время платежа

    return salary_massage


bot.polling(none_stop=True)