import random
class Character:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    def attack(self, other):
        dmg = round(self.attack_power + (self.attack_power * (random.randint(30, 91) / 100)), 2)
        other.hp -= dmg
        print(f"{self.name} attacks {other.name} for {dmg} damage!")

    def is_alive(self):
        return self.hp > 0

    def __str__(self):
        return f"{self.name}: {self.hp:.2f} HP"