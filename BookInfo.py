# All infromation has been pulled from 5e.tools (https://5etools-mirror-1.github.io/)
# JSON files have been slightly reformated
import json
class BookInfo:
    def __init__(self):
        self.Info = {}
        spellFile = open("data/book/spells.json", "r", encoding = "utf-8")
        dictionaryFile = open("data/book/simple_english_dictionary.json", "r", encoding = "utf-8")
        self.Info["spells"] = (json.load(spellFile))
        self.Info["dict"] = (json.load(dictionaryFile))

    def info(self, term):
        return self.Info["spells"][term]
    
    def define(self, term):
        return self.Info["dict"].get(term)

    def titleCase(self, s):
        return " ".join(word[0].upper()+word[1:] for word in s.split(" "))