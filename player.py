from main import *

class Player:
    def __init__(self, hp, atk):
        self.hp = hp
        self.atk = atk
    
    def hp(self):
        return self.hp
    
    def atk(self):
        return self.atk
    
    def __str__(self):
        return "Player HP: " + str(self.hp), "Player ATK:: " + str(self.atk)