
import tkinter as tk
from tkinter import ttk, messagebox, Text
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
        conn = pyodbc.connect(strCon)
        df = pd.read_sql("SELECT * FROM Studente", conn)
        conn.close()
        box.delete("1.0", tk.END)
        box.insert(tk.END, df.to_string(index=False))
    except Exception as e:
        messagebox.showerror("Errore", str(e))

def insert():
    """Inserisce un nuovo studente nel DB"""
    nome = e_nome.get().strip()
    cognome = e_cognome.get().strip()
    data_nascita = e_datanascita.get().strip()
    email = e_mail.get().strip()

    # Controllo campi vuoti
    if not nome or not cognome or not data_nascita or not email:
        messagebox.showwarning("Attenzione", "Tutti i campi devono essere compilati!")
        return

    try:
        conn = pyodbc.connect(strCon)
        cursor = conn.cursor()
        sql = """
            INSERT INTO Studente (NomeStudente, CognomeStudente, DataNascita, Email)
            VALUES (?, ?, ?, ?)
        """
        cursor.execute(sql, (nome, cognome, data_nascita, email))
        conn.commit()
        conn.close()
        messagebox.showinfo("OK", "Studente inserito!")

        # Pulisce i campi dopo inserimento
        e_nome.delete(0, tk.END)
        e_cognome.delete(0, tk.END)
        e_datanascita.delete(0, tk.END)
        e_mail.delete(0, tk.END)

        mostra()  # Aggiorna la lista
    except Exception as e:
        messagebox.showerror("Errore", str(e))

# GUI
win = tk.Tk()
win.title("Gestione Studente")
win.geometry("700x600")

# Etichette
ttk.Label(win, text="Nome").grid(row=0, column=0, padx=5, pady=5)
ttk.Label(win, text="Cognome").grid(row=0, column=1, padx=5, pady=5)
ttk.Label(win, text="Data di nascita (YYYY-MM-GG)").grid(row=0, column=2, padx=5, pady=5)
ttk.Label(win, text="Email").grid(row=0, column=3, padx=5, pady=5)

# Campi input
e_nome = ttk.Entry(win); e_nome.grid(row=1, column=0, padx=5, pady=5)
e_cognome = ttk.Entry(win); e_cognome.grid(row=1, column=1, padx=5, pady=5)
e_datanascita = ttk.Entry(win); e_datanascita.grid(row=1, column=2, padx=5, pady=5)
e_mail = ttk.Entry(win); e_mail.grid(row=1, column=3, padx=5, pady=5)

# Pulsanti
ttk.Button(win, text="Mostra", command=mostra).grid(row=2, column=0, padx=5, pady=10)
ttk.Button(win, text="Inserisci", command=insert).grid(row=2, column=1, padx=5, pady=10)

# Area testo per mostrare dati
box = tk.Text(win, width=80, height=20)
box.grid(row=4, column=0, columnspan=4, padx=10, pady=10)

win.mainloop()
