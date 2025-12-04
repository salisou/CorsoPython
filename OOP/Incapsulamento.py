# Incapsulamento
#=====================================================================
#
#=====================================================================
class ContoBancario:
    # Costruttore della calasse
    def __init__(self, saldo = 0):
        self._saldo = saldo # attributo privata (private)

    # Metodo
    def deposita(self, importo):
        if importo <= 0:
            raise ValueError("L'importo da depositare deve essere positivo.")
        self._saldo += importo

    def preleva(self, importo):
        if importo <= 0:
            raise ValueError("L'importo da prelevare deve essere positivo.")
        if importo > self._saldo:
            raise ValueError("Saldo insufficiente.")
        self._saldo -= importo

    def saldo(self):
        return self._saldo

    def __str__(self):
        return f"Saldo attuale: {self._saldo}€"

conto = ContoBancario(20)
print(conto)  # -> "Saldo attuale: 10 000€"
