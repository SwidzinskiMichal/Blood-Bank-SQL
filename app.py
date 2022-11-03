import database

MENU_PROMPT = """ --Blood Barnk Database --

Options:

1) Add a new donor 
2) Search all donors
3) Search donors by name
4) Search donors by surname
5) Search donors by age
6) Search donors by sex
7) Search donors by type
8) Check blood quantity by type
9) Exit

Select: """


def menu():
    connection = database.connect_db()
    database.create_table(connection)
    
    while (user_input := input(MENU_PROMPT)) != "9":
        if user_input == "1":
            name = input("Enter donor's name: ")
            surname = input("Enter donor's surname: ")
            age = int(input("Enter donor's age: "))
            sex = input("Enter donor's sex: ")
            bloodtype = input("Enter donor's blood type: ")
            quantity = int(input("Enter quantity donated: "))
            database.add_donor(connection, name, surname, age, sex, bloodtype, quantity)
        elif user_input == "2":
            list_of_donors = database.get_all_donors(connection)
            for donor in list_of_donors:
                print(donor)
        elif user_input == "3":
            if user_input == "3":
                name = input("Enter donor's name: ")
                get_donors_by_name = database.get_donors_by_name(connection, name)
                for name in get_donors_by_name:
                    print(name)
        elif user_input == "4":
            if user_input == "4":
                surname = input("Enter donor's surname: ")
                get_donors_by_surname = database.get_donors_by_surname(connection, surname)
                for surname in get_donors_by_surname:
                    print(surname)
        elif user_input == "5":
            if user_input == "5":
                age = int(input("Enter donor's age: "))
                get_donors_by_age = database.get_donors_by_age(connection, age)
                for age in get_donors_by_age:
                    print(age)
        elif user_input == "6":
            if user_input == "6":
                sex = input("Enter donor's sex: ")
                get_donors_by_sex = database.get_donors_by_sex(connection, sex)
                for sex in get_donors_by_sex:
                    print(sex)
        elif user_input == "7":
            if user_input == "7":
                bloodtype = input("Enter donor's blood type: ")
                get_donors_by_type = database.get_donors_by_type(connection, bloodtype)
                for bloodtype in get_donors_by_type:
                    print(bloodtype)
        elif user_input == "8":
            blood_quantity = database.get_type_quantity(connection)
            for bloodtype in blood_quantity:
                print(bloodtype)
        else:
            print("Invalid input")

        
menu()
