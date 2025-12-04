#=========================================================================
# Una classe è modello (o stampo) che descrive un tipo di oggetto
# Definisce:
#       Attributi/proprietà -> caratteristiche dell'oggetto (es: nome, cognome, età ecc...)
#       Metodi -> azioni che l'oggetto può compilare (calcolare, stampare, salvare ecc...)
#=========================================================================


class Persona:
    # name = "Moussa"
    # Cognome = "Salisou"

    def __init__(self, _name, _cognome, _eta):
        self.name = _name # proprietà
        self.cognome = _cognome
        self.eta = _eta

    def saluta(self):
        print(f"Caio mi chiamo {self.name} {self.cognome} e ho {self.eta} anni.")

#
# p = Persona("Marco", "Pippo", 35)
# p.saluta()


class Rettangolo:
    def __init__(self, _base, _altezza):
        self.base = _base
        self.altezza = _altezza

    def area(self):
        area = self.base * self.altezza
        return print("L'area: ", area)



r = Rettangolo(50, 2)
print(r.area())
print("Altezza: ", r.altezza)



