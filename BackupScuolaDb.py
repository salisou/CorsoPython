# ---------------------------------------------------------
#  GESTIONALE COMPLETO CON BACKUP + DASHBOARD GRAFICA
# ---------------------------------------------------------

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pyodbc
import pandas as pd
import matplotlib.pyplot as plt
import os

# ---------------------------------------
# PARAMETRI DI CONNESSIONE AL DATABASE
# ---------------------------------------

DRIVER_NAME = "ODBC Driver 17 for SQL Server"
SERVER_NAME = r"(localdb)\ServerPythonSql"
DATABASE_NAME = "ScuolaDb"

conn_str = f"""
    Driver={{{DRIVER_NAME}}};
    Server={SERVER_NAME};
    Database={DATABASE_NAME};
    Trusted_Connection=yes;
    Encrypt=no;
"""


# ---------------------------------------
# FUNZIONI DATABASE
# ---------------------------------------

def get_tables():
    """Restituisce tutte le tabelle presenti nel database."""
    try:
        conn = pyodbc.connect(conn_str)
        query = """
        SELECT TABLE_NAME 
        FROM INFORMATION_SCHEMA.TABLES 
        WHERE TABLE_TYPE = 'BASE TABLE'
        """
        df = pd.read_sql(query, conn)
        conn.close()
        return df["TABLE_NAME"].tolist()

    except Exception as e:
        messagebox.showerror("ERRORE", str(e))
        return []


# ---------------------------------------
# BACKUP DI TUTTE LE TABELLE
# ---------------------------------------

def backup_all():
    try:
        formato = combo_formato.get()
        if not formato:
            messagebox.showerror("⚠️ ATTENZIONE", "Seleziona un formato di backup!")
            return

        tables = get_tables()
        if not tables:
            messagebox.showerror("ERRORE", "Nessuna tabella trovata!")
            return

        conn = pyodbc.connect(conn_str)

        # ------- EXCEL (tutte le tabelle in un file) -------
        if formato == "Excel":
            file_path = filedialog.asksaveasfilename(
                defaultextension=".xlsx",
                filetypes=[("Excel", "*.xlsx")]
            )

            if not file_path:
                return

            with pd.ExcelWriter(file_path, engine="openpyxl") as writer:
                for t in tables:
                    df = pd.read_sql(f"SELECT * FROM {t}", conn)
                    df.to_excel(writer, sheet_name=t, index=False)

            messagebox.showinfo("OK", f"Backup salvato in: {file_path}")

        # ------- CSV / JSON / XML (file separati) -------
        else:
            folder = filedialog.askdirectory(title="Seleziona cartella")
            if not folder:
                return

            for t in tables:
                df = pd.read_sql(f"SELECT * FROM {t}", conn)

                path = os.path.join(folder, f"{t}.{formato.lower()}")

                if formato == "CSV":
                    df.to_csv(path, index=False)
                elif formato == "JSON":
                    df.to_json(path, orient="records", indent=4)
                elif formato == "XML":
                    df.to_xml(path, index=False)

            messagebox.showinfo("OK", f"Backup {formato} salvato in:\n{folder}")

        conn.close()

    except Exception as e:
        messagebox.showerror("❌ ERRORE", str(e))


# ---------------------------------------
# DASHBOARD GRAFICA AUTOMATICA
# ---------------------------------------

def mostra_dashboard():
    """Mostra automaticamente grafici per tutte le tabelle."""
    try:
        tables = get_tables()
        if not tables:
            messagebox.showerror("Errore", "Nessuna tabella trovata.")
            return

        conn = pyodbc.connect(conn_str)

        for t in tables:
            df = pd.read_sql(f"SELECT * FROM {t}", conn)

            # Mostra un grafico SOLO per colonne numeriche
            numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns

            if len(numeric_cols) >= 1:
                plt.figure(figsize=(7,4))
                df[numeric_cols].sum().plot(kind="bar")
                plt.title(f"Dashboard Tabella: {t}")
                plt.xlabel("Campi numerici")
                plt.ylabel("Valori totali")
                plt.grid()
                plt.show()

        conn.close()

    except Exception as e:
        messagebox.showerror("❌ Errore Dashboard", str(e))


# ---------------------------------------
# MOSTRA DATI IN UNA FINESTRA
# ---------------------------------------

def mostra_tabelle():
    """Apre una finestra con tutte le tabelle e i loro record."""
    try:
        conn = pyodbc.connect(conn_str)

        win2 = tk.Toplevel(win)
        win2.title("Visualizza dati")
        win2.geometry("700x500")

        tabs = ttk.Notebook(win2)
        tabs.pack(fill="both", expand=True)

        for t in get_tables():
            frame = ttk.Frame(tabs)
            tabs.add(frame, text=t)

            df = pd.read_sql(f"SELECT * FROM {t}", conn)

            tree = ttk.Treeview(frame, columns=list(df.columns), show="headings")
            tree.pack(fill="both", expand=True)

            # Intestazioni
            for col in df.columns:
                tree.heading(col, text=col)
                tree.column(col, width=120)

            # Inserimento dati
            for _, row in df.iterrows():
                tree.insert("", tk.END, values=list(row))

        conn.close()

    except Exception as e:
        messagebox.showerror("❌ Errore Visualizzazione", str(e))


# ---------------------------------------
# INTERFACCIA GRAFICA TKINTER
# ---------------------------------------

win = tk.Tk()
win.title("Backup & Dashboard - ScuolaDb")
win.geometry("450x350")

frm = ttk.Frame(win, padding=20)
frm.pack(fill="both", expand=True)

ttk.Label(frm, text="Seleziona Formato Backup:", font=("Arial", 12)).pack(pady=10)

combo_formato = ttk.Combobox(frm, values=["Excel", "CSV", "JSON", "XML"], state="readonly")
combo_formato.pack(pady=5)

# Pulsanti
ttk.Button(frm, text="📂 Backup Tutte le Tabelle", command=backup_all).pack(pady=10)
ttk.Button(frm, text="📊 Mostra Dashboard Grafica", command=mostra_dashboard).pack(pady=10)
ttk.Button(frm, text="📋 Mostra Tabelle & Dati", command=mostra_tabelle).pack(pady=10)

win.mainloop()
