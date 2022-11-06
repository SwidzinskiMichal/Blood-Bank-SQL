import sqlite3


CREATE_BLOODBANK_TABLE = "CREATE TABLE IF NOT EXISTS donors (id INTEGER PRIMARY KEY, name TEXT, surname TEXT, age INTEGER, sex TEXT, bloodtype TEXT, quantity INTEGER);"

INSERT_DONOR = "INSERT INTO donors (name, surname, age, sex, bloodtype, quantity) VALUES (?, ?, ?, ?, ?, ?);"

GET_ALL_DONORS = "SELECT * FROM donors;"
GET_DONOR_BY_ID = "SELECT * FROM donors WHERE id = ?;"
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
DELTE_DONOR = "DELETE FROM donors WHERE id = ?;" 
                


def connect_db():
    connection = sqlite3.connect("blood-bank-sql/bloodbank.db")
    cursor = connection.cursor()
    return cursor

def create_table(cursor):
    cursor.execute(CREATE_BLOODBANK_TABLE)

def add_donor(cursor, name, surname, age, sex, bloodtype, quantity):
    cursor.execute(INSERT_DONOR, (name, surname, age, sex, bloodtype, quantity,))
    id = cursor.lastrowid
    cursor.connection.commit()
    return cursor.execute("SELECT * FROM donors WHERE id = ?;", (id,)).fetchone()     

def fetch_all_donors(cursor):
    return cursor.execute(GET_ALL_DONORS).fetchall()

def fetch_donors_by_id(cursor):
    return cursor.execute(GET_DONOR_BY_ID).fetchone()

def fetch_type_quantity(cursor):
    return cursor.execute(GET_TYPE_QUANTITY).fetchall()

def fetch_donors_by_name(cursor, name):
    return cursor.execute(GET_DONORS_BY_NAME, (name,)).fetchall()

def fetch_donors_by_surname(cursor, surname):
    return cursor.execute(GET_DONORS_BY_SURNAME, (surname,)).fetchall()

def fetch_donors_by_age(cursor, age):
    return cursor.execute(GET_DONORS_BY_AGE, (age,)).fetchall()

def fetch_donors_by_sex(cursor, sex):
    return cursor.execute(GET_DONORS_BY_SEX, (sex,)).fetchall()

def fetch_donors_by_type(cursor, bloodtype):
    return cursor.execute(GET_DONORS_BY_TYPE, (bloodtype,)).fetchall()

def update_blood_quantity_in_db(cursor, name, surname, quantity):
    cursor.execute(UPDATE_BLOOD_QUANTITY,(quantity, name, surname, ))
         
def remove_donor(cursor, id):
    cursor.execute(DELTE_DONOR,(id,))
    cursor.connection.commit()

