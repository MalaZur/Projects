class Email:
    def __init__(self, login='', email=''):
        self.login = login
        self.__email = email
    
    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, n_em):
        if n_em.count('@') == 1 and n_em.find('@') < n_em.find('.'):
            self.__email = n_em
        else:
            print('Email is not right')
    


#k = Email("abobich", "artur4lazarev@gmail.com")
#print(k.email)
#k.email = "artur5lazarev@gmail.com"
#print(k.email)


class Robot:
    def __init__(self, name='', year=1900, psyh = 0.0, phys = 0.0):
        self.name = name
        self.year = year
        self.__psyh = psyh
        self.__phys = phys
    
    @property
    def condition(self):
        if self.__psyh + self.__phys <= -1:
            return "Я чувствую себя несчастным"
        elif self.__psyh + self.__phys > -1 and self.__psyh + self.__phys <= 0:
            return "Я чувствую себя плохо"
        elif self.__psyh + self.__phys == 1.9949999999999999:
            return "Чувствую себя на 18, хоть и преподаю программирование"
        elif self.__psyh + self.__phys > 0 and self.__psyh + self.__phys <= 0.5:
           return "Могло быть хуже" 
        elif self.__psyh + self.__phys >= 0.5 and self.__psyh + self.__phys <= 1:
           return "Кажется всё в порядке" 
        else:
            return "Всё супер!"
       
#k1 = Robot("Marry", 1969, 0.5, -0.4)
#print(k1.condition)
#k2 = Robot("Vlad", 1995, 1.9, 0.095)
#print(k2.condition)


class Money:
    def __init__(self, dollar=0, cents=0):
        self._dollar = dollar
        self._cents = cents
        self._total_cents = cents + dollar*100

    @property
    def dollars(self):
        return self._dollar
    
    @dollars.setter
    def dollars(self, n_d):
        if isinstance(n_d, int) and n_d>0:
            self._total_cents = n_d*100 + self._cents
            self._dollar = n_d
        else:
            print("Error dollars")

    @property
    def cents(self):
        return self._cents
    
    @cents.setter
    def cents(self, n_c):
        if isinstance(n_c, int) and n_c>0 and n_c < 100:
            self._total_cents = n_c*100 + self._cents
            self._cents = n_c
        else:
            print("Error cents")

    def __str__(self) -> str:
        str = f"Ваше состояние составляет {self._dollar} долларов и {self._cents} центов"
        return str

d1 = Money(20, 40)
print(d1.dollars)
d1.dollars = -10
d1.dollars = 15
d1.cents = 12.2
d1.cents = -1
d1.cents = 25
print(d1.cents)
print(d1.dollars)
print(d1)