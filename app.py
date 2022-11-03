import database


def menu():
    connection = database.connect_db()
    database.create_table(connection)



