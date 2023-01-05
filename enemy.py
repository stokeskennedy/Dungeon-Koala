from player import *

class Enemy(Player):
    def __str__(self):
        return "Enemy HP: " + str(self.hp), "Enemy ATK: " + str(self.atk)