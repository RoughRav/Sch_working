import csv

def create_data(text: str):
    """Добавление нового контакта"""
    text = list(text.split())
    with open('data_base.csv', 'a', newline= '', encoding='UTF-8') as file:
        data = csv.writer(file)
        data.writerow(text)
        print('Информация внесена')
