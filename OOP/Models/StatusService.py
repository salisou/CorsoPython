# SERVIZIO
class StatusService:
    def __init__(self, patients):
        self.patients = patients

    def total(self):
        return len(self.patients)

    def admitted(self):
        return sum(1 for p in self.patients if p.status == "Admitted")
