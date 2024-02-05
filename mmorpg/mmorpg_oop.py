class Warrior:
    def __init__(self, health=100, stamina=100):
        self.__health = health
        self.__stamina = stamina
    
    def introduce(self):
        print('---------------')
        print(f'Class: {self.__class__.__name__} \nHealth: {self.__health} \nStamina: {self.__stamina}')
        print('---------------')
    
    def get_health(self):
        return self.__health
    
    def set_health(self, points):
        self.__health += points
        if self.__health >= 100:
            self.__health = 100
        elif self.__health < 0:
            self.__health = 0
    
    def heal(self, target):
        if self.__stamina >=20:
            target.set_health(10) 
            self.__stamina -= 20
            print('---------------')
            print(f'The {self.__class__.__name__} applies a bandage of healing herbs to the {target.__class__.__name__}\n{target.__class__.__name__} Health has been increased to {target.get_health()} \n{self.__class__.__name__} has {self.__stamina} stamina left') 
            print('---------------')
        else: print("Not enough stamina for this spell.\n")
    
    def attack(self, target):
        if target.get_health() > 3:
            target.set_health(-3)
            print('---------------')
            print(f'The {self.__class__.__name__} inflicts damage with the sword to the {target.__class__.__name__}\n{target.__class__.__name__} health reduced to {target.get_health()}') 
            print('---------------')
        else:
            target.set_health(-3)
            print('---------------')
            print(f'The {self.__class__.__name__} deals fatal blow and kills {target.__class__.__name__}\n{target.__class__.__name__} goes to Valhalla') 
            print('---------------')

class Mage:
    def __init__(self, health=60, mana=110):
        self.__health = health
        self.__mana = mana
    
    def introduce(self):
        print('---------------')
        print(f'Class: {self.__class__.__name__} \nHealth: {self.__health} \nMana: {self.__mana}')
        print('---------------')
    
    def get_health(self):
        return self.__health
    
    def set_health(self, points):
        self.__health += points
        if self.__health >= 100:
            self.__health = 100
        elif self.__health < 0:
            self.__health = 0
    
    def heal(self, target):
        if self.__mana >=20:
            target.set_health(10)
            self.__mana -= 20
            print('---------------')
            print(f'{self.__class__.__name__} uses a healing spell on {target.__class__.__name__}\n{target.__class__.__name__} Health has been increased to {target.get_health()} \n{self.__class__.__name__} has {self.__mana} mana left') 
            print('---------------')
        else: print("Not enough mana for this spell.\n")
    
    def attack(self, target):
        if target.get_health() > 3: 
            target.set_health(-3)
            print('---------------')
            print(f'The {self.__class__.__name__} deals magic damage to {target.__class__.__name__}\n{target.__class__.__name__} health reduced to {target.get_health()}') 
            print('---------------')
        else:
            target.set_health(-3)
            print('---------------')
            print(f'The {self.__class__.__name__} deals fatal magic blow and kills {target.__class__.__name__}\n{target.__class__.__name__} goes to Valhalla') 
            print('---------------')



