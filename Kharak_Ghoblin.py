
import random


class Character:
    def __init__(self, name, health, defense):
        self.health = health
        self.name = name
        self.defense = defense
    
    def is_alive(self):
        return self.health > 0
    
    def get_attack_damage(self):
        pass
    
class Hero(Character):
    def __init__(self, name, health, defense, attacks):
        super().__init__(name, health, defense)
        self.attacks = attacks
        
    def get_attack_damage(self, attack_type, base_damage):
        self.base_damage = base_damage
        if attack_type not in self.attacks:
            raise ValueError(f"{self.name} does not have the {attack_type} ready or learned")
        elif attack_type == "basic":
            return base_damage, self.defense
        elif attack_type == "special":
            return base_damage * 2, self.defense
        elif attack_type == "ultimate":
            return base_damage * 3, self.defense
        

class Enemy(Character):
    def __init__(self, name, health, defense, damage):
        super().__init__(name, health, defense)
        self.damage = damage
    
    def get_attack_damage(self):
        return self.damage, self.defense

    

class Fight:
    def __init__(self, hero, enemy):
        self.hero = hero
        self.enemy = enemy
        
    def start_fight(self):
        print(f"{self.hero.name} vs {self.enemy.name} - FIGHT !!!")
        loop = 0
        while self.hero.is_alive() and self.enemy.is_alive():
            loop += 1
            print(f"\nROUND {loop}")
            user_dec = input("what type of attack to strike with ? ")
            enemy_damage, enemy_defense = self.enemy.get_attack_damage()
            base_damage, hero_defense = self.hero.get_attack_damage(user_dec, random.randint(1, 10))
            prevent_minus_dmg = lambda damage, defense: max(damage - defense, 0)
            self.hero.health -= prevent_minus_dmg(enemy_damage, hero_defense)
            self.enemy.health -= prevent_minus_dmg(base_damage, enemy_defense)
            print(f"{self.hero.name} attacked with {user_dec} strike for {base_damage} damage, and has a defense of {hero_defense}")
            print(f"{self.enemy.name} attacked for {enemy_damage} and it´s defense is {enemy_defense}")
            print(f"{self.hero.name} ({self.hero.health}) - {self.enemy.name} ({self.enemy.health})")
        if self.hero.is_alive():
            print(f"{self.hero.name} wins!")
        else:
            print(f"{self.enemy.name} wins!")


hero = Hero("Hero", 100, random.randint(1, 6), ["basic", "special", "ultimate"])
enemy = Enemy("Enemy", 100, random.randint(1, 6), random.randint(1, 10))
fight = Fight(hero, enemy)
fight.start_fight()

