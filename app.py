import database

MENU_PROMPT = """ --Blood Barnk Database --

Options:

1) Add a new donor 
2) Search all donors
3) Search donors by id
4) Search donors by name
5) Search donors by surname
6) Search donors by age
7) Search donors by sex
8) Search donors by type
9) Check blood quantity by type
10) Update donor's blood quantity
11) Delete donor from database
0) Exit

Select: """


def menu():
    connection = database.connect_db()
    database.create_table(connection)
    
    while (user_input := input(MENU_PROMPT)) != "0":
        if user_input == "1":
            add_new_donor(connection)
        elif user_input == "2":
            list_donors(connection)
        elif user_input == "3":
            search_donors_by_id(connection)
        elif user_input == "4":
            search_donors_by_name(connection)
        elif user_input == "5":
            search_donors_by_surname(connection)
        elif user_input == "6":
            search_donors_by_age(connection)
        elif user_input == "7":
            search_donors_by_sex(connection)
        elif user_input == "8":
            search_donors_by_bloodtype(connection)
        elif user_input == "9":
            check_blood_quanity(connection)
        elif user_input == "10":
            update_bloods_quantity(connection)
        elif user_input == "11":
            remove_donor_from_db(connection)
        else:
            print("Invalid input")


def add_new_donor(connection):
    name = input("Enter donor's name: ")
    surname = input("Enter donor's surname: ")
    age = int(input("Enter donor's age: "))
    sex = input("Enter donor's sex: ")
    bloodtype = input("Enter donor's blood type: ")
    quantity = int(input("Enter quantity donated: "))
    database.add_donor(connection, name, surname, age, sex, bloodtype, quantity)

def list_donors(connection):
    list_donors = database.fetch_all_donors(connection)
    for donor in list_donors:
        print(donor)   

def search_donors_by_id(connection):
    id = input("Enter donor's id: ")
    get_donors_by_id = database.fetch_donors_by_id(connection, id)
    for id in get_donors_by_id:
        print(id)

def search_donors_by_name(connection):
    name = input("Enter donor's name: ")
    get_donors_by_name = database.fetch_donors_by_name(connection, name)
    for name in get_donors_by_name:
        print(name)

def search_donors_by_surname(connection):
    surname = input("Enter donor's surname: ")
    get_donors_by_surname = database.fetch_donors_by_surname(connection, surname)
    for surname in get_donors_by_surname:
        print(surname)

def search_donors_by_age(connection):
    age = int(input("Enter donor's age: "))
    get_donors_by_age = database.fetch_donors_by_age(connection, age)
    for age in get_donors_by_age:
        print(age)

def search_donors_by_sex(connection):
    sex = input("Enter donor's sex: ")
    get_donors_by_sex = database.fetch_donors_by_sex(connection, sex)
    for sex in get_donors_by_sex:
        print(sex)

def search_donors_by_bloodtype(connection):
    bloodtype = input("Enter donor's blood type: ")
    get_donors_by_type = database.fetch_donors_by_type(connection, bloodtype)
    for bloodtype in get_donors_by_type:
        print(bloodtype)

def check_blood_quanity(connection):
    blood_quantity = database.fetch_type_quantity(connection)
    for bloodtype in blood_quantity:
        print(bloodtype)

def update_bloods_quantity(connection):
    name = input("Enter donor's name: ")
    surname = input("Enter donor's surname: ")
    quantity = int(input("Enter quantity: "))
    database.update_blood_quantity_in_db(connection, name, surname, quantity)


def remove_donor_from_db(connection):
    id = input("Enter donor's id: ")
    database.remove_donor(connection, id)

menu()
