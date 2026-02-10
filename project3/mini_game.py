# สร้างเกมจากคลาสที่เราสร้างขึ้นมาในไฟล์ `classes.py` โดยเราจะสร้างเกมที่มีตัวละครหลักและศัตรูที่ต้องต่อสู้กัน ในไฟล์ `mini_game.py` ดังนี้:
# pythonfrom classes import Character, Enemy
import random 
import time
from classes import Character, Enemy
def main():
    # สร้างตัวละครหลัก
    hero = Character("Hero", 100, 20)
    
    # สร้างศัตรู
    enemies = [
        Enemy("Goblin", 50, 10),
        Enemy("Orc", 80, 15),
        Enemy("Dragon", 150, 25)
    ]
    
    print("Welcome to the Mini Game!")
    time.sleep(1)
    
    for enemy in enemies:
        print(f"\nA wild {enemy.name} appears!")
        time.sleep(1)
        
        while enemy.hp > 0 and hero.hp > 0:
            hero.attack(enemy)
            time.sleep(1)
            if enemy.hp > 0:
                enemy.attack(hero)
                time.sleep(1)
                if hero.hp <= 0:
                    print("You have been defeated! Game Over.")
                    return
        
        print(f"You have defeated the {enemy.name}!")
        time.sleep(1)
    
    print("Congratulations! You have defeated all enemies!")
    
if __name__ == "__main__":
    main()