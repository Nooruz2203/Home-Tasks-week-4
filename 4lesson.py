"""
class Test():
    hello = 'hello world'
    def __init__(self,name):
        self.name = name
        self.test_var= 'Some Data'

t1 = Test(
    'Some Name'
)

print(t1.name)
print(t1.test_var)
print(Test.hello)
print(t1.hello)
"""

# class AvtoZavodBMW():
#     count_car = 0
#     def __init__(self,name,mark,model,year):
#         self.name = name
#         self.mark = mark
#         self.model = model
#         self.year = year
#         AvtoZavodBMW.count_car +=1
#         #print(f'Создалась{self.name}----{self.count_car}'

# bmw = AvtoZavodBMW(
#     'BMW', 'BMW', '720', 2005
# )
# bmw = AvtoZavodBMW(
#     'bmww', 'BMw', '700', 2006
# )
# bmw = AvtoZavodBMW('bmd','sd','sd',2008)
# print(bmw.count_car)

"""
class Robot:
    population = 0
    def __init__(self,name):
        self.name = name
        print(f'Inicialisation {self.name}')

        Robot.population +=1
    def __del__(self):
        print(f'{self.name} is being destroyed!')
        Robot.population -= 1
        if Robot.population == 0:
            print(f'{self.name} was last one')
        else:
            print(f'{Robot.population} amount of working robot')

    def sayHi(self):
        print(f'Hi I am robot, my name is {self.name}')
    
    def howmany():
        print(f'For this moment we have {Robot.population} robots')

    Howmany = staticmethod(howmany)

Optimus = Robot(
    'Optimus Prime'
)
Optimus.sayHi()
Robot.howmany()
"""

# class User:
#     def __init__(self,name,email):
#         self.name = name
#         self.email = email

#     def get_email_data(self):
#         return{
#             'name': self.name,
#             'email': self.email
#         }
# john = User('John Conor','johnconor@example.com')
# print(john.get_email_data())

"""
class Singleton:
    instance = None
    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

a =Singleton()
b = Singleton()
print(a is b)
print(id(a))
print(id(b))
"""



