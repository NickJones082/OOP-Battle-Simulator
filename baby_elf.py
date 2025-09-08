from enemy import Enemy
class Baby_Elf(Enemy):
    def cry():
        print("AAAAAAAAAAAA AAAAAAAAAAAAAA")
    
    #Override take damage
    def take_damage(self, damage):
        print("You hit a BABY? Cool")
        return super().take_damage(damage)