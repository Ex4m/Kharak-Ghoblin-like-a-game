
import random


class Character:
    def __init__(self, name, health):
        self.health = health
        self.name = name
    
    def is_alive(self):
        return self.health > 0
    
    def get_attack_damage(self):
        pass
    
class Hero(Character):
    def __init__(self, name, health, damage):
        super().__init__(name, health)
        self.damage = damage
        
    def get_attack_damage(self):
        return self.damage

class Enemy(Character):
    def __init__(self, name, health, damage):
        super().__init__(name, health)
        self.damage = damage
    
    def get_attack_damage(self):
        return self.damage


class Fight:
    def __init__(self, hero, enemy):
        self.hero = hero
        self.enemy = enemy
        
    def start_fight(self):
        print(f"{self.hero.name} vs {self.enemy.name} - FIGHT !!!")
        while self.hero.is_alive() and self.enemy.is_alive():
            self.hero.health -= self.enemy.get_attack_damage()
            self.enemy.health -= self.hero.get_attack_damage()
            print(f"{self.hero.name} ({self.hero.health}) - {self.enemy.name} ({self.enemy.health})")
        if self.hero.is_alive():
            print(f"{self.hero.name} wins!")
        else:
            print(f"{self.enemy.name} wins!")


hero = Hero("Hero", 100, random.randint(1, 10))
enemy = Enemy("Enemy", 100, random.randint(1, 10))
fight = Fight(hero, enemy)
fight.start_fight()


