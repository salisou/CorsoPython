import tkinter as tk
from tkinter import ttk, messagebox

import box
import pyodbc
import pandas as pd



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

def mostra():
    """Legge tutti gli studenti dal DB e li mostra nella TextBox."""
    try:
        conn = pyodbc.connect(strCon)  # Connessione al DB
        df = pd.read_sql("SELECT * FROM Studente", conn)  # Query con Pandas
        conn.close()  # Chiude la connessione
        box.delete("1.0", tk.END)  # Pulisce la TextBox
        box.insert(tk.END, df.to_string(index=False))  # Inserisce i dati
    except Exception as e:
        messagebox.showerror("Errore", str(e))  # Mostra errore

def insert():
    """Inserisce un nuovo studente nel db """
    nome = e_nome.get().strip() # legge il nome
    cognome = e_cognome.get().strip() # legge il cognome
    # data_nascita = e_datanascita.get().strip() # legge la data di nascita
    email = e_mail.get().strip() # leggge l'inddirizzo mail

    # Controllo compi vuoti
    if not nome or cognome or not email:
        messagebox.showwarning(f"Attenzione: I campi devono essere compilati")
        return

    try:
        conn = pyodbc.connect(strCon)  # connessione
        cursor = conn.cursor()

        sql = """
                    INSERT INTO Studente (NomeStudente, CognomeStudente, DataNascita, Email)
                    VALUES (?, ?, ?, ?)
                """

        cursor.execute(sql, (nome, cognome, email))
        conn.commit() # salvare le modifiche
        conn.close()  # chiude la connessione
        messagebox.showinfo("Ok", "Studente inserito!") # confermo
        mostra() #aggiiorna la lista
    except Exception as e:
        messagebox.showerror("Errore", str(e))


# GUI
win = tk.Tk()
win.title("Gestione Studente")
win.geometry("600x400")

# Etichette
ttk.Label(win, text="Nome").grid(row=0, column=0, padx=5, pady=5)
ttk.Label(win, text="Cognome").grid(row=0, column=1, padx=5, pady=5)
ttk.Label(win, text="Email").grid(row=0, column=2, padx=5, pady=5)

# Campi input
e_nome = ttk.Entry(win); e_nome.grid(row=1, column=0, padx=5, pady=5)
e_cognome = ttk.Entry(win); e_cognome.grid(row=1, column=1, padx=5, pady=5)
e_mail = ttk.Entry(win); e_mail.grid(row=1, column=2, padx=5, pady=5)

# Pulsanti
ttk.Button(win, text="Mostra", command=mostra).grid(row=2, column=0, padx=5, pady=10)
ttk.Button(win, text="Inserisci", command=insert).grid(row=2, column=1, padx=5, pady=10)

# Area testo per mostrare dati
box = tk.Text(win, width=70, height=15)
box.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

win.mainloop()
