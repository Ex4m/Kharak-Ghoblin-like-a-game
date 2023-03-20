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
    def __init__(self, hero, enemy, attack_types):
        self.hero = hero
        self.enemy = enemy
        self.attack_types = attack_types
        
        
    def start_fight(self):
        print(f"{self.hero.name} vs {self.enemy.name}")
        loop = 1
        print("------------------------------------------------------------")
        while self.hero.is_alive() and self.enemy.is_alive():
            print(f"\nROUND {loop}")
            self.fight(self.hero, self.enemy, self.attack_types) # Hero attacks Enemy
            if self.enemy.is_alive():
                self.fight(self.enemy, self.hero, self.attack_types) # Enemy attacks hero
                time.sleep(1)
            loop += 1
        print("------------------------------------------------------------")
        
    def fight(self, attacker, defender, attack_types):
        print(f"{attacker.name} attacks {defender.name}")
        attack = random.choice(attack_types)
        damage = attack.damage + attacker.attack - defender.defense
        damage = max(damage, 0)
        defender.health -= damage
        print(f"{attack.name} does {damage} damage")
        print(f"{defender.name} has {defender.defense} defense so the actual damage is {attack.damage + attacker.attack}-{defender.defense} = {damage}. Health of {defender.name} is now {defender.health}")
        try:
            if defender.is_bleeding:
                print(f"{defender.name} is bleeding !!!")
                rend = [attack for attack in attack_types if isinstance(attack, DotAttack) and attack.name == "rend"][0]
                rend.bleed(defender)
        except:
            pass
        if not defender.is_alive():
            print(f"{defender.name} has been defeated!")
        
        if isinstance(attack, Stun):
            attack.stun(attacker, defender)
        elif isinstance(attack, DotAttack):
            damage, bleed_damage, bleed_rounds, is_bleeding = attack.rend(attacker, defender)
            defender.bleed_rounds = bleed_rounds
            defender.is_bleeding = is_bleeding
        

          

class DotAttack(Attack):
    def __init__(self, name, damage, bleed_rounds, bleed_damage):
        super().__init__(name, damage)
        self.bleed_rounds = bleed_rounds
        self.bleed_damage = bleed_damage

    def rend(self, attacker, defender):
        damage = self.damage - defender.defense
        damage = max(damage, 0)
        bleed_damage = round(self.damage * 0.5, None)
        defender.health -= damage
        print(f"{attacker.name} has applied BLEED to {defender.name} for {self.bleed_rounds} rounds")
        defender.bleed_rounds = self.bleed_rounds     #Here I apply bleed rounds to object of defender
        defender.is_bleeding = True
        return damage, bleed_damage , defender.bleed_rounds, defender.is_bleeding

    def bleed(self, defender):
        if defender.bleed_rounds > 0:
            bleeding = round(self.bleed_damage * 0.4, None)
            defender.health -= bleeding
            defender.bleed_rounds -= 1
            print(f"{defender.name} has bled for {bleeding}, so it has now {defender.health} health. It will bleed for the next {defender.bleed_rounds} rounds.")
        else:
            defender.is_bleeding = False
        return self.bleed_damage, defender.bleed_rounds, defender.is_bleeding

    def is_bleeding(self):
        return self.bleed_rounds > 0


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
            
        


def roll_dice(from_side, to_side):
    return random.randint(from_side, to_side)



Hero = Character(100, 10, 5)
Hero.set_name("The Gargix (Hero)")
Goblin = Character(80, 8, 4)
Goblin.set_name("Awaken Goblin")

attack_types = [
    Attack("swing", roll_dice(2,5)),
    Attack("punch", roll_dice(1,8)),
    Attack("ultimate strike", roll_dice(6,12)),
    DotAttack("rend", roll_dice(2,6), 3, roll_dice(4,6)),
    Stun("stun", roll_dice(1,2), 2)
]

duel = Fight(Hero, Goblin, attack_types)
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