
import pyodbc as db
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

# Connessione al DB
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

def crea_studente():
    nome = input("Inserisci il Nome: ").strip()
    cognome = input("Inserisci il Cognome: ").strip()
    data_nascita = input("Inserisci la Data di Nascita (YYYY-MM-DD): ").strip()
    email = input("Inserisci l'Email: ").strip()

    if not nome or not cognome or not data_nascita or not email:
        print("⚠️ Tutti i campi sono obbligatori!")
        return

    try:
        datetime.strptime(data_nascita, "%Y-%m-%d")
    except ValueError:
        print("⚠️ Formato data non valido (usa YYYY-MM-DD)")
        return

    try:
        with db.connect(strCon) as connection:
            with connection.cursor() as cursor:
                sql = """
                    INSERT INTO Studente (NomeStudente, CognomeStudente, DataNascita, Email)
                    VALUES (?, ?, ?, ?)
                """
                cursor.execute(sql, [nome, cognome, data_nascita, email])
                connection.commit()
                print("✅ Studente inserito correttamente 🎉")
    except Exception as e:
        print(f"❌ Errore durante l'inserimento: {e}")

def leggi_studenti():
    try:
        with db.connect(strCon) as connection:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM Studente"
                cursor.execute(sql)
                rows = cursor.fetchall()

                if not rows:
                    print("⚠️ Nessuno studente trovato.")
                    return

                # Recupera i nome delle colonne
                columns = [desc[0] for desc in  cursor.description]

                # Converti in DataFrame
                df = pd.DataFrame(rows, columns=["ID", "Nome", "Cognome", "DataNascita", "Email"])
                print("\n📋 Lista degli studenti:")
                print(df)


                # Grafico a barre (conteggio studenti per cognome)
                if "CognomeStudente" in df.columns:
                    df["CognomeStudente"].value_counts().plot(kind="bar", title="Studenti per Cognome")
                plt.show()
    except Exception as e:
        print(f"❌ Errore durante la lettura: {e}")
crea_studente()
leggi_studenti()
# Esempio di utilizzo:
# crea_studente()
# leggi_studenti()
