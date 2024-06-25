with open(Tphones.txt, 'r') as file1:
    lines1 = file1.readlines()
    for name, family name, phone, status in zip(lines1):
        print(f'name, family, phone, status')

line.split(',') = [РџРёС‚РѕРЅРѕРІ,    РђРЅС‚РѕРЅ,     '777',    'СѓРјРµРµС‚ РІ РџРёС‚РѕРЅ']

    with open(filename,'r',encoding='utf-8') as phb:

        for line in phb:

           record = dict(zip(fields, line.split(',')))


			#dict(( (С„Р°РјРёР»РёСЏ,РРІР°РЅРѕРІ),(РёРјСЏ, РўРѕС‡РєР°),(РЅРѕРјРµСЂ,8928) ))
	     
		
	   phone_book.append(record)	

    return phone_book


contact = {}


def display_contact():
    print(contact.items())
    print("Name\t\tContact Number")
    for key in contact:
        print("{}\t\t{}".format(key,contact.get(key)))


while True:
    choice = int(input(" 1. Add new contact \n 2. Search contact \n 3.Display contact\n 4. Edit contact \n 5. Delete contact\n 6.Exit\n Enter your choice "))
    if choice == 1:
        name = input("enter the contact name ")
        phone = input("enter the mobile number")
        contact[name] = phone
    elif choice == 2:
        search_name = input("enter the contact name ")
        if search_name in contact:
            print(search_name,"contact number is ",contact[search_name])
        else:
            print("Name is not found in contact book")
    elif choice == 3:
        if not contact:
            print("empty contact book")
        else:
            display_contact()
    elif choice == 4:
        edit_contact = input("Enter the contact to be edited ")
        if edit_contact in contact:
            phone = input("enter mobile number")
            contact[edit_contact]=phone
            print("contact updated")
            display_contact()
        else:
            print("Name is not found in contact book")
    elif choice == 5:
        del_contact = input("Enter the contact to be deleted ")
        if del_contact in contact:
            confirm = input("Do you want to delete this contact y/n? ")
            if confirm =='y' or confirm =='Y':
                contact.pop(del_contact)
            display_contact()
        else:
            print("Name is not found in contact book")
    else:
        break

