# Eredità
from pygments.styles import material


class Persona:
    def __init__(self, name, cognome):
        self.name = name
        self.cognome = cognome

    def saluta(self):
        print("Caio sono " + self.name + " " + self.cognome)

class Insegnante(Persona):
    def __init__(self, _name, _cognome, materia):
        super().__init__(_name, _cognome)
        self._materia = materia

    def saluta(self):
        print("Caio sono " + self.name + " " + self.cognome + " insegno " + self._materia)

p = Persona("Pipp", "toto")
i = Insegnante("Raimond", "Borgo", "Python")


p.saluta()
i.saluta()
