# All infromation has been pulled from 5e.tools (https://5etools-mirror-1.github.io/)
# JSON files have been slightly reformated
import json
class BookInfo:
    def __init__(self):
        self.Info = {}
        spellFile = open("data/book/spells.json", "r", encoding = "utf-8")
        self.Info["spells"] = (json.load(spellFile))

    def info(self, term):
        return self.Info["spells"][self.titleCase(term)]

    def titleCase(self, s):
        return " ".join(word[0].upper()+word[1:] for word in s.split(" "))

