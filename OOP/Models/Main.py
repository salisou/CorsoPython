# MODELLO DATI
class Patient:
    def __init__(self, name, gender, age, department, status):
        self.name = name
        self.gender = gender
        self.age = age
        self.department = department
        self.status = status


# SORGENTE DATI MOCK
class MockDataSource:
    def load_patients(self):
        return [
            Patient("Patient_1", "F", 14, "Cardiology", "Admitted"),
            Patient("Patient_10", "M", 14, "Maternity", "Admitted"),
            Patient("Patient_94", "F", 84, "Pediatrics", "Discharged"),
        ]


# SERVIZIO KPI
class StatsService:
    def __init__(self, patients):
        self.patients = patients

    def total(self):
        return len(self.patients)

    def admitted(self):
        return sum(1 for p in self.patients if p.status == "Admitted")


# VISTA KPI
import tkinter as tk
from tkinter import ttk


class KpiBar:
    def __init__(self, parent):
        self.frame = ttk.Frame(parent, padding=10)
        self.frame.pack(fill="x")
        self.lbl_total = ttk.Label(self.frame, text="Totale: 0")
        self.lbl_total.pack(side="left", padx=10)

    def update(self, stats: StatsService):
        self.lbl_total.configure(text=f"Totale: {stats.total()}")


# APP PRINCIPALE
class DashboardApp:
    def __init__(self, data_source):
        self.root = tk.Tk()
        self.root.title("Dashboard Ospedaliera")
        self.data_source = data_source
        self.patients = self.data_source.load_patients()
        self.stats = StatsService(self.patients)
        self.kpi_bar = KpiBar(self.root)
        self.kpi_bar.update(self.stats)
        self.root.mainloop()


# AVVIO
if __name__ == "__main__":
    app = DashboardApp(MockDataSource())
