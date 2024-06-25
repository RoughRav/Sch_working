'''Взаимодействие с пользователем'''


def interaction():
    """Выбор действия пользователя"""
    action = int(input('Введите номер команды: \n1 - Сделать запись\n2 - Получить номер телефона\n3 - Удалить запись\n'))
    if action == 1:
        text_input = input('Введите ФИО и номер телефона через пробел: ')
        return (text_input, action)
    if action == 2:
        text_input = input('Введите фамилию/имя/отчество: ')
        return (text_input, action)
    if action == 3:
        text_input = input('Введите фамилию/имя/отчество/номер телефона: ')
        return (text_input, action)


def res_find(string: list):
    for item in string:
        print(item)

