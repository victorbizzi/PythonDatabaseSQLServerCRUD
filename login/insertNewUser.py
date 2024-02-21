from datetime import datetime
from db import connect_to_db, connection_close_db


def insert_user(con, username, password, date):
    with con.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) FROM userlogdata WHERE usernamecl = ?", (username,))
        if cursor.fetchone()[0] > 0:
            print("Username already exists. Please choose a different username.")
            return

        sql = 'INSERT INTO userlogdata (usernamecl, userpasswordcl, RegistrationDatecl) VALUES (?, ?, ?);'
        cursor.execute(sql, [username, password, date])
        con.commit()


def add_userlogin_data():
    username = input("What is the username? ")
    password = input("What is the password? ")
    date = datetime.now()

    print(username, password, date)
    confirmation = input("Confirm? Y or N? ")
    if confirmation.lower() == 'y':
        con = connect_to_db()
        if con:
            insert_user(con, username, password, date)
            connection_close_db(con)
            #print("User data addedkoº")
    else:
        print("User data insertion canceled.")


if __name__ == "__main__":
    while True:
        add_userlogin_data()
