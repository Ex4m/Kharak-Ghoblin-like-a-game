


class Hero:
    def __init__(self, health, damage, inventory):
        self.health = health
        self.damage = damage
        self.inventory = inventory

class Enemy:
    def __init__(self, health, damage, floor):
        self.health = health
        self.damage = damage
        self.floor = floor # 1-4

    