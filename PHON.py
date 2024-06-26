# ---------- Основной модуль
filename_work = "Tphones.txt"


#  ФУНКЦИИ ...................................................................

#1 Показать весь справочник
def show_all(my_dict):
    s = 0
    for j in my_dict:
        j = str(j).title()
        s = s + 1
        print(f'{s}. {j}')



# 2 Добавить новый контакт в справочник
def add_contact(my_dict):
    name = input('Введите имя контакта: \n')
    phone = input('Введите номер телефона контакта: \n')
    comment = input('Введите коментарий к контакту: \n')
    new_string = f'{name} {phone} {comment}'.title()
    my_dict.append({'Имя': name, 'Телефон': phone, 'Коментарий': comment})
    with open('Tphones.txt', 'a+', encoding='utf-8') as file:
        file.write(f'{new_string} \n')


# 3 Поиск контакта
def find_contact(my_dict):
    search_word = input('Введите текст для поиска: \n').lower()
    for item in range(len(my_dict)):
        for i in my_dict[item].values():
            if search_word in i:
                print(f'{item + 1}. {my_dict[item]}')

# 4 Изменение контакта
def change_contact(my_dict,index):
    to_change = int(input('Что хотите изменить? \n \
1 - имя \n 2 - номер телефона \n 3 - коментарий \n - '))
    fields = list(my_dict[0].keys())
    new_value = input('Введите новое значение поля: ')
    temp_dict = my_dict[index]
    temp_dict[fields[to_change -1]] = new_value
    my_dict[index] = temp_dict
    with open('phones.txt', 'w', encoding='utf-8') as file:
        for i in my_dict:
            file.write(f'{i["Имя"]} {i["Телефон"]} {i["Коментарий"]} \n')

# 5 Удаление контакта
def del_contact(my_dict,index):
    my_dict.pop(index)
    with open('phones.txt', 'w', encoding='utf-8') as file:
        for i in my_dict:
            file.write(f'{i["Имя"]} {i["Телефон"]} {i["Коментарий"]} \n')




# КОД....................................................................

my_guide = []
with open('Tphones.txt', 'r', encoding='utf-8') as file:
    for i in file:
        my_list = i.lower().split()
        my_guide.append({'Имя': my_list[0],'Телефон': my_list[1], 'Коментарий': my_list[2]})

while True:
    try:
        print('Выберите нужный пункт ниже: \n 1. Показывать все контакты \n 2. Добавить контакт \n \
3. Найти контакт \n 4. Изменить контакт \n 5. Удалить контакт \n 6. Выход из программы')
        request = int(input('Введите цифру: '))
        print()
        if request == 1:
            show_all(my_guide)
            print()
        elif request == 2:
            add_contact(my_guide)
            print()
        elif request == 3:
            find_contact(my_guide)
            print()
        elif request == 4:
            index = int(input('Введите индекс контакта: '))
            change_contact(my_guide,index - 1)
            print()
        elif request == 5:
            i = int(input('Введите индекс контакта: '))
            del_contact(my_guide,i - 1)
            print()
        elif request == 6:
            break

    except ValueError:
        print('Вы ввели неверное значение, выбирете цифру из меню.')
        print()
        next