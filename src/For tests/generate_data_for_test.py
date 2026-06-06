#!/usr/bin/env python
# coding: utf-8

# In[237]:

def generate_data_for_test_func():
    from datetime import datetime
    from decimal import Decimal


    # In[238]:


    from models import Car, CarFullInfo, CarStatus, Model, ModelSaleStats, Sale


    # In[239]:


    import pandas as pd
    import os


    # In[240]:


    cwd = os.path.dirname(os.path.abspath(__name__))


    # Модели:

    # In[241]:


    # Данные из файла теста
    models_list = [
            Model(id=1, name="Optima", brand="Kia"),
            Model(id=2, name="Sorento", brand="Kia"),
            Model(id=3, name="3", brand="Mazda"),
            Model(id=4, name="Pathfinder", brand="Nissan"),
            Model(id=5, name="Logan", brand="Renault"),
        ]


    # In[242]:


    # Сборка датафрейма
    models = pd.DataFrame(
        {'id':[x.id for x in models_list] ,
        'name':[x.name for x in models_list],
        'brand':[x.brand for x in models_list]})\
            .drop_duplicates(['name', 'brand'])\
            .reset_index(drop=True)


    # In[243]:


    # Запись в файл
    models.to_csv(f'{cwd}//data_for_test//models.txt', index=False, sep=';')


    # Конвертация в формат, необходимый для работы методов класса CarService:

    # In[244]:


    with open(f'{cwd}//data_for_test//models.txt', mode='r', encoding='utf-8') as models_f:
        lines = models_f.readlines()

    with open(f'{cwd}//data_for_test//models.txt', mode='w', encoding='utf-8', newline='') as models_f:
        for line in lines:
            models_f.write(line.strip().ljust(200-1)+'\n')


    # Индекс таблицы с моделями авто:

    # In[245]:


    model_indexed_row_order = models['id']\
        .sort_values()\
        .reset_index()\
        .rename(columns={'id':'key'})


    # In[246]:


    # Убираем индекс 0, прибавив ко всем значениям 1
    model_indexed_row_order['index'] = model_indexed_row_order['index']+1


    # In[247]:


    # Запись в файл
    model_indexed_row_order[['key','index']].to_csv('data_for_test//models_index.txt', index=False, sep=';')


    # In[248]:


    # Конвертация в формат, необходимый для работы методов:
    with open(f'{cwd}//data_for_test//models_index.txt', mode='r', encoding='utf-8') as models_f:
        lines = models_f.readlines()

    with open(f'{cwd}//data_for_test//models_index.txt', mode='w', encoding='utf-8', newline='') as models_f:
        for line in lines:
            models_f.write(line.strip().ljust(200-1)+'\n')


    # ---

    # Авто:

    # In[249]:


    # Данные из файла теста
    cars_list = [
            Car(
                vin="KNAGM4A77D5316538",
                model=1,
                price=Decimal("2000"),
                date_start=datetime(2024, 2, 8),
                status=CarStatus.available,
            ),
            Car(
                vin="5XYPH4A10GG021831",
                model=2,
                price=Decimal("2300"),
                date_start=datetime(2024, 2, 20),
                status=CarStatus.reserve,
            ),
            Car(
                vin="KNAGH4A48A5414970",
                model=1,
                price=Decimal("2100"),
                date_start=datetime(2024, 4, 4),
                status=CarStatus.available,
            ),
            Car(
                vin="JM1BL1TFXD1734246",
                model=3,
                price=Decimal("2276.65"),
                date_start=datetime(2024, 5, 17),
                status=CarStatus.available,
            ),
            Car(
                vin="JM1BL1M58C1614725",
                model=3,
                price=Decimal("2549.10"),
                date_start=datetime(2024, 5, 17),
                status=CarStatus.reserve,
            ),
            Car(
                vin="KNAGR4A63D5359556",
                model=1,
                price=Decimal("2376"),
                date_start=datetime(2024, 5, 17),
                status=CarStatus.available,
            ),
            Car(
                vin="5N1CR2MN9EC641864",
                model=4,
                price=Decimal("3100"),
                date_start=datetime(2024, 6, 1),
                status=CarStatus.available,
            ),
            Car(
                vin="JM1BL1L83C1660152",
                model=3,
                price=Decimal("2635.17"),
                date_start=datetime(2024, 6, 1),
                status=CarStatus.available,
            ),
            Car(
                vin="5N1CR2TS0HW037674",
                model=4,
                price=Decimal("3100"),
                date_start=datetime(2024, 6, 1),
                status=CarStatus.available,
            ),
            Car(
                vin="5N1AR2MM4DC605884",
                model=4,
                price=Decimal("3200"),
                date_start=datetime(2024, 7, 15),
                status=CarStatus.available,
            ),
            Car(
                vin="VF1LZL2T4BC242298",
                model=5,
                price=Decimal("2280.76"),
                date_start=datetime(2024, 8, 31),
                status=CarStatus.delivery,
            ),
        ]


    # In[250]:


    # Сохранение в датафрейм
    cars = pd.DataFrame(
        {'vin':[x.vin for x in cars_list],
        'model':[x.model for x in cars_list],
        'price':[x.price for x in cars_list],
        'date_start':[datetime.strftime(x.date_start, '%Y-%m-%d') for x in cars_list],
        'status':[str(x.status) for x in cars_list]
        }
    )


    # In[251]:


    # Запись в файл
    cars.to_csv(f'{cwd}//data_for_test//cars.txt', sep=';', index=False)


    # Конвертация в формат, необходимый для работы методов класса CarService:

    # In[252]:


    with open(f'{cwd}//data_for_test//cars.txt', mode='r', encoding='utf-8') as cars_f:
        lines = cars_f.readlines()

    with open(f'{cwd}//data_for_test//cars.txt', mode='w', encoding='utf-8', newline='') as cars_f:
        for line in lines:
            cars_f.write(line.strip().ljust(200-1)+'\n')


    # Индекс авто:

    # In[253]:


    cars_indexed_row_order = cars['vin']\
        .sort_values()\
        .reset_index()\
        .rename(columns={'vin':'key'})


    # In[254]:


    # Убираем индекс 0, прибавив ко всем значениям 1
    cars_indexed_row_order['index'] = cars_indexed_row_order['index']+1


    # In[255]:


    cars_indexed_row_order[['key','index']].to_csv('data_for_test//cars_index.txt', index=False, sep=';')


    # In[256]:


    with open(f'{cwd}//data_for_test//cars_index.txt', mode='r', encoding='utf-8') as cars_f:
        lines = cars_f.readlines()

    with open(f'{cwd}//data_for_test//cars_index.txt', mode='w', encoding='utf-8', newline='') as cars_f:
        for line in lines:
            cars_f.write(line.strip().ljust(200-1)+'\n')


    # ### `Sales`

    # Сформируем базу для таблицы продаж, взяв строки из таблицы Cars со статусом Sold:

    # In[257]:


    sales_base = cars[cars['status']=='sold'][['vin','price','date_start']]\
        .rename(columns={'vin':'car_vin'})\
            .reset_index(drop=True)


    # Подготовка и формирование столбца с номером продажи:

    # In[258]:


    # Количество автосалонов (Любое правдоподное число)
    total_dealers = 36

    # Предположим, что продажи деляется поровну
    group_size = len(sales_base)//total_dealers

    # Остаток добавляем в последнюю группу
    last_group_size = group_size + len(sales_base)%total_dealers

    #len(sales_base) == len(sales_base)//total_dealers * total_dealers + len(sales_base)%total_dealers


    # Формирование и объединение списков:

    # In[259]:


    sales_list = [
        f'{a}#' + str(i) 
        for a in range(1, total_dealers + 1)
        for i in range(1, last_group_size+1 if a == total_dealers else group_size+1)
    ]


    # In[260]:


    sales_base['sales_number'] = sales_list


    # Допустим, все машины были проданы с коэффициентом от 1 до 2 от закупочной стоимоси (price):

    # In[261]:


    # Подготовка коэффициента для расчёта стоимости
    sales_base['koef'] = pd.Series([round(random.random()+1,2) for _ in range(len(sales_base))])


    # In[262]:


    # Расчёт итоговой стоимости
    sales_base['price'] - pd.to_numeric(sales_base['price'])
    sales_base['cost'] = round(sales_base['price']*sales_base['koef'], 2) if len(sales_base) != 0 else pd.Series() ## 


    # In[263]:


    # Удалении промежуточных столбцов koef и cost
    sales_base_with_cost = sales_base.drop(['price','koef'], axis=1)


    # Сформируем случайный период от 7 до 180 дней (Период продажи):

    # In[264]:


    sales_base_with_cost['sales_period'] = pd.to_timedelta(
        pd.Series([random.randint(7, 180) for _ in range(len(sales_base_with_cost))]), unit='D'
    )


    # In[265]:


    # Расчёт даты продажи
    sales_base_with_cost['sales_date'] = pd.to_datetime(sales_base_with_cost['date_start']) + sales_base_with_cost['sales_period']


    # In[266]:


    # Удаление промежуточных столбцов sales_period и date_start
    sales = sales_base_with_cost.drop(['sales_period','date_start'], axis=1)[
        # Формирование порядка столбцов
        ['sales_number','car_vin','cost','sales_date']
    ]


    # Запись в рабочую директорию:

    # In[267]:


    sales.to_csv(f'{cwd}//data_for_test//sales.txt',sep=';', index=False)


    # Конвертация в файл с фикс. длиной строки:

    # In[268]:


    with open(f'{cwd}//data_for_test//sales.txt', mode='r', encoding='utf-8') as sales_f:
        lines = sales_f.readlines()

    with open(f'{cwd}//data_for_test//sales.txt', mode='w', encoding='utf-8', newline='') as sales_f:
        for line in lines:
            sales_f.write(line.strip().ljust(200-1)+'\n')


    # Индекс: 

    # In[269]:


    sales_with_index = sales.reset_index()


    # In[270]:


    sales_with_index['index'] = sales_with_index['index'] + 1


    # In[271]:


    sales_index = sales_with_index[['car_vin','index']]\
        .sort_values(by='car_vin')\
        .rename(columns={'car_vin':'key'})


    # In[272]:


    sales_index.to_csv(f'{cwd}//data_for_test//sales_index.txt', sep=';', index=False)


    # Конвертация в файл с фикс. длиной строки:

    # In[273]:


    with open(f'{cwd}//data_for_test//sales_index.txt', mode='r', encoding='utf-8') as sales_f:
        lines = sales_f.readlines()

    with open(f'{cwd}//data_for_test//sales_index.txt', mode='w', encoding='utf-8', newline='') as sales_f:
        for line in lines:
            sales_f.write(line.strip().ljust(200-1)+'\n')


    # In[274]:


    print("Данные для работы успешно сгенерированны!") 


    # 
