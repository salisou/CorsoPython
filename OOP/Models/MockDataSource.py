# SORGENTE DATI MOCK (DATI FINTI)
from OOP.Models.Patient import Patient

class MockDataSource:
    def load_patients(self):
        return [
            Patient("Patient_1", "F", 14, "Cardiology", "Admitted"),
            Patient("Patient_10", "M", 14, "Maternity", "Admitted"),
            Patient("Patient_94", "F", 84, "Pediatrics", "Discharged"),
        ]
