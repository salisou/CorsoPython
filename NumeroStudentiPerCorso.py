from tkinter import messagebox

import matplotlib.pyplot as plt
import pandas as pd
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

try:
    conn = db.connect(strCon)

    # Usa la store procedure
    query = "EXEC sp_NumeroStudentiPerCorso;"
    df = pd.read_sql(query, conn)
    conn.close()

    print(df)

    # 1 Grafico barre
    plt.figure(figsize=(10, 5))
    plt.bar(df['NomeCorso'], df['NumeroStudenti'])
    plt.title('Numero di studenti per corso')
    plt.xlabel('Nome Corso')
    plt.ylabel('Numero studenti')
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.xticks(rotation=40, ha='right')
    plt.tight_layout()
    plt.show()


    # 2 Grafico a torta
    plt.figure(figsize=(8, 8))
    plt.pie(df['NumeroStudenti'], labels=df['NomeCorso'], autopct='%1.1f%%')
    plt.title("Distribuzione studenti per corso")
    plt.show()
except Exception as e:
    messagebox.showerror("Error", e)