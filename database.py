import sqlite3


CREATE_BLOODBANK_TABLE = "CREATE TABLE donors (id INTEGER PRIMERY KEY, name TEXT, surname TEXT, age INTEGER, sex TEXT, type TEXT);"

INSERT_DONOR = "INSERT INTO donors (name, surname, age, sex, type) VALUES(?, ?, ?, ?, ?);"

GET_ALL_DONORS = "SELECT * FROM donors;"
GET_DONORS_BY_NAME = "SELECT * FROM donors WHERE name = ?;"
GET_DONORS_BY_SURNAME = "SELECT * FROM donors WHERE surname = ?;"
GET_DONORS_BY_AGE = "SELECT * FROM donors WHERE age = ?;"
GET_DONORS_BY_SEX = "SELECT * FROM donors WHERE sex = ?;"
GET_DONORS_BY_TYPE = "SELECT * FROM donors WHERE type = ?;"


def connect_db():
    return sqlite3.connect("blood-bank-sql/bloodbank.db")

def create_table(connection):
    with connection:
        connection.execute(CREATE_BLOODBANK_TABLE)

def add_donor(connection, name, surname, age, sex, type):
    with connection:
        connection.execute(INSERT_DONOR, (name, surname, age, sex, type))

def get_all_donors(connection):
    with connection:
        return connection.execute(GET_ALL_DONORS).fetchall()

def get_donors_by_name(connection, name):
    with connection:
        return connection.execute(GET_DONORS_BY_NAME, (name)).fetchall()

def get_donors_by_surname(connection, surname):
    with connection:
        return connection.execute(GET_DONORS_BY_SURNAME, (surname)).fetchall()

def get_donors_by_age(connection, age):
    with connection:
        return connection.execute(GET_DONORS_BY_AGE, (age)).fetchall()

def get_donors_by_sex(connection, sex):
    with connection:
        return connection.execute(GET_DONORS_BY_SEX, (sex)).fetchall()

def get_donors_by_type(connection, type):
    with connection:
        return connection.execute(GET_DONORS_BY_TYPE, (type)).fetchall()

