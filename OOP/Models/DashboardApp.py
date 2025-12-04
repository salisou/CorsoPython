import tkinter as tk

# Import corretti dei namespace
from OOP.Models.KpiBar import KpiBar
from OOP.Models.StatusService import StatusService
from OOP.Models.MockDataSource import MockDataSource

class DashboardApp:
    def __init__(self, data_source):
        self.root = tk.Tk()
        self.root.title("Dashboard Ospedaliera")
        self.data_source = data_source
        self.patients = self.data_source.load_patients()
        self.stats = StatusService(self.patients)
        self.kpi_bar = KpiBar(self.root)
        self.kpi_bar.update(self.stats)
        self.root.mainloop()

# AVVIO
if __name__ == "__main__":
    app = DashboardApp(MockDataSource())
