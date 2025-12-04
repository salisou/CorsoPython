# Eredità
#=========================================================================
# Una classe può ereditare di un altra
# Significa che prendere attributi e metodi della classe "Genitore/Padre"
# e può aggiungerne o modificare.
#=========================================================================

class Animale:
    def parla(self):
        print("Sono genitore")

class Cane(Animale): # eredità da Animale
    def parla(self):
        print("Bau Bau!")


# print("Sono un cane")
# c = Cane()
# c.parla()

# Polimorfismo
#=========================================================================
# Capacità di usare lo stesso metodo su diversi oggetti,
# ottenendo comportamenti differenti
#=========================================================================
animali = [Cane(), Animale()]
for a in animali:
    a.parla() # Cane -> Bau Bau!, Animale -> Sono genitore
