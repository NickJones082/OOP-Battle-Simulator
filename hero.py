import random

class Hero:
    """
    This is our hero blueprint.
    
    O=('-'Q)

    Attributes:
        name: The name of our adventurer.
        hp: The current health value.
        strength: The amount of damage the hero can deal.
        (Bonus) defence: A hero's ability to reduce incoming damage.
        (Bonus) special_ability: A unique ability the hero can use.
    """
    
    def __init__(self, name):
        #TODO Set the hero's name.
        self.name = name
        #TODO Set the hero's health. You might give the hero more health than a goblin.
        self.health = 150
        #TODO Set the hero's attack power. Should it be more consistent than the goblin's?
        self.attack_power = random.randint(7, 10)




    

    def strike(self):
        # TODO Implement the hero's attack logic. It could be stronger or more consistent than a goblin's.
        damage = random.randint (5, self.attack_power)
        damage = damage + random.randint(1, 10)
        bonus_chance = random.randint(0, 5)
        self.special_ability = random.randint(100, 200)
        bonus_damage = damage + self.special_ability
        if bonus_chance > 4:
            print(f"{self.name} used their special ability!")
            return bonus_damage
        return damage

    
    
    def receive_damage(self, damage):
        # TODO Implement take_damage
        self.health -= damage
        # TODO We should prevent health from going into the NEGATIVE
        if self.health < 0:
            self.health = 0
        print(f"{self.name} takes {damage} damage. Health is now {self.health}.")
   
    def is_alive(self):
        return self.health != 0

