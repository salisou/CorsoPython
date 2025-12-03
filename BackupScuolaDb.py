# ============================================================
#   GESTIONALE BACKUP + DASHBOARD DATABASE SQL SERVER
# ============================================================

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pyodbc as odbc
import pandas as pd
import matplotlib.pyplot as plt
import os

# --- PARAMETRI DI CONNESSIONE SQL SERVER ---
DRIVER_NAME = "ODBC Driver 17 for SQL Server"
SERVER_NAME = r"(localdb)\ServerPythonSql"
DATABASE_NAME = "ScuolaDb"

conn_str = f"""
    DRIVER={{{DRIVER_NAME}}};
    SERVER={SERVER_NAME};
    DATABASE={DATABASE_NAME};
    Trusted_Connection=yes;
    Encrypt=no;
"""

# connessione
def get_connection():
    return odbc.connect(conn_str)

# ============================================================
# FUNZIONE: recupera lista tabelle
# ============================================================
def get_tables():
    try:
        conn = odbc.connect(conn_str)
        query = """
            SELECT TABLE_NAME
            FROM INFORMATION_SCHEMA.TABLES
            WHERE TABLE_TYPE = 'BASE TABLE'
        """

        df = pd.read_sql(query, conn)
        conn.close()
        return df['TABLE_NAME'].tolist()
    except Exception as ex:
        messagebox.showerror("Error", f"Errore durante lettura tabelle:\n{str(ex)}")
        return []

# ============================================================
# FUNZIONE: BACKUP COMPLETO DATABASE icon list (⚠️🚫⛔❌‼)
# ============================================================
def backup_all():
    try:
        formato = combo_formato.get()
        if not formato:
            messagebox.showerror("⚠️️ Attenzione!", "Formato non valido‼️")
            return
        tables = get_tables()
        if not tables:
            messagebox.showerror("⛔ Errore", "Nessuna tabella trovata")
            return

        conn = odbc.connect(conn_str)

        # -------SALVATAGGIO EXCEL-------
        # if formato == "Excel":
        #     file_path = filedialog.askopenfilename(
        #         defaultextension=".xlsx",
        #         filetypes=[("Excel", "*.xlsx")],
        #     )
        if formato == "Excel":
            file_path = filedialog.asksaveasfilename(
                defaultextension=".xlsx",
                filetypes=[("Excel", "*.xlsx")],
                title="Salva Backup Excel"
            )
            if not file_path:
                return

            with pd.ExcelWriter(file_path, engine="openpyxl") as writer:
                for t in tables:
                    df = pd.read_sql(f"SELECT * FROM {t}", conn)
                    df.to_excel(writer, sheet_name=t, index=False)

            # messagebox.showinfo("Ok", f"Back-Up Excel salvato in:\n{file_pth}")
            messagebox.showinfo("✔️ Backup Eseguito",
                                f"Backup Excel salvato in:\n{file_path}")


            # ----SALVATAGGIO CSV / JSON / XML -------
        else:
            folder = filedialog.askdirectory(title="Cartella di destinazione")
            if not folder:
                return

            for t in tables:
                df = pd.read_sql(f"SELECT * FROM {t}", conn)

                path = os.path.join(folder, f"{t}.{formato.lower()}")

                if formato == "CSV":
                    df.to_csv(path, index=False)
                elif formato == "JSON":
                    df.to_json(path, indent=4, orient="records")
                elif formato == "XML":
                    df.to_xml(path, index=False)

            # messagebox.showerror("Ok", f"Back-Up {formato} salvato in:\n{folder}") # Da Modificare
            messagebox.showinfo("✔️ Backup Eseguito",
                                f"Backup {formato} salvato in:\n{folder}")
        conn.close()
    except Exception as e:
        messagebox.showerror("❌Error", str(e))

# ============================================================
# FUNZIONE: DASHBOARD TABELLE
# ============================================================
def dashboard_tabelle():
    try:
        tables = get_tables()
        if not tables:
            messagebox.showwarning("Errore", "Nessuna tabella trovata.")
            return

        conn = odbc.connect(conn_str)

        tab_names = []
        tab_counts = []

        for t in tables:
            df = pd.read_sql(f"SELECT * FROM {t}", conn)
            tab_names.append(t)
            tab_counts.append(len(df))

        conn.close()

        # --- GRAFICO ---
        plt.figure(figsize=(10, 5))
        plt.bar(tab_names, tab_counts)
        plt.title("Numero di record per tabella")
        plt.ylabel("Record")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    except Exception as e:
        messagebox.showerror("⛔Errore", str(e))

# ============================================================
# INTERFACCIA GRAFICA TKINTER
# ============================================================

win = tk.Tk()
win.title("Back-Up Database Scuola DB + Dashboard")
win.geometry("420x300")

frm = ttk.Frame(win, padding="20")
frm.pack(fill="both", expand=True)

ttk.Label(frm, text="Formato di esportazione:").pack(pady=10)

combo_formato = ttk.Combobox(
    frm,
    values=["Excel", "CSV", "JSON", "XML"],
    state="readonly",
    font=("Segoe UI", 11)
)

combo_formato.pack(pady=5)

ttk.Button(frm, text="📂 Back-Up Tutte le tabelle", command=backup_all).pack(pady=10)
ttk.Button(frm, text="📊 Dashboard Tabelle", command= dashboard_tabelle).pack(pady=5)

win.mainloop()