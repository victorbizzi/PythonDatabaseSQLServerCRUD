import sqlite3
from pathlib import Path
import pyodbc
import globalVars


def connect_to_db():
    con_str = globalVars.connectionString
    try:
        con = pyodbc.connect(con_str)
        print("\n ############### \n Connection successful \n ###############")
        return con
    except Exception as e:
        print(f"Error: {e}")

def connection_close_db(con):
    con.close()
    print("\n ############### \n Connection closed \n ###############")
