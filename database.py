import sqlite3


CREATE_BLOODBANK_TABLE = "CREATE TABLE IF NOT EXISTS donors (id INTEGER PRIMERY KEY, name TEXT, surname TEXT, age INTEGER, sex TEXT, bloodtype TEXT, quantity INTEGER);"

INSERT_DONOR = "INSERT INTO donors (name, surname, age, sex, bloodtype, quantity) VALUES (?, ?, ?, ?, ?, ?);"

GET_ALL_DONORS = "SELECT * FROM donors;"
GET_DONORS_BY_NAME = "SELECT * FROM donors WHERE name = ?;"
GET_DONORS_BY_SURNAME = "SELECT * FROM donors WHERE surname = ?;"
GET_DONORS_BY_AGE = "SELECT * FROM donors WHERE age = ?;"
GET_DONORS_BY_SEX = "SELECT * FROM donors WHERE sex = ?;"
GET_DONORS_BY_TYPE = "SELECT * FROM donors WHERE bloodtype = ?;"
GET_TYPE_QUANTITY = """
                    SELECT bloodtype,
                    SUM (quantity)
                    FROM donors
                    GROUP BY bloodtype;
                    """
UPDATE_BLOOD_QUANTITY = "UPDATE donors SET quantity = ? WHERE name = ? AND surname = ?;"
DELTE_DONOR = "DELETE FROM donors WHERE name =? AND surname = ?;" 
                


def connect_db():
    return sqlite3.connect("blood-bank-sql/bloodbank.db")

def create_table(connection):
    with connection:
        connection.execute(CREATE_BLOODBANK_TABLE)

def add_donor(connection, name, surname, age, sex, bloodtype, quantity):
    with connection:
        connection.execute(INSERT_DONOR, (name, surname, age, sex, bloodtype, quantity,))

def fetch_all_donors(connection):
    with connection:
        return connection.execute(GET_ALL_DONORS).fetchall()

def fetch_type_quantity(connection):
    with connection:
        return connection.execute(GET_TYPE_QUANTITY).fetchall()

def fetch_donors_by_name(connection, name):
    with connection:
        return connection.execute(GET_DONORS_BY_NAME, (name,)).fetchall()

def fetch_donors_by_surname(connection, surname):
    with connection:
        return connection.execute(GET_DONORS_BY_SURNAME, (surname,)).fetchall()

def fetch_donors_by_age(connection, age):
    with connection:
        return connection.execute(GET_DONORS_BY_AGE, (age,)).fetchall()

def fetch_donors_by_sex(connection, sex):
    with connection:
        return connection.execute(GET_DONORS_BY_SEX, (sex,)).fetchall()

def fetch_donors_by_type(connection, bloodtype):
    with connection:
        return connection.execute(GET_DONORS_BY_TYPE, (bloodtype,)).fetchall()

def update_blood_quantity_in_db(connection, name, surname, quantity):
    with connection:
        connection.execute(UPDATE_BLOOD_QUANTITY,(quantity, name, surname, ))
        connection.commit()
         
def remove_donor(connection, name, surname):
    with connection:
        return connection.execute(DELTE_DONOR,(name, surname,))
