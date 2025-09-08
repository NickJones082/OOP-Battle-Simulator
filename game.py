import random
from goblin import Goblin
from hero import Hero
from boss import Allen_Mcdade

def main():
    print("Welcome to the Battle Arena!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")

    # Create a hero
    hero = Hero("Sol")

    # Create goblins ༼ ºل͟º ༽ ༼ ºل͟º ༽ ༼ ºل͟º ༽
    goblins = [Goblin(f"Goblin {i+1}", "green") for i in range(3)]

    # Keep track of how many goblins were defeated
    defeated_goblins = 0
    #Track number of rounds that have been completed
    total_rounds = 0
    


    # Battle Loop 
    while hero.is_alive() and any(goblin.is_alive() for goblin in goblins):
        print("\nNew Round!")
        
        # Hero's turn to attack
        target_goblin = random.choice([goblin for goblin in goblins if goblin.is_alive()])
        damage = hero.strike()
        print(f"Hero attacks {target_goblin.name} for {damage} damage!")
        target_goblin.take_damage(damage)

        # Check if the target goblin was defeated
        if not target_goblin.is_alive():
            defeated_goblins += 1
            print(f"{target_goblin.name} has been defeated!")

        # Goblins' turn to attack
        for goblin in goblins:
            if goblin.is_alive():
                damage = goblin.attack()
                print(f"{goblin.name} attacks hero for {damage} damage!")
                hero.receive_damage(damage)
        
        total_rounds = total_rounds + 1

    # Determine outcome
    if hero.is_alive():
        print(f"\nThe hero has defeated all the goblins! ༼ ᕤ◕◡◕ ༽ᕤ")
    else:
        print(f"\nThe hero has been defeated. Game Over. (｡•́︿•̀｡)")


    if hero.is_alive():
        Allen = Allen_Mcdade("Allen Mcdade")
        print("-------------------------------------------------")
        print("Boss Round!")
        hero.health = 150
        print("Health Restored! Take down the Boss!")
        print("-------------------------------------------------")
        while hero.is_alive() and Allen.is_alive():
            damage = hero.strike()
            Allen.take_damage(damage)
            print(str(hero.name) + " strikes the boss for " + str(damage))
            print(str(Allen.name) + " takes " + str(damage))

            damage = Allen.attack()
            hero.receive_damage(damage)
            print(str(Allen.name) + " strikes " + str(hero.name) + " for " + str(damage) + " damage")
            print(str(hero.name) + " takes " + str(damage) + " damage")
            print("-------------------------------------------------")

        
        if hero.is_alive():
            print(f"\nThe hero has defeated the boss! ༼ ᕤ◕◡◕ ༽ᕤ")
        else:
            print(f"\nThe hero has been defeated. Game Over. (｡•́︿•̀｡)")



    # Final tally of goblins defeated
    print(f"\nTotal goblins defeated: {defeated_goblins} / {len(goblins)}")
    
    # Total Rounds played
    print("Total rounds played/survived: " + str(total_rounds))

    #Print if boss was defeated
    if not(Allen.is_alive()):
        print("Boss was defeated!")
    else:
        print("Boss was not defeated!")

if __name__ == "__main__":
    main()
