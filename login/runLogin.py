import getpass
from db import connect_to_db, connection_close_db


def login_data_validate(con, username, password):
    with con.cursor() as cursor:
        sql = 'SELECT * FROM userlogdata WHERE usernamecl = ?'
        cursor.execute(sql, [username])
        result = cursor.fetchone()

        if result is not None:
            sql = 'SELECT * FROM userlogdata WHERE usernamecl = ? AND userpasswordcl = ?'
            cursor.execute(sql, [username, password])
            result = cursor.fetchone()
            if result:
                print("\n Login OK")
            else:
                print("Login failed")
        else:
            print("Login failed")
        return result


def runLogin():
    con = connect_to_db()
    user_test = input("Your username: ")
    user_password = input("Your password: ")
    if con:
        login_data_validate(con, user_test, user_password)
        connection_close_db(con)


if __name__ == "__main__":
    while True:
        runLogin()
