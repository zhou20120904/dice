import random as r
class Dice():
    def __init__(self, sides):
        self.sides = sides
    def roll(self):
        return r.randint(1,self.sides)
    def allSide(self):
        return list(range(1,self.sides))
    def count(self,times):
        rolls={}
        for i in range(times):
            try:
                rolls[self.roll()]+=1
            except:
                rolls[self.roll()]=1
        return list(rolls.values())