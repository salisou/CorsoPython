from tkinter import messagebox

import matplotlib.pyplot as plt
import pandas as pd
import pyodbc as db
from sqlalchemy import true

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
    query2 = "EXEC sp_MediaVotiPerStudente;"
    df = pd.read_sql(query, conn)
    df2 = pd.read_sql(query2, conn)
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
    plt.title("Distribuzione di studenti per corso")
    plt.show()

    # 3 Grafico
    plt.figure(figsize=(10, 5))
    plt.plot(df['NomeCorso'], df['NumeroStudenti'], marker='o')
    plt.title('Numero di studenti per corso')
    plt.xlabel('Nome Corso')
    plt.ylabel('Numero studenti')
    plt.xticks(rotation=40, ha='right')
    plt.grid(True)
    plt.tight_layout()
    plt.show()
except Exception as e:
    messagebox.showerror("Error", e)