import database

MENU_PROMPT = """ --Blood Barnk Database --

Options:

1) Add a new donor 
2) Get all donors
3) Search donors
4) Check blood quantity by type
5) Update donor's blood quantity
6) Delete donor from database
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
            search_donors(connection)
        elif user_input == "4":
            check_blood_quanity(connection)
        elif user_input == "5":
            update_bloods_quantity(connection)
        elif user_input == "6":
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

def search_donors(connection):
    print("Please enter search paramiters in lower case and with inverted commas (ex. name = 'John').")
    print("Multiple paramiters searched together need to be separated with AND (ex. name = 'John' AND surname = 'Adams')")
    print("Allowed search paramiters are name, surname, age, sex and bloodtype")
    search_paramiters = input("Enter paramiters: ")
    get_donors = database.custom_search(connection, search_paramiters)
    for donor in get_donors:
        print(donor)

def check_blood_quanity(connection):
    blood_quantity = database.fetch_type_quantity(connection)
    for bloodtype in blood_quantity:
        print(bloodtype)

def update_bloods_quantity(connection):
    id = input("Enter donor's id: ")
    quantity = int(input("Enter quantity: "))
    database.update_blood_quantity_in_db(connection, id, quantity)

def remove_donor_from_db(connection):
    id = input("Enter donor's id: ")
    database.remove_donor(connection, id)

menu()
