import translator as tr
#
t = tr.Translator()
t.loadDictionary("dictionary.txt")

while True:
    t.printMenu()
    choice = input("Seleziona un'opzione: ")

    if choice == "1":
        entry = input("Inserisci la parola e le traduzioni: ")
        t.handleAdd(entry)
    elif choice == "2":
        query = input("Inserisci la parola da tradurre: ")
        t.handleTranslate(query)
    elif choice == "3":
        query = input("Inserisci la parola con wildcard (?): ")
        t.handleWildCard(query)
    elif choice == "4":
        print("Uscita...")
        t.dict.saveDictionary("dictionary.txt")
        break
    else:
        print("Scelta non valida. Riprova.")