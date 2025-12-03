# ============================================================
#   GESTIONALE BACKUP + DASHBOARD DATABASE SQL SERVER
# ============================================================

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pyodbc
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

# ============================================================
# FUNZIONE: recupera lista tabelle
# ============================================================


# ============================================================
# FUNZIONE: BACKUP COMPLETO DATABASE
# ============================================================


# ============================================================
# FUNZIONE: DASHBOARD TABELLE
# ============================================================


# ============================================================
# INTERFACCIA GRAFICA TKINTER
# ============================================================
