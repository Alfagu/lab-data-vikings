# Project lab-data-vikings
import random


# Soldier (constructor, ataque y daño)
class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength

    def receive_damage(self, damage):
        self.health = self.health - damage

# Viking
class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health = health, strength = strength)
        self.name = name

    def receive_damage(self, damage):
        super().receive_damage(damage)
        if self.health > 0:
            return(self.name+" has received "+str(damage)+" points of damage")
        else:
            return(self.name+" has died in act of combat")

    def battle_cry(self):
        return("Odin Owns You All!")

# Saxon
class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health = health, strength = strength)

    def receive_damage(self, damage):
        super().receive_damage(damage)
        if self.health > 0:
            return("A Saxon has received "+str(damage)+" points of damage")
        else:
            return("A Saxon has died in combat")

# War
class War:
    def __init__(self, viking_army = [], saxon_army = []):
        self.viking_army = viking_army
        self.saxon_army = saxon_army
    def add_viking(self):
        pass
    def add_saxon(self):
        pass
    def viking_attack(self):
        pass
    def saxon_attack(self):
        pass
    def show_status(self):
        pass
