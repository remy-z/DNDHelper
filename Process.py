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
    def roll(self, message):
        args = message.split()
        rolls = []
        for arg in args:
            mod = 0
            num = 0
            sides = 0
            if "+" in arg:
                x = arg.split("+")
                mod += int(x[1])
                x = arg.split("+")
                num, sides = x[0].split("d")
            elif "-" in arg:
                x = arg.split("-")
                mod -= int(x[1])
                num, sides = x[0].split("d")
            else:
                num, sides = arg.split("d")
            rolls.append(self.action.roll(int(num), int(sides), mod))
        return self.format.roll(rolls)

    #GRAB INFO
    def info(self, arg):
        name = ""
        spellName = self.book.titleCase(arg)
        spellInfo = self.book.info(spellName)
        message = self.format.info(spellName, spellInfo)
        return message
           
    def macro(self, ctx, arg):
        return ""