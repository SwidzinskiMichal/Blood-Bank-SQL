import sqlite3


CREATE_BLOODBANK_TABLE = "CREATE TABLE IF NOT EXISTS donors (id INTEGER PRIMARY KEY, name TEXT, surname TEXT, age TEXT, sex TEXT, bloodtype TEXT, quantity INTEGER);"

INSERT_DONOR = "INSERT INTO donors (name, surname, age, sex, bloodtype, quantity) VALUES (?, ?, ?, ?, ?, ?);"

GET_ALL_DONORS = "SELECT * FROM donors;"

GET_TYPE_QUANTITY = """
                    SELECT bloodtype,
                    SUM (quantity)
                    FROM donors
                    GROUP BY bloodtype;
                    """
UPDATE_BLOOD_QUANTITY = "UPDATE donors SET quantity = ? WHERE id = ?;"
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

def custom_search(cursor, search_paramiters):
    return cursor.execute(f"SELECT * FROM donors WHERE {search_paramiters};").fetchall()

def update_blood_quantity_in_db(cursor, quantity, id):
    cursor.execute(UPDATE_BLOOD_QUANTITY,(quantity, id,))
         
def remove_donor(cursor, id):
    cursor.execute(DELTE_DONOR,(id,))
    cursor.connection.commit()

