
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
        elif attack_type == "stun":
            return round(base_damage * 0.5, None), self.defense
        

 
class Enemy(Character):
    def __init__(self, name, health, defense, damage):
        super().__init__(name, health, defense)
        self.damage = damage
    
    def get_attack_damage(self, defense, damage):
        self.defense = defense
        self.damage = damage
        return self.damage, self.defense

    

class Fight:
    def __init__(self, hero, enemy):
        self.hero = hero
        self.enemy = enemy
        
    def start_fight(self):
        print(f"{self.hero.name} vs {self.enemy.name} - FIGHT !!!")
        loop = 0
        stunloop = 0

        def battle_round(stunloop, user_dec):
            enemy_damage, enemy_defense = self.enemy.get_attack_damage(random.randint(1,6), random.randint(1,10))
            base_damage, hero_defense = self.hero.get_attack_damage(user_dec, random.randint(1,6))
            prevent_minus_dmg = lambda damage, defense: max(defense - damage, 0)
            if stunloop == 0:
                self.hero.health -= prevent_minus_dmg(hero_defense, enemy_damage)
                self.enemy.health -= prevent_minus_dmg(enemy_defense, base_damage)
                print(f"{self.hero.name} attacked with {user_dec} strike for {base_damage} damage, and has a defense of {hero_defense}")
            elif stunloop == 1:
                print(f"{self.hero.name} attacked with {user_dec} strike for {base_damage} damage, and has a defense of {hero_defense}. Enemy is dazed from previsious round")
                self.hero.health -= prevent_minus_dmg(hero_defense, 0)
                self.enemy.health -= prevent_minus_dmg( round(enemy_defense * 0.5, None), base_damage)
            print(f"{self.enemy.name} attacked for {enemy_damage} and it´s defense is {enemy_defense}")
            print(f"{self.hero.name} ({self.hero.health}) - {self.enemy.name} ({self.enemy.health})")

        while self.hero.is_alive() and self.enemy.is_alive():
            loop += 1
            print(f"\nROUND {loop}")
            user_dec = input("what type of attack to strike with ? ")

            battle_round(stunloop, user_dec)

            if user_dec == "stun":
                stunloop += 1 
            
        if self.hero.is_alive():
            print(f"{self.hero.name} wins!")
        else:
            print(f"{self.enemy.name} wins!")


def dice_throw(how_many_sides):
    random.seed()
    return random.randint(1,how_many_sides)


hero = Hero("Hero", 100, random.randint(1,6), ["basic", "special", "ultimate", "stun"])
enemy = Enemy("Enemy", 100, random.randint(1,6), random.randint(1,10))
fight = Fight(hero, enemy)
fight.start_fight()

