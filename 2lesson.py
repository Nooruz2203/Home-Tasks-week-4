# class Person():
#     def speak(self):
#         print('Я говорю')
# p1 = Person()
# p1.speak()
# p2 = Person()
# p2.speak()


# car = {'make':'Honda',
#        'model': 'Accord',
#        'odometer': 0,
#        'year': 2008
# }

"""
def go_car(car,km):
    odometer = car.get('odometer')
    car['odometer']=odometer + km
    return car
old_car = go_car(car, 120)
print(old_car)

old_car = go_car(car,15)
print(old_car)
"""
# class Car:
#     def __init__(self,auto_owner,auto_make,auto_model,prod_year):
#         self.owner = auto_owner
#         self.make = auto_make
#         self.model = auto_model
#         self.year = prod_year
#         self.odometer = 0
#     def go(self,km):
#         self.odometer = self.odometer + km
#         print('WHoooooo!!!!!!!!!!!')

# new_car = Car('John','Toyota','camry',2020)
# print(new_car.odometer)
# new_car.go(368)
# print('Johns Car odometer', new_car.odometer)

# new_car = Car('Rachel','Mers','sclass',2020)
# print('Rachels Car odometer',new_car.odometer)


# class Laptop():
#     def __init__(self, name):
#         self.name = name
#     def turn_on(self):
#         print(f'notebook {self.name} is on')
#         print(self.name)

# apple_mac = Laptop('Macbook Pro')
# apple_mac.turn_on()

# acer = Laptop('Acer Pro')
# acer.turn_on()

# Lenovo = Laptop('Lenovo')
# Lenovo.turn_on()
"""
class Hello():
    def __init__(self, name):
        self.name = name
        self.say_hello()
    def say_hello(self):
        print(f'Hi {self.name}')


# names = ['John','Rachel','Peter']
# for object_ in names:
#     Hello(object_)
text = ""
while True:
    text = input('input name:')
    if text == 'q':
        break
    Hello(text)
"""   

#module random

import random 

# random.randrange(1,10)
# print(random.randrange(1,10))
# print(random.randrange(100))
# print('число со степом 2',random.randrange(1,50,2))


#random.randint(a,b)

#print(random.randint(5,15))

# print(random.choice('this is a letter'))
# print(random.choice([x for x in range(1,50)]))
"""
dict_ = {'name':'john','name2':'rachel'}
key = (random.choice(tuple(dict_.keys())))
print(dict_.get(key))
"""

#random.shuffle(iterable object)
"""
numbers = [1,2,3,4,5,6,7,34,65,54]

random.shuffle(numbers)
print(numbers)
"""

# advertisements = ['1 реклама', ' 1xbet','777','Oshka','Beeline']
# random.shuffle(advertisements)
# print(advertisements[0])
"""
x = [x for x in "это тестовый пример"]
random.shuffle(x)
print(x)
"""

# print(random.sample([2,4,3,7,1,9,6,66],5))
# print(random.sample('this is sample test',3))

# print(random.random())
# print(random.random())


class Student():
    def __init__(self, name, lastname, university):
        self.name = name
        self.lastname = lastname
        self.university = university
        self.books = []
        self.knowledge = 0
        self.is_readytowork = False

    def read_book(self,bookname):
        self.books.append(bookname)
        self.__add_points(400)

    def do_homework(self):
        self.__add_points(10) 

    def do_real_project(self,project_name):
        print(f'You {self.name} did - {project_name} this project')
        self.__add_points(50)
    
    def __add_points(self,point):
        self.knowledge +=point
        if self.knowledge >= 1000:
            print(f'{self.name} student is really working')
            self.is_readytowork = True
            if self.is_readytowork:
                print(f'{self.name} She is working')
        

st1 = Student(
    'John', 'Snow','Garvard'
)
st2 = Student(
    'Rachel','Smith', 'Oxford'
)
st3 = Student(
    'Sonya', 'Blake', 'Stanford'
)

st1.read_book('Game of Thrones')
st1.do_homework()
st2.read_book('Jane Ostin')
st2.read_book('Aitmatov')
st2.read_book('Harry poter')
st2.do_homework
st3.do_homework()
print(f'{st1.name}-{st1.knowledge}-{st1.books}')
print()
print(f'{st2.name}-{st2.knowledge}-{st2.books}')
print()
print(f'{st3.name}-{st3.knowledge}-{st3.books}')
print()

#print(st1.__add_points(100)) #защита 