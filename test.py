class Character:
    def __init__(self, health, base_damage, defense):
        self.health = health
        self.base_damage = base_damage
        self.defense = defense
        
    def set_name(self):
        self.name = input("What name this character should be called? ")
        
    
    def get_name(self):
        if self.name:
            return self.name
        else:
            self.set_name()
            return self.name



class Fight:
    def __init__(self, hero, enemy):
        self.hero = hero
        self.enemy = enemy
        
    def start(self):
        self.hero.health -= self.enemy.base_damage
        self.enemy.health -= self.hero.base_damage    
        print(f"{self.hero.name} has now {self.hero.health} and {self.enemy.name} has now {self.enemy.health}")
        
        
Hero = Character(100,20,10)
Goblin = Character(80,25,7)
Hero.set_name()
Goblin.set_name()

duel = Fight(Hero, Goblin)
duel.start()