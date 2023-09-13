class Person:
    "Any help info about class Human"
    def __init__(self, name, weapon, power, magic, life, lvl, profession):
        self.name = name
        self.health = 100
        self.power = power
        self.weapon = weapon
        self.magic = magic
        self.life = life
        self.lvl = lvl
        self.profession = profession

    @property
    def inf(self):
        return self.name, self.health, self.power, self.weapon, self.magic, self.life, self.lvl, self.profession

    @inf.setter
    def inf(self, name, power, weapon):
        return f'{name, power, weapon}'

    def attack(self):
        return f'attack with power {self.power} with lvl {self.lvl}'

class Character(Person):
    def __init__(self, name, weapon, power, magic, life, lvl, profession, hit):
        super().__init__(name, weapon, power, magic, life, lvl, profession)
        self.hit = hit

    def attack2(self):
        super().attack()
        return f'attack with power {self.power} with lvl {self.lvl} with hit {self.hit}'

ninja = Character('Evangelyne', 100, 'might', False, True, 1, 'cooking', 20)
print(ninja.name



      )
