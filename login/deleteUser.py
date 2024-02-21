from db import connect_to_db, connection_close_db


def printAllUsers(con):
    with con.cursor() as cursor:
        sql = 'SELECT usernamecl FROM userlogdata'
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            print(row.usernamecl)


def deleteConfirmation(con, username_to_delete):
    with con.cursor() as cursor:
        sql = 'DELETE FROM userlogdata WHERE usernamecl = ?;'
        cursor.execute(sql, [username_to_delete])
    con.commit()

def delete_userlogin_data():
    confirmation = input("Do you know the username? Y or N? ")
    if confirmation.lower() == 'y':
        username_to_delete = input("Enter the username: ")
        con = connect_to_db()
        if con:
            deleteConfirmation(con, username_to_delete)
            print(f"User {username_to_delete} has been deleted")
            connection_close_db(con)

        else:
            connection_close_db(con)
            print("User data deletion canceled.")
    else:
        confirmation = input("Would you like to see all users? Y or N? ")
        if confirmation.lower() == 'y':  # Corrected the comparison
            con = connect_to_db()
            if con:
                printAllUsers(con)  # Pass the connection to printAllUsers
                user_del_conf = input("Which user? ")
                con = connect_to_db()
                if con:
                    deleteConfirmation(con, user_del_conf)
                    connection_close_db(con)

        else:
            print("Process finished")


if __name__ == "__main__":
    while True:
        delete_userlogin_data()