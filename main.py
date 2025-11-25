# pip install pyodbc
# python.exe -m pip install --upgrade pip
import pyodbc as db

DRIVER_NAME = "ODBC Driver 17 for SQL Server"
SERVER_NAME = r"(localdb)\ServerPythonSql"
DATABASE_NAME = "ScuolaDb"

strCon = f"""
    Driver={{{DRIVER_NAME}}};
    Server={SERVER_NAME};
    Database={DATABASE_NAME};
    Trusted_Connection=yes;
    Encrypt=no;
"""

connection = db.connect(strCon)
print(connection)
print("la Connessione è OK🎉🎉🎉")