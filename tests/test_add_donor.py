import sqlite3
import pytest
from database import add_donor, remove_donor
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
