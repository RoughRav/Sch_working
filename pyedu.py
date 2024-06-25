PB=read_txt('Tphones.txt')
phonebook={}
def add_contact(name,phone):
    phonebook[name] = phone
    print(f'Contact {name} added to {phonebook}')
def delete_contact(name):
    if name in phonebook:
        del phonebook[name]
    else:
        print('No contact in your phonbook')
def display_contacts():
    if not phonebook:
        print('Empty phonebook')
    else:
      for name, phone in phonebook.items():
        print(f'{name}: {phone}')
def main():
    while True:
        print('\n1. Add contact')
        print('2. Delete contact')
        print('3. Display all contacts')
        print('4. Exit')
        choice=int(input())
        if choice=='1':
            name=input('Enter name: ')
            phone=input('Enter phone: ')
            add_contact(name,phone)
        elif choice=='2':
            name=input('Enter name for deleting: ')
            delete_contact(name)
        elif choice=='3':
            display_contacts(phonebook)
        elif choice=='4':
            break
        else:
            print('Unknown command, try again')
if __name__=='__main__':
    main()
