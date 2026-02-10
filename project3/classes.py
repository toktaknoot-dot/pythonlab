#สร้างคลาส Character และ Enemy ในไฟล์ `classes.py` ดังนี้:
#```python
class Character:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self, enemy):
        enemy.hp -= self.damage
        print(f"{self.name} attacked {enemy.name} for {self.damage} damage!")
        if enemy.hp <= 0:
            print(f"{enemy.name} has been defeated!")

class Enemy(Character):
    def __init__(self, name, hp, damage):
        super().__init__(name, hp, damage)
