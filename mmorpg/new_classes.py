from mmorpg_oop import Warrior, Mage
from random import *

class Knight(Warrior):
    def __init__(self, health=100, armor=100, stamina=100):
        super().__init__(health, stamina)
        self.__armor = armor

    def set_health(self, points):
        if self.__armor > 0 and points < 0:
            self.__armor += points
            if self.__armor < 0:
                overdamage = self.__armor
                self.__armor = 0
                return super().set_health(overdamage)
        else:
            return super().set_health(points)
        
    def __critical_hit(self, target):
        if target.__armor <= 10 and target.__armor != 0:
            target.set_health(-10)
            print('---------------')
            print(f'The {self.__class__.__name__} inflicts critical damage with the sword to the {target.__class__.__name__}\n{target.__class__.__name__} armor has been destroyed\n{target.__class__.__name__} health reduced to {target.get_health()}') 
            print('---------------')
        elif target.__armor == 0 and target.get_health() > 10:
            target.set_health(-10)
            print('---------------')
            print(f'The {self.__class__.__name__} inflicts critical damage with the sword to the {target.__class__.__name__}\n{target.__class__.__name__} armor reduced to {target.__armor}\n{target.__class__.__name__} health reduced to {target.get_health()}') 
            print('---------------')
        elif target.get_health() > 10:
            target.set_health(-10)
            print('---------------')
            print(f'The {self.__class__.__name__} inflicts critical damage with the sword to the {target.__class__.__name__}\n{target.__class__.__name__} armor reduced to {target.__armor}\n{target.__class__.__name__} health reduced to {target.get_health()}') 
            print('---------------')
        else:
            target.set_health(-10)
            print('---------------')
            print(f'The {self.__class__.__name__} deals critical fatal blow and kills {target.__class__.__name__}\n{target.__class__.__name__} goes to Valhalla') 
            print('---------------')


    def attack(self, target):
        chance = randint(1,10)
        if chance<=4: 
            self.__critical_hit(target)
        else:
            if target.__armor <= 3 and target.__armor != 0:
                target.set_health(-3)
                print('---------------')
                print(f'The {self.__class__.__name__} inflicts damage with the sword to the {target.__class__.__name__}\n{target.__class__.__name__} armor has been destroyed\n{target.__class__.__name__} health reduced to {target.get_health()}') 
                print('---------------')
            elif target.__armor == 0 and target.get_health() > 3:
                target.set_health(-3)
                print('---------------')
                print(f'The {self.__class__.__name__} inflicts damage with the sword to the {target.__class__.__name__}\n{target.__class__.__name__} armor reduced to {target.__armor}\n{target.__class__.__name__} health reduced to {target.get_health()}') 
                print('---------------')
            elif target.get_health() > 3:
                target.set_health(-3)
                print('---------------')
                print(f'The {self.__class__.__name__} inflicts damage with the sword to the {target.__class__.__name__}\n{target.__class__.__name__} armor reduced to {target.__armor}\n{target.__class__.__name__} health reduced to {target.get_health()}') 
                print('---------------')
            else:
                target.set_health(-3)
                print('---------------')
                print(f'The {self.__class__.__name__} deals fatal blow and kills {target.__class__.__name__}\n{target.__class__.__name__} goes to Valhalla') 
                print('---------------')



            

un1 = Knight()
un2 = Knight(60,7,50)
un1.attack(un2)
un1.attack(un2)
un1.attack(un2)
un1.attack(un2)
un1.attack(un2)

