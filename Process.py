import random as r
from re import S
import Actions
import BookInfo
import Format

class Process:
    
    def __init__(self):
        self.action = Actions.Actions()
        self.book = BookInfo.BookInfo()
        self.format = Format.Format()
    
    def process(self, message):
        pass
    
    # PROCESS ROLL COMMANDS rolls in the format of {number of dice}d{sides}{+/-}{mod} 
    # modifier is optional
    def rollCommand(self, message):
        args = message.split()
        rolls = self.action.getRolls(args)
        return self.format.roll(rolls)

    def macroCommand(self, macro):
        pass

    # GRAB INFO
    def info(self, arg):
        name = ""
        spellName = arg
        spellInfo = self.book.info(arg)
        message = self.format.info(spellName, spellInfo)
        return message
    
    def define(self, arg):
        word = arg
        definition = self.book.define(word)
        return self.format.define(word, definition)