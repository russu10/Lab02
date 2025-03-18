import re

from dictionary import Dictionary


class Translator:

    def __init__(self):
        self.dict = Dictionary()

    def printMenu(self):
        print("\n--- Traduttore Alieno ---")
        print("1. Aggiungere una nuova parola")
        print("2. Cercare la traduzione di una parola")
        print("3. Cercare con wildcard (uso di ?)")
        print("4. Uscire")

    def loadDictionary(self, filename):
        self.dict.loadDictionary(filename)

    def handleAdd(self, entry):
        parts = entry.strip().split()
        if len(parts) < 2:
            print("Formato non valido! Usa: <parola_aliena> <traduzione1 traduzione2 ...>")
            return
        word, translations = parts[0], parts[1:]
        if not re.fullmatch("[a-zA-Z]+", word) or not all(re.fullmatch("[a-zA-Z]+", t) for t in translations):
            print("Errore: sono ammessi solo caratteri alfabetici.")
            return
        self.dict.addWord(word, translations)
        print("Parola aggiunta con successo!")

    def handleTranslate(self, query):
        if not re.fullmatch("[a-zA-Z]+", query):
            print("Errore: sono ammessi solo caratteri alfabetici.")
            return
        translations = self.dict.translate(query)
        print(f"Traduzioni per '{query}': {', '.join(translations)}")

    def handleWildCard(self, query):
        if query.count("?") != 1 or not re.fullmatch("[a-zA-Z?]+", query):
            print("Errore: usa una sola wildcard '?' e solo caratteri alfabetici.")
            return
        matches = self.dict.translateWordWildCard(query)
        if matches:
            for word, translations in matches.items():
                print(f"{word}: {', '.join(translations)}")
        else:
            print("Nessuna corrispondenza trovata.")