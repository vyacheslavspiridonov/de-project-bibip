#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
import string
import decimal
from datetime import datetime, timedelta 
import pandas as pd # для работы с таблицами при генерации данных
import os


# ## Генерация данных:

# ### `Models`

# Имя автомобильной модели:

# In[ ]:


def generate_model_name():
    # Наборы символов
    letters = string.ascii_uppercase  # Только заглавные латинские буквы
    digits = string.digits            # Цифры от 0 до 9

    part1 = random.choices(letters)[0]                       
    part2 = random.randint(2,9)

    return f'{part1}-{part2}'


# In[ ]:


model_names = [generate_model_name() for _ in range(1,501)]


# ID строк (Primary Key):

# In[ ]:


model_id = list(range(1,501))


# Бренды:

# In[ ]:


def generate_brand():
    # Генерация 26 брендов (Размер алфавита)
    return random.choice(string.ascii_uppercase)

brands = [generate_brand() for _ in range(500)]


# **Таблица:**

# In[ ]:


models = pd.DataFrame(
    {'id':model_id,
    'name':model_names,
    'brand':brands})\
        .drop_duplicates(['name', 'brand'])\
        .reset_index(drop=True)


# In[ ]:


# Запись в файл
models.to_csv('data/models.txt', index=False, sep=';')


# Конвертация в файл с фикс. длиной строки:

# In[ ]:


with open('data/models.txt', mode='r', encoding='utf-8', newline='') as models_f:
    lines = models_f.readlines()

with open('data/models.txt', mode='w', encoding='utf-8', newline='') as models_f:
    for line in lines:
        models_f.write(line.strip().ljust(200-1)+'\n')


# Индекс:

# In[ ]:


model_indexed_row_order = models['id']\
    .sort_values()\
    .reset_index()\
    .rename(columns={'id':'key'})


# In[ ]:


# Убираем индекс 0, прибавив ко всем значениям 1
model_indexed_row_order['index'] = model_indexed_row_order['index']+1


# In[ ]:


# Запись в файл
model_indexed_row_order[['key','index']].to_csv('data/models_index.txt', index=False, sep=';')


# Конвертация в файл с фикс. длиной строки:

# In[ ]:


with open('data/models_index.txt', mode='r', encoding='utf-8') as models_f:
    lines = models_f.readlines()

with open('data/models_index.txt', mode='w', encoding='utf-8', newline='') as models_f:
    for line in lines:
        models_f.write(line.strip().ljust(200-1)+'\n')


# ### `Cars`

# Размер тестового файла:

# In[ ]:


size_for_test = 500_000


# Генерация VIN:

# In[ ]:


def generate_vin():
    # Наборы символов
    letters = string.ascii_uppercase  # Только заглавные латинские буквы
    digits = string.digits            # Цифры от 0 до 9

    # Конструируем строку по позициям (на основе "5XYPH4A10GG021831"):
    part1 = str(random.randint(0,9))                         # Статичное начало (1 симв.)
    part2 = "".join(random.choices(letters, k=4))            # 4 случайные буквы (в примере: XYPH)
    part3 = "".join(random.choices(digits, k=1))             # 1 случайная цифра (в примере: 4)
    part4 = "".join(random.choices(letters, k=1))            # 1 случайная буква (в примере: A)
    part5 = "".join(random.choices(digits, k=2))             # 2 случайные цифры (в примере: 10)
    part6 = "".join(random.choices(letters, k=2))            # 2 случайные буквы (в примере: GG)
    part7 = "".join(random.choices(digits, k=6))             # 6 случайных цифр  (в примере: 021831)

    # Собираем всё вместе
    return f"{part1}{part2}{part3}{part4}{part5}{part6}{part7}"


# In[ ]:


vin_list = [generate_vin() for _ in range(size_for_test)]


# Модели:

# In[ ]:


models_id_fk = [random.randint(1,501) for _ in range(size_for_test)]


# Цены:

# In[ ]:


prices = [round(random.randint(2000, 4000)+random.random(),2) for _ in range(size_for_test)]


# Даты:

# In[ ]:


def generate_date(start_year, end_year):
    """Генерация одной случайной даты в диапазоне."""
    # Получаем временную метку (timestamp) в секундах

    start_day = datetime(year=start_year, month=1, day=1)
    end_day = datetime(year=end_year, month=8, day=31)

    time_between_dates = end_day - start_day
    days_between_dates = time_between_dates.days


    # Генерируем случайное количество дней
    random_number_of_days = random.randrange(days_between_dates)

    # Добавляем случайное число дней к начальной дате
    return datetime.date(start_day + timedelta(days=random_number_of_days))


# In[ ]:


start, end = 2020, 2024
dates = [generate_date(start, end) for _ in range(size_for_test)]


# Статус автомомобиля:

# In[ ]:


def get_status():
    status_enums = ["available", "reserve", "sold", "delivery"]
    return random.choice(status_enums)


# In[ ]:


status = [get_status() for i in range(size_for_test)]


# **Таблица:**

# In[ ]:


cars = pd.DataFrame(
    {'vin':vin_list,
     'model':models_id_fk,
     'price':prices,
     'date_start':dates,
     'status':status}
)


# In[ ]:


cars.to_csv('data/cars.txt', sep=';', index=False)


# Конвертация в файл с фикс. длиной строки:

# In[ ]:


with open('data/cars.txt', mode='r', encoding='utf-8') as cars_f:
    lines = cars_f.readlines()

with open('data/cars.txt', mode='w', encoding='utf-8', newline='') as cars_f:
    for line in lines:
        cars_f.write(line.strip().ljust(200-1)+'\n')


# Индекс:

# In[ ]:


cars_indexed_row_order = cars['vin']\
    .sort_values()\
    .reset_index()\
    .rename(columns={'vin':'key'})


# In[ ]:


# Убираем индекс 0, прибавив ко всем значениям 1
cars_indexed_row_order['index'] = cars_indexed_row_order['index']+1


# In[ ]:


cars_indexed_row_order[['key','index']].to_csv('data/cars_index.txt', index=False, sep=';')


# Конвертация в файл с фикс. длиной строки:

# In[ ]:


with open('data/cars_index.txt', mode='r', encoding='utf-8') as cars_f:
    lines = cars_f.readlines()

with open('data/cars_index.txt', mode='w', encoding='utf-8', newline='') as cars_f:
    for line in lines:
        cars_f.write(line.strip().ljust(200-1)+'\n')


# ### `Sales`

# Сформируем базу для таблицы продаж, взяв строки из таблицы Cars со статусом Sold:

# In[ ]:


sales_base = cars[cars['status']=='sold'][['vin','price','date_start']]\
    .rename(columns={'vin':'car_vin'})\
        .reset_index(drop=True)


# Подготовка и формирование столбца с номером продажи:

# In[ ]:


# Количество автосалонов (Любое правдоподное число)
total_dealers = 36

# Предположим, что продажи деляется поровну
group_size = len(sales_base)//total_dealers

# Остаток добавляем в последнюю группу
last_group_size = group_size + len(sales_base)%total_dealers

#len(sales_base) == len(sales_base)//total_dealers * total_dealers + len(sales_base)%total_dealers


# Формирование и объединение списков:

# In[ ]:


sales_list = [
    f'{a}#' + str(i) 
    for a in range(1, total_dealers + 1)
    for i in range(1, last_group_size+1 if a == total_dealers else group_size+1)
]


# In[ ]:


sales_base['sales_number'] = sales_list


# Допустим, все машины были проданы с коэффициентом от 1 до 2 от закупочной стоимоси (price):

# In[ ]:


# Подготовка коэффициента для расчёта стоимости
sales_base['koef'] = pd.Series([round(random.random()+1,2) for _ in range(len(sales_base))])


# In[ ]:


# Расчёт итоговой стоимости
sales_base['cost'] = round(sales_base['price']*sales_base['koef'], 2)


# In[ ]:


# Удалении промежуточных столбцов koef и cost
sales_base_with_cost = sales_base.drop(['price','koef'], axis=1)


# Сформируем случайный период от 7 до 180 дней (Период продажи):

# In[ ]:


sales_base_with_cost['sales_period'] = pd.to_timedelta(
    pd.Series([random.randint(7, 180) for _ in range(len(sales_base_with_cost))]), unit='D'
)


# In[ ]:


# Расчёт даты продажи
sales_base_with_cost['sales_date'] = pd.to_datetime(sales_base_with_cost['date_start']) + sales_base_with_cost['sales_period']


# **Таблица**:

# In[ ]:


# Удаление промежуточных столбцов sales_period и date_start
sales = sales_base_with_cost.drop(['sales_period','date_start'], axis=1)[
    # Формирование порядка столбцов
    ['sales_number','car_vin','cost','sales_date']
]


# In[ ]:


sales.to_csv('data/sales.txt',sep=';', index=False)


# Конвертация в файл с фикс. длиной строки:

# In[ ]:


with open('data/sales.txt', mode='r', encoding='utf-8') as sales_f:
    lines = sales_f.readlines()

with open('data/sales.txt', mode='w', encoding='utf-8', newline='') as sales_f:
    for line in lines:
        sales_f.write(line.strip().ljust(200-1)+'\n')


# Индекс:

# In[ ]:


sales_with_index = sales.reset_index()


# In[ ]:


sales_with_index['index'] = sales_with_index['index'] + 1


# In[ ]:


sales_index = sales_with_index[['car_vin','index']]\
    .sort_values(by='car_vin')\
    .rename(columns={'car_vin':'key'})


# In[ ]:


sales_index.to_csv('data/sales_index.txt', sep=';', index=False)


# Конвертация в файл с фикс. длиной строки:

# In[ ]:


with open('data/sales_index.txt', mode='r', encoding='utf-8') as sales_f:
    lines = sales_f.readlines()

with open('data/sales_index.txt', mode='w', encoding='utf-8', newline='') as sales_f:
    for line in lines:
        sales_f.write(line.strip().ljust(200-1)+'\n')


# In[ ]:


print("Данные для работы успешно сгенерированны! Размер строки в файлах - 200 байт")


# In[ ]:




