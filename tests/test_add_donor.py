import sqlite3
import pytest
from database import add_donor, remove_donor, update_blood_quantity_in_db, fetch_donors_by_id
CREATE_BLOODBANK_TABLE = "CREATE TABLE IF NOT EXISTS donors (id INTEGER PRIMARY KEY, name TEXT, surname TEXT, age INTEGER, sex TEXT, bloodtype TEXT, quantity INTEGER);"
GET_DONOR_BY_ID = "SELECT * FROM donors WHERE id = ?;"
DELTE_DONOR = "DELETE FROM donors WHERE id = ?;" 

@pytest.fixture
def db_cursor():
    connection = sqlite3.connect(":memory:")
    connection.execute(CREATE_BLOODBANK_TABLE)
    cursor = connection.cursor()
    yield cursor

def test_add_donor(db_cursor):
    donor = ("Kuba", "Kowalski", 55, "Male", "0", 450)
    result = add_donor(db_cursor, *donor)
    assert donor == result[1:]

def test_delete_donor(db_cursor):
    donor = ("Adam", "Kowalski", 55, "Male", "0", 450)
    result = add_donor(db_cursor, *donor)
    assert donor == result[1:]
    id = result[0]
    remove_donor(db_cursor, id)
    assert db_cursor.execute(GET_DONOR_BY_ID, (result[0],)).fetchone() is None

def test_update_blood_quantity(db_cursor):
    donor = ("Tom", "Kowalski", 55, "Male", "0", 450)
    result = add_donor(db_cursor, *donor)
    assert donor == result[1:]
    id = result[0]
    update_blood_quantity_in_db(db_cursor, 100, id)
    assert db_cursor.execute(f'SELECT quantity FROM donors WHERE id = {id};').fetchone() == (100,) 

def test_search_by_id(db_cursor):
    donor = ("Bob", "Kowalski", 55, "Male", "0", 450)
    result = add_donor(db_cursor, *donor)
    assert donor == result[1:]
    id = result[0]
    fetch_donors_by_id(db_cursor, id)
    assert db_cursor.execute(f'SELECT name FROM donors WHERE id = {id};').fetchone() == ("Bob",)