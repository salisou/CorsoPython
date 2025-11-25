rubrica = {
    100: {
        "nome": "Anna",
        "Cognome": "Barco",
        "Classe": "4A"
    },
    101: {
        "nome": "Marco",
        "Cognome": "Marroni",
        "Classe": "C5"
    },
    103: {
        "nome": "Luca",
        "Cognome": "Russo",
        "Classe": "4B"
    }
}

# Aggiungere un nuovo studente
rubrica[102] = {
    "nome": "Marta",
    "Cognome": "Gialli",
    "Classe": "4C"
}

# Modificare la classe di uno studente specifico
rubrica[101]["Classe"] = "5B"

# Selezionare uno studente in base al Id (indice)
studente = rubrica[102]
# usando una condizione (se trova lo studente dice studente trovato se no studente non trovato)
if studente:
    print("Studente 100:", studente["nome"], studente["Cognome"])
else:
    print(f"Studente con l'indice non trovato!")


if 100 in rubrica:
    del rubrica[100] # rimuove la coppia chiave-valore

#Itere su chiave e valore
for id_studente, info in rubrica.items():
    print(f"Id dello studente: {id_studente}: nome {info["nome"]} Cognome {info["Cognome"]} e la classe {info["Classe"]}")

#