import re

#
class Dictionary:
    def __init__(self):
        self.dictionary = {}
    def loadDictionary(self,filename):
        try :
            with open(filename,"r", encoding = "utf-8") as file:
                 for line in file:
                    parts = line.strip().split(" ")
                    if len(parts) >1:
                        word,translations = parts[0].lower(),parts[1:]
                        if word in self.dictionary:
                            self.dictionary[word].update(translations)
                        else:
                            self.dictionary[word] = set(translations)
        except FileNotFoundError:
            print("file non trovato")

    def saveDictionary(self,filename):
        with open(filename,"w", encoding = "utf-8") as file:
            for(word,translations) in self.dictionary.items():
                file.write(f"{word} {' '.join(translations)}\n")
    def addWord(self,word,transaltions):
        word = word.lower()
        if word in self.dictionary:
            self.dictionary[word].update(transaltions)
        else:
            self.dictionary[word] = set(transaltions)


    def translate(self,word):
        word = word.lower()
        return self.dictionary.get(word,["no traduzione trovata"])


    def translateWordWildCard(self,query):
        pattern = query.lower().replace("?",".")
        ragex = re.compile((f"^{pattern}$"))
        matches = {word:translations for word,translations in self.dictionary.items()}
        return matches