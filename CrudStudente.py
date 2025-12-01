
import tkinter as tk
from datetime import datetime
from tkinter import ttk, messagebox, Text
import pyodbc as odbc
import pandas as pd

from progetto2 import id_studente

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

# ==========================
# FUNZIONI PRINCIPALI
# ==========================
def mostra():
    """Mostra tutti gli studenti nella griglia Treeview"""
    try:
        conn = odbc.connect(strCon)                      # Connessione DB
        df = pd.read_sql("EXEC sp_selectStudenti", conn)   # Legge tutti i record
        conn.close()

        # Cancella righe esistenti nella griglia
        for row in grid.get_children():
            grid.delete(row)

        # Inserisce nuove righe
        for _, r in df.iterrows():
            grid.insert("", tk.END, values=(r["StudenteId"], r["NomeStudente"], r["CognomeStudente"], r["DataNascita"], r["Email"]))
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
        conn = odbc.connect(strCon)
        cursor = conn.cursor()
        sql = """ EXEC sp_InsertStudente ?, ?, ?, ? """

        cursor.execute(sql, (nome, cognome, data_nascita, email))
        conn.commit()
        conn.close()
        messagebox.showinfo("OK", "Studente inserito!")
        pulisci_campi() # pulisce i textBox della forma o Modulo
        mostra()  # Aggiorna la lista
        # Modificare il tipo del'eccezione usando pyodbc.error
    except odbc.Error as e:
        messagebox.showerror("Errore Db",f"Errore durante l'inserimento: {e}")
    except Exception as ex:
        messagebox.showerror("Errore!", f"Errore imprevisto")

###########################################################
#                 Funzioni da creare
###########################################################

#------ Creare una funzione per gestire gli aggiornamenti
def update_by_id():
    """Aggiorna i dati di uno studente in base a l'Id"""
    id_studente = e_id.get().strip()
    nome = e_nome.get().strip()
    cognome = e_cognome.get().strip()
    data_nascita = e_datanascita.get().strip()
    email = e_mail.get().strip()

    # Controllo campi vuoti
    if not id_studente or not nome or not cognome or not data_nascita or not email:
        messagebox.showwarning("Attenzione", "Tutti i campi devono essere compilati!")
        return

    if not id_studente.isdigit():
        messagebox.showerror("Errore", "l'Id deve essere un numero!")
        return

    try:
        conn = odbc.connect(strCon)
        cursor = conn.cursor()
        """ -------Usare la store procedure  per l'aggiornamento"""
        sql = """ EXEC sp_UpdateStudente ?, ?, ?, ?, ? """

        cursor.execute(sql, (id_studente, nome, cognome, data_nascita, email))
        conn.commit()

        if cursor.rowcount > 0:
            messagebox.showinfo("OK", "Studente aggiornato!")
        else:
            messagebox.showwarning("Attenzione", "ID non trovato!")

        pulisci_campi()
        mostra()
    except odbc.Error as db_Err:
        conn.rollback()
        messagebox.showerror("Errore  DB", f"Errore durante l'aggiornamento: {db_Err}")
    except Exception as ex:
        messagebox.showerror("Errore!", f"Errore imprevisto {ex}")
    finally:
        try:
            conn.close()
        except:
            pass
#--------------------------------------------------------

#------ Creare una funzione per Cancellare---------------
def delete_by_id():
    """Elimina uno studente usando l'ID"""
    id_studente = e_id.get().strip()

    if not id_studente:
        messagebox.showwarning("Attenzione", "Inserisci l'ID dello studente da eliminare!")
        return

    if not id_studente.isdigit():
        messagebox.showerror("Errore", "L'ID deve essere un numero intero!")
        return

    try:
        conn = odbc.connect(strCon)
        cursor = conn.cursor()
        sql = "EXEC sp_DeleteStudente ?"
        cursor.execute(sql, (int(id_studente),))
        conn.commit()

        if cursor.rowcount > 0:
            messagebox.showinfo("OK", "Studente eliminato!")
        else:
            messagebox.showwarning("Attenzione", "ID non trovato.")

        pulisci_campi()
        mostra()
    except odbc.Error as db_err:
        conn.rollback()
        messagebox.showerror("Errore DB", f"Errore durante l'eliminazione: {db_err}")
    except Exception as e:
        messagebox.showerror("Errore", f"Errore imprevisto: {e}")
    finally:
        try:
            conn.close()
        except:
            pass
#--------------------------------------------------------

#------ Creare una funzione che Pulisce tutti i campi di input--
def pulisci_campi():
    e_id.delete(0, tk.END)
    e_nome.delete(0, tk.END)
    e_cognome.delete(0, tk.END)
    e_datanascita.delete(0, tk.END)
    e_mail.delete(0, tk.END)
#---------------------------------------------------------------

#-Creare una funzione che Carica i dati della riga selezionata nei campi di input
def carica_dati(event):
    """Carica i dati della riga selezionata nei campi di input"""
    selezione = grid.selection()
    if selezione:
        valori = grid.item(selezione[0], "values")
        e_id.delete(0, tk.END); e_id.insert(0, valori[0])
        e_nome.delete(0, tk.END); e_nome.insert(0, valori[1])
        e_cognome.delete(0, tk.END); e_cognome.insert(0, valori[2])
        e_datanascita.delete(0, tk.END); e_datanascita.insert(0, valori[3])
        e_mail.delete(0, tk.END); e_mail.insert(0, valori[4])
#---------------------------------------------------------------

###########################################################
#                 Fine dei  Funzioni
###########################################################
# ==========================
# GUI
# ==========================
win = tk.Tk()
win.title("Gestione Studente")
win.geometry("850x650")

# Etichette
# Aggiungere StudenteId
ttk.Label(win, text="ID").grid(row=0, column=0, padx=5, pady=5)
ttk.Label(win, text="Nome").grid(row=0, column=1, padx=5, pady=5)
ttk.Label(win, text="Cognome").grid(row=0, column=2, padx=5, pady=5)
ttk.Label(win, text="Data di nascita (YYYY-MM-GG)").grid(row=0, column=3, padx=5, pady=5)
ttk.Label(win, text="Email").grid(row=0, column=4, padx=5, pady=5)

# Campi input
# Aggiungere StudenteId
e_id = ttk.Entry(win); e_id.grid(row=1, column=0, padx=5, pady=5)
e_nome = ttk.Entry(win); e_nome.grid(row=1, column=1, padx=5, pady=5)
e_cognome = ttk.Entry(win); e_cognome.grid(row=1, column=2, padx=5, pady=5)
e_datanascita = ttk.Entry(win); e_datanascita.grid(row=1, column=3, padx=5, pady=5)
e_mail = ttk.Entry(win); e_mail.grid(row=1, column=4, padx=5, pady=5)

# Pulsanti
ttk.Button(win, text="Mostra", command=mostra).grid(row=2, column=0, padx=5, pady=10)
ttk.Button(win, text="Inserisci", command=insert).grid(row=2, column=1, padx=5, pady=10)
########## Pulsanti da aggiungere ###########
# Aggiorna per ID e Elimina per ID
ttk.Button(win, text="Aggiorna per ID", command=update_by_id).grid(row=2, column=2, padx=5, pady=10)
ttk.Button(win, text="Elimina per ID", command=delete_by_id).grid(row=2, column=3, padx=5, pady=10)
##############################################

# Griglia tipo WinForms###########################
columns = ("StudenteId", "Nome", "Cognome", "DataNascita", "Email")
grid = ttk.Treeview(win, columns=columns, show="headings", height=15)

for col in columns:
    grid.heading(col, text=col)
    grid.column(col, width=150)

scrollbar = ttk.Scrollbar(win, orient="vertical", command=grid.yview)
grid.configure(yscroll=scrollbar.set)

grid.grid(row=4, column=0, columnspan=5, padx=10, pady=10)
scrollbar.grid(row=4, column=5, sticky="ns")

# Evento click su riga
grid.bind("<<TreeviewSelect>>", carica_dati)

win.mainloop()
