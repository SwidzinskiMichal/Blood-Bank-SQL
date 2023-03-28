import sqlite3
import pytest
from database import add_donor, remove_donor, update_blood_quantity_in_db, custom_search
CREATE_BLOODBANK_TABLE = "CREATE TABLE IF NOT EXISTS donors (id INTEGER PRIMARY KEY, name TEXT, surname TEXT, age TEXT, sex TEXT, bloodtype TEXT, quantity INTEGER);"
GET_DONOR_BY_ID = "SELECT * FROM donors WHERE id = ?;"
DELTE_DONOR = "DELETE FROM donors WHERE id = ?;" 

@pytest.fixture
def db_cursor():
    connection = sqlite3.connect(":memory:")
    connection.execute(CREATE_BLOODBANK_TABLE)
    cursor = connection.cursor()
    yield cursor

def test_add_donor(db_cursor):
    donor = ("Kuba", "Kowalski", "55", "Male", "0", 450)
    result = add_donor(db_cursor, *donor)
    assert donor == result[1:]

def test_delete_donor(db_cursor):
    donor = ("Adam", "Kowalski", "55", "Male", "0", 450)
    result = add_donor(db_cursor, *donor)
    assert donor == result[1:]
    id = result[0]
    remove_donor(db_cursor, id)
    assert db_cursor.execute(GET_DONOR_BY_ID, (result[0],)).fetchone() is None

def test_update_blood_quantity(db_cursor):
    donor = ("Tom", "Kowalski", "55", "Male", "0", 450)
    result = add_donor(db_cursor, *donor)
    assert donor == result[1:]
    id = result[0]
    update_blood_quantity_in_db(db_cursor, 100, id)
    assert db_cursor.execute(f'SELECT quantity FROM donors WHERE id = {id};').fetchone() == (100,) 

def test_search(db_cursor):
    donor = ("Ashley", "Adams", "25", "Female", "0", 450)
    result = add_donor(db_cursor, *donor)
    assert donor == result[1:]
    id = result[0]
    custom_search(db_cursor, "name = 'Ashley'")
    assert db_cursor.execute(f'SELECT name FROM donors WHERE id = {id};').fetchone() == ('Ashley',)
    custom_search(db_cursor, "surname = 'Adams'")
    assert db_cursor.execute(f'SELECT surname FROM donors WHERE id = {id};').fetchone() == ('Adams',)
    custom_search(db_cursor, "age = '25'")
    assert db_cursor.execute(f'SELECT age FROM donors WHERE id = {id};').fetchone() == ('25',)
    custom_search(db_cursor, "sex = 'Female'")
    assert db_cursor.execute(f'SELECT sex FROM donors WHERE id = {id};').fetchone() == ('Female',)
    custom_search(db_cursor, "bloodtype = '0'")
    assert db_cursor.execute(f'SELECT bloodtype FROM donors WHERE id = {id};').fetchone() == ('0',)
    paramiters = "name = 'Ashley' AND surname = 'Adams' AND age = '25' AND sex = 'Female' AND bloodtype = '0'"
    custom_search(db_cursor, paramiters)
    assert db_cursor.execute(f'SELECT * FROM donors WHERE id = {id};').fetchone() == (id, 'Ashley', 'Adams', '25', 'Female', '0', 450)




