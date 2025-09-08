import random
from enemy import Enemy

class Allen_Mcdade(Enemy):
    #override health + attack power
    def __init__(self, name):
        super().__init__(name)
        self.health = 200
        self.attack_power = random.randint(10, 20)


    def mongolian_Throat_Singing(self):
        print("Allen Mcdade used their Special attack, Mongolian Throat Singing!")
        print("oiiiiiiii oiiiiiiiiiii ooooooooooo oiiiiiiiiiiii")


    def attack(self):
        self.mongolian_Throat_Singing()
        return self.attack_power
