import random
import time

class Character:
    def __init__(self, health, attack, defense):
        self.health = health
        self.attack = attack
        self.defense = defense
        self.name = ""

    def set_name(self, name):
        self.name = name

    def is_alive(self):
        return self.health > 0

class Attack:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def swing(self, attacker, defender):
        damage = self.damage + attacker.damage - defender.defense
        damage = max(damage, 0)
        defender.health -= damage
        print(f"{attacker.name} uses {self.name} and does {damage} damage")
        if not defender.is_alive():
            print(f"{defender.name} has been defeated!")
         




class Fight:
    def __init__(self, hero, enemy, attack_types, stun_attack, dot_attack):
        self.hero = hero
        self.enemy = enemy
        self.attack_types = attack_types
        self.stun_attack = stun_attack
        self.dot_attack = dot_attack
        
    def start_fight(self):
        print(f"{self.hero.name} vs {self.enemy.name}")
        loop = 1
        while self.hero.is_alive() and self.enemy.is_alive():
            print(f"\nROUND {loop}")
            self.fight(self.hero, self.enemy, self.attack_types, self.stun_attack, self.dot_attack) # Hero attacks Enemy
            if self.enemy.is_alive():
                self.fight(self.enemy, self.hero, self.attack_types, self.stun_attack, self.dot_attack) # Enemy attacks hero
                time.sleep(1)
            loop += 1

    def fight(self, attacker, defender, attack_types, stun_attack, dot_attack):
        print(f"{attacker.name} attacks {defender.name}")
        attack = random.choice(attack_types)
        damage = attack.damage + attacker.attack - defender.defense
        damage = max(damage, 0)
        defender.health -= damage
        print(f"{attack.name} does {damage} damage")
        if not defender.is_alive():
            print(f"{defender.name} has been defeated!")
        if isinstance(attack, Stun):
            stun_attack.stun(attacker, defender)
        elif isinstance(attack, DotAttack):
            dot_attack.rend(attacker, defender, 3) # assuming 3 rounds for simplicity
        return



class Stun(Attack):
    def __init__(self, name, damage, rounds):
        super().__init__(name,damage)
        self.rounds = rounds
        
    def stun(self, attacker, defender):
        print(f"{attacker.name} uses {self.name} and stuns {defender.name}")
        defender.defense -= 5
        defender.defense = max(defender.defense, 0)
        for i in range(self.rounds):
            print(f"\nROUND {i+1}")
            if defender.is_alive():
                print(f"{defender.name} has recovered from stun and his defense not lowered anymore")
            else:
                break
        defender.defense += 5
          

class DotAttack(Attack):
    def __init__(self, name, damage):
        super().__init__(name,damage)
        
    def rend(self, attacker, defender, rounds):
        damage = self.damage + attacker.attack - defender.defense
        damage = max(damage, 0)
        total_damage = 0
        for i in range(rounds):
            defender.health -= damage
            total_damage += damage
            print(f"{attacker.name} uses {self.name} and does {damage} damage over {rounds-i} rounds")
            if not defender.is_alive():
                print(f"{defender.name} has bled out")
                break
            time.sleep(1)
        return total_damage


Hero = Character(100, 0, 0)
Hero.set_name("Hero")
Goblin = Character(80, 0, 0)
Goblin.set_name("Goblin")

attack_types = [Attack("swing", 10), Attack("punch", 7), Attack("ultimate strike", 20)]
stun_attack = Stun("STUN", 0 , 2)
dot_attack = DotAttack("BLEED", 6)


duel = Fight(Hero, Goblin, attack_types, stun_attack, dot_attack)
duel.start_fight()







"""import random
import time

class Character:
    def __init__(self, health, attack, defense, name):
        self.health = health
        self.attack = attack
        self.defense = defense
        self.name = name

    def set_name(self, name):
        self.name = name

    def is_alive(self):
        return self.health > 0
    
    

class Attack_type(Character):
    def __init__(self):    
        pass
    
    def basic_swing(self, attacker, defender,  bonus_damage):
        self.bonus_damage = bonus_damage
        swing_damage = attacker.attack + bonus_damage     
        defender.health -= swing_damage + defender.defense   
        print(f"{attacker.name} has used swing attack for {swing_damage} on {defender.name}")
        print(f"{attacker.name} have {attacker.health} health and {defender.name} have now {defender.health} health")
        
        


class Fight:
    def __init__(self, hero, enemy, attack_types, stun_attack, dot_attack):
        self.hero = hero
        self.enemy = enemy
        self.attack_types = attack_types
        self.stun_attack = stun_attack
        self.dot_attack = dot_attack
        
    def start_fight(self):
        print(f"{self.hero.name} vs {self.enemy.name}")
        loop = 1
        while self.hero.is_alive() and self.enemy.is_alive():
            print(f"\nROUND {loop}")
            self.fight(self.hero, self.enemy, self.attack_types, self.stun_attack, self.dot_attack) # Hero attacks Enemy
            if self.enemy.is_alive():
                self.fight(self.enemy, self.hero, self.attack_types, self.stun_attack, self.dot_attack) # Enemy attacks hero
                time.sleep(1)
            loop += 1

    def fight(self, attacker, defender, attack_types):
        print(f"{attacker.name} attacks {defender.name}")
        attack = random.choice(attack_types)
        damage = attack.damage + attacker.attack - defender.defense
        damage = max(damage, 0)
        defender.health -= damage
        print(f"{attack.name} does {damage} damage")
       

Hero = Character(100, 9 , 5, "Arix")        
Ghoblin = Character(50,7,3, "Ghoblin")

swing = Attack_type()

duel = Fight(Hero,Ghoblin, )"""