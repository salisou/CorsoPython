# Introduzione alla lista (Operazioni base e comprehensions)

# Obiettivo:
#       mostrare come creare, modificare e interrogare liste; interrogare liste comprehensions

voti = [28, 23, 22, 18, 30, 5, 10]
# inserimento alla ista dei voti (append())
voti.append(24)

#Inserice un voto in una posizione specifica
voti.insert(2, 24)
# Rimuove un voto specifico (prima occorrenza)
voti.remove(18)

# Rimuovere e ottenere l'ultimo element
numeri = voti.pop()

# Accesso con indice (0)
primo_voto = voti[4]

# Restituisce gli ultimi 2 numeri
ulitimi_due = voti[-2:]

# Lunghezza della lista
n = len(voti)

# somma, media, min, max
somma = sum(voti) # somma degli elementi
media = somma / n if n > 0 else 0
minimo = min(voti)
maximo = max(voti)

voti_alti = [v for v in voti if v >= 27]

voti_ordinari = sorted(voti)


# Stampa risultati
print("Voti", voti)
print("Promo elemento del voto", primo_voto)
print("Primo voto", primo_voto)
print("N:", n, "Somma:", somma, "Min:", minimo, "Max:", maximo)
print("Voti >= 27", voti_alti)
print("Voti ordinari:", voti_ordinari)



