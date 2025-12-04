from tkinter import ttk
from OOP.Models.StatusService import StatusService  # nome corretto

class KpiBar:
    def __init__(self, parent):
        self.frame = ttk.Frame(parent, padding=10)
        self.frame.pack(fill="x")
        self.lbl_total = ttk.Label(self.frame, text="Totale: 0")
        self.lbl_total.pack(side="left", padx=10)

    def update(self, stats: StatusService):
        self.lbl_total.configure(text=f"Totale: {stats.total()}")
