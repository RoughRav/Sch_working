# with open ('example.txt', 'w+') as file:
#     file.write('Питт, Брэд, 5555, Актер, Неизв, Паук, 111, Музыкант, Зверев, Сергей, 222, Стилист, Михалков, Никита, 333, Режиссер, Лель, Катя, 444, певица')
# print()
def add_contact(PB,name,phone):
    PB[name] = phone
def delete_contact(PB,name):
    if name in PB:
        del PB[name]
    else:
        print('Такого контакта нет')
def save_PB(PB,example):
    with open(example, 'w+') as f:
        for name, phone in PB.items():
            f.write(f'{name},{phone}\n')
# def read_txt(example):
#     phone_book=[]
#     fields=['Фамиль', 'Имя','Телефон','Описание']
#     with open(example, 'r', encoding='utf-8') as f:
#         for line in f:
#             record=dict(zip(fields,line.split(',')))
#             phone_book.append(record)
#     return phone_book
# def write_txt(example, phone_book):
#     with open(example, 'w', encoding='utf-8') as fg:
#         for i in range(len(phone_book)):
#             s=''
#             for v in phone_book[i].values():
#                 s=s+v+','
#             fg.write(f'{s[:-1]}\n')
def load_PB(example):
    PB={}
    with open(example, 'r', encoding='utf-8') as f:
        for line in f:
            name, phone=line.strip().split(',')
            PB[name]=phone
    except FileNotFoundError:
    pass
    return PB
def main():
    filename='example'
    phonebook=load_phonebook(filename)
while True:
    print('\n1. Добавить контакт')
    print('2. Удалить контакт')
    print('3. Вывести контакты')
    print('4. Выйти')
    choice=input('Выберите действие: ')
    if choice=='1':
        name=input('Введите имя: ')
        phone=input('Введите телефон: ')
        add_contact(phonebook,name,phone)
        save_PB(phonebook,filename)
    elif choice=='2':
        name=input('Введите имя контактк для удаления: ')
        delete_contact(phonebook,name)
        save_PB(phonebook,filename)
    elif choice=='3':
        display_contacts(phonebook)
    elif choice=='4':
        break
    else:
        print('Неизвестная команда, попробуйте снова')
if __name__ == '__main__':
main()