import random as r
class Actions:
    #returns a tuple containing the total of the roll, and a list of all the rolls, the last
    # value of the list as a string with the mod value
    def roll(self, num, sides, mod, arg):
        total = 0
        allRolls = []
        for x in range(num): 
            roll = r.randint(1, sides)
            total += roll
            allRolls.append(roll) 
        total += mod
        if mod > 0:
            allRolls.append(f" + {mod}")
        elif mod < 0:
            allRolls.append(f" - {-mod}")
        else:
            allRolls.append(0)
        return (total, allRolls, arg)