import pandas as pd

#==================================================
#
#==================================================

df_dict = pd.read_excel("Backup_ScuolaDb.xlsx", sheet_name=None)

# Itera su tutte le foglie di execl che trova
for nome_foglio, df in df_dict.items():
    print(f"\n=== Foglio {nome_foglio} ===")
    print(df)