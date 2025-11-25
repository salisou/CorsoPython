# str => stringa (Testo)
# int => intero (1000000000)
# fload => decimali (2.10)
# bool => boolean (vero/falso) true / false

# Esempio 1:
# nome = "Moussa"
# eta = 45
# altezza = 1.85

# print(f"Mi chiamo {nome} ho {eta} anni e misuro {altezza} m")


# Esercizio 1
# scrivi un programma che memorizza : (nome, cognome, eta e verifica se l'eta è maggiore stampa maggiorenne se non minorenne)
# print('Come ti chiami? ')
# nome = "Giorgio"
# cognome = "Ricci"
# eta = 56
# if eta >= 56:
#     print(f'Ti chiami {nome} {cognome} hai {eta} anni e sei maggiorenne')
# else:
#     print(f'Ti chiami {nome} {cognome} hai {eta} anni e sei minorenne')


# Cicli for e while
# frutti = ["mela", "banana", "pera"]
# for frutto in frutti:
#     print(frutto)
#
# x = 5
#
# while x > 0:
#     print(x)
#     x -= 2


def impor_programmazione(linguaggi):
    print('Ho imparato a programmare in', linguaggi)


### 2025
impor_programmazione("Python")

# Crea una lista che calcola la media di una lista di numeri
# funzione
# numeri = []

# def calcola_media(lista):
#     return sum(lista) / len(lista)
#
# numeri = [10, 20, 30, 40, 50]
# print("La media è:", calcola_media(numeri))

try:
    numero = int(input("Inserire un numero: ")) # abc (1263541)
    if numero == int(0):
       print("inserisci un numero più altro")
    elif numero > int(0):
       print(f"Hai inserito un numero {numero }")
    else:
        print("inserisci un valore")
except ValueError:
    print("Errore non è un numero! ")