"""
class Student():
    def get_student_info(self):
        print(self.name,self.lastname,'поступил в', self.year_of_entrance,'на факультет:', self.department)

Вася = Student()
Вася.name = 'Вася'
Вася.lastname = 'Иванов'
Вася.year_of_entrance = '2017'
Вася.department = 'Программирование'

Student.get_student_info(Вася)
Вася.get_student_info()


class student:
    def __init__(self, name, lastname, departament, year_of_entarance):
        self.name = name
        self.lastname = lastname
        self.departament = departament
        self.year_of_entarance = year_of_entarance
    def get_student_info(self):
        print(self.name,self.lastname,"поступил в", self.year_of_entarance + "г. на факультет:", self.departament)


student1=student("Вася", "Иванов", "Программирование", "2017")
student1.get_student_info()
"""


# class ContactList:
#     def init(self,names):
#         self.names = names
#     def search_by_name(self,search):
#         for name in self.names:
#             if name == search:
#                 print(name)
# all_contacts=ContactList(['Саша','Саша','Саша','Коля','Миша','Саша','Света','Никита','Миша',
#                 'Валера','Валера','Юля','Юля','Саша','Саша','Саша','Оля','Юля','Саша','Оля','Петя',
#                 'Петя','Юля','Антон','Антон','Маша','Гоша','Оля','Юля','Гоша','Оля','Юля'])
# all_contacts.search_by_name("Антон")


# class List:

#     def __init__(self):
#         self.all_contacts = []

#     def search_by_name(self, *name):
#         for i in name:
#             self.all_contacts.append(i.title())
#         ss = [i for i in self.all_contacts if self.all_contacts.count(i) > 1]
#         sss = set(ss)
#         print("Список совпадений: ")
#         for a in sss:
#             print("\t",a)
# class ContactList(List):

#     def __init__(self):
#         super().__init__()
# my_contacts = ContactList()
# my_contacts.search_by_name("monkey","flowers","donkey","smile","donkey","monkey","books")
"""
class Airplane:
    def __init__(self, make, model, year, max_speed,odometer,is_flying):
            self.make = make
            self.model = model
            self.year = year
            self.max_speed = max_speed
            self.odometer = odometer
            self.is_flying = False

    def take_off(self):
        self.is_flying = True
        print('Самолет взлетел')
    def fly(self):
        self.odometer /= 1000
        print(self.odometer)

    def land(self):
        self.is_flying = False
        print('Самолет приземлился')

Airplane=Airplane("Boeing", "an214", "2016",'1000 km/h',100000,False)
Airplane.take_off()
Airplane.fly()
Airplane.land()
"""



# class Car:
#     def __init__(self, make, model, year, odometer,fuel,drive):
#             self.make = make
#             self.model = model
#             self.year = year
#             self.odometer = odometer
#             self.fuel = fuel
#             self.drive = drive

#     def distance(self):
#         self.drive /= 10
#         print(self.drive)
#     def add_distance(self):
#         self.odometer += self.drive
#         print(self.odometer)

#     def subtract_fuel(self):
#         if self.fuel - self.drive > 0:
#             print('lets drive')
#         else:
#             print('Need more fuel, please, fill more!')

# Car=Car("Mazda", "rx", "2016",0,70,100)
# Car.distance()
# Car.add_distance()
# Car.subtract_fuel()


"""
class Act_of_Shooting:
    def __init__(self, make, model, year, odometer,fuel,drive):
            self.make = make
            self.model = model
            self.year = year
            self.odometer = odometer
            self.fuel = fuel
            self.drive = drive

    def distance(self):
        self.drive /= 10
        print(self.drive)
    def add_distance(self):
        self.odometer += self.drive
        print(self.odometer)

    def subtract_fuel(self):
        if self.fuel - self.drive > 0:
            print('lets drive')
        else:
            print('Need more fuel, please, fill more!')

Car=Car("Mazda", "rx", "2016",0,70,100)
Car.distance()
Car.add_distance()
Car.subtract_fuel()
"""

# from random import shuffle
# import random

# class Card:
#     def __init__(self,suit,val):
#         self.suit = suit
#         self.value = val
#     def show(self):
#         print('{}  {}'.format(self.value,self.suit))

# card = Card('Card', 6)
# card.show()

# class Deck:
#     def __init__(self):
#         self.cards = []
#         self.build()
#     def build(self):
#         for s in ['Червы','Бубны','Трефы','Пики']:
#             for v in [2,3,4,5,6,7,8,9,10,'J', 'Q', 'K','A']:
#                 self.cards.append(Card(s,v))

#     def show(self):
#         for x in self.cards:
#             x.show()
#     def shuffle(self):
#         for i in range(len(self.cards)-1, 0, -1):
#             r = random.randint(0,i)
#             self.cards[i],self.cards[r] = self.cards[r], self.cards[i]

# deck = Deck()
# deck.shuffle()
# deck.show()
"""
class Soldier:
    def __init__(self,name):
        self.name = name

class Gun:
    def __init__(self):
        self.bullets = 3

    def AK47(self):
        print(f"\tSoldier {self.name.title()} scream 'A-ta-ta'")
        print(f"\t\tAK47 did: ")
        if self.bullets:
            piy = 0
            for x in range(self.bullets):
                piy += 1
                self.bullets -= 1
                print("\t\t\tti-gi-ti-gi-tish",piy)
        else:
            print(f"No bullets!")
            self.patrons()

    def patrons(self):
        print(f"\t\t\tBullets left {self.bullets} pieces")

    def reload(self):
        self.bullets += 4
        print(f"\t\t\tSoldier {self.name.title()} scream 'REALOAD!'")

class Act_of_Shooting(Soldier,Gun):
    def __init__(self,name):
        Soldier.__init__(self,name)
        Gun.__init__(self)
        print(f"\t\t\tBullets: {self.bullets} pieces")

Soldier = Act_of_Shooting('Peter')
Soldier.AK47()
Soldier.patrons()
Soldier.reload()
"""


# class house:
#     def __init__(self, type_, total_area, names_furniture):
#         self.type = type_
#         self.total_area = total_area
#         self.names_furniture = names_furniture
#         self.remaining_area = total_area
#     def cali(self):
#         for furniture in self.names_furniture:
#             if furniture == 'Bed':
#                 self.remaining_area -= 4
#             elif furniture == 'Wardrobe':
#                 self.remaining_area -= 2
#             elif furniture == 'Table':
#                 self.remaining_area -= 1.5
#         print(f'household type: {self.type} total area: {self.total_area} \nremaining area: {self.remaining_area} furniture name: {self.names_furniture}')
# house_1=house("asd", 123, ['Bed', 'Wardrobe', 'Table']).cali()


"""
class Student:
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major

    def str(self):
        print(f'<name:{self.name}, age:{self.age}, major:{self.major}>')

Steve = Student("Steven Schultz", 23, "English")
Johnny = Student("Jonathan Rosenberg", 24, "Biology")
Penny = Student("Penelope Meramveliotakis", 21, "Physics")
Student.str(Steve)

# <name: Steven Schultz, age: 23, major: English>
# print(Johnny)
# <name: Jonathan Rosenberg, age: 24, major: Biology>
"""



# import moneyfmt
"""
class Dollar:
    def __init__(self,value):
        self.value = 0

    def update(self,amount):
        self.value.update()

    def repr(self):
        self.value = float(123456.78901)
        print('$' + format((self.value), ',.2f'))

money = Dollar(123456.78901)
#Dollar.update(123456.78901)
Dollar.repr(money)
"""

# dollarize(123456.78901) # "$123,456.80"
# dollarize(-123456.7801) #-> "-$123,456.78"
# dollarize(1000000) #-> "$1,000,000

# "init" //constructor initializes the data value
# "update" //method replaces data value with new one
# "repr" //methods returns Float value
# "str" //method, that implements logic of dollarize() method

# //The output will look like this:

# cash = moneyfmt.MoneyFmt(12345678.021)
# print(cash) -- returns "$12,345,678.02"
# cash.update(100000.4567)
# print(cash) -- returns "$100,000.46"
# cash.update(-0.3)
# print(cash) -- returns "-$0.30"
# repr(cash) -- returns -0.3




# Driver program to test above functions 
#Let us create following BST 

# class Node:
#     def __init__(self,val):
#         self.value = val
#         self.leftChild = None
#         self.rightChild = None

#     def insert(self,data):
#         if self.value == data:
#             return False
#         elif self.value > data:
#             if self.leftChild:
#                 return self.leftChild.insert(data)
#             else:
#                 self.leftChild = Node(data)
#                 return True
#         else:
#             if self.rightChild:
#                 return self.rightChild.insert(data)
#             else:
#                 self.rightChild = Node(data)
#                 return True

#     def find(self,data):
#         if (self.value == data):
#             return True
#         elif self.value > data:
#             if self.leftChild:
#                 return self.leftChild.find(data)
#             else:
#                 return False
#         else:
#             if self.rightChild:
#                 return self.rightChild.find(data)
#             else:
#                 return False

    
#     def preorder(self):
#         if self:
#             print(str(self.value))
#             if self.leftChild:
#                 self.leftChild.preorder()
#             if self.rightChild:
#                 self.rightChild.preorder()

#     def postorder(self):
#         if self:
#             if self.leftChild:
#                 self.leftChild.postorder()
#             if self.rightChild:
#                 self.rightChild.postorder()
#             print(str(self.value))

#     def intorder(self):
#         if self:
#             if self.leftChild:
#                 self.leftChild.inorder()
#             print(str(self.value))
#             if self.rightChild:
#                 self.rightChild.inorder()            

# class Tree:
#     def __init__(self):
#         self.root = None

#     def insert(self,data):
#         if self.root:
#             return self.root.insert(data)
#         else:
#             self.root = Node(data)
#             return True
        
#     def find(self, data):
#         if self.root:
#             return self.root.find(data)
#         else:
#             return False
#     def preorder(self):
#         if self.root is not None:
#             print('PreOrder')
#             self.root.preorder()

#     def postorder(self):
#         if self.root is not None:
#             print('PostOrder')
#             self.root.postorder()

#     def inorder(self):
#         if self.root is not None:
#             print('InOrder')
#             self.root.inorder()

# root = Node(50)

# root = Node(30) 
# root = Node(20) 
# root = Node(40) 
# root = Node(70) 
# # root = root.Node(60) 
# # root = root.Node(80) 

# print("Sorted tree")
# Node.sorted()

# bst = Tree()
# bst.insert(50)
# bst.insert(30)
# bst.insert(20)
# bst.insert(40)
# bst.insert(60)
# bst.insert(70)
# bst.insert(80)
# print(bst.insert(80))
# bst.preorder()
# bst.postorder()
# bst.inorder()

"""
              50 
            /    \ 
          30      70 
         /  \    /  \ 
       20   40  60   80 

class Node(object):

	def insert(self, d):
		if self.data == d:
			return False
		elif d < self.data:
			if self.left:
				return self.left.insert(d)
			else:
				self.left = Node(d)
				return True
		else:
			if self.right:
				return self.right.insert(d)
			else:
				self.right = Node(d)
				return True

class Node:
      def init(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           
def lca(root, v1, v2):
    node=root
    if node is None:
        return None
    if node.info>v1 and node.info>v2:
        return lca(node.left,v1,v2)
    elif node.info<v1 and node.info < v2:
        return lca(node.right,v1,v2)
    else:
        return node

root = Node(50)
root = root.addNode(30) 
root = root.addNode(20) 
root = root.addNode(40) 
root = root.addNode(70) 
root = root.addNode(60) 
root = root.addNode(80) 

print "Sorted tree"
root.sorted()
"""

    # Create class User with proper methods:
    #     get_account_balance(),  change_password()
    #     Create decorator to handle errors, listed below

# class User: 
#     def __init__(self,name): 
#         self.name = name
#         self.balance=0
#         print("Hello Noka!!! Welcome to the Deposit & Withdrawal Machine") 
  
#     def deposit(self): 
#         amount=float(input("Enter amount to be Deposited: ")) 
#         self.balance += amount 
#         print("Amount Deposited:",amount) 
  
#     def withdraw(self): 
#         amount = float(input("Enter amount to be Withdrawn: ")) 
#         if self.balance>=amount: 
#             self.balance-=amount 
#             print("You Withdrew:", amount) 
#         else: 
#             print("Insufficient balance  ") 
  
#     def get_account_balance(self): 
#         print("Your Available Balance=",self.balance) 
    
#     def change_password(self):
#         self.password = []
#         self.password = float(input("Enter new password: "))
#         print("\n Your password been changed ") 
 
# s = User('Noka')   
# s.deposit() 
# s.withdraw() 
# s.get_account_balance()
# s.change_password()

"""import random
 
class unit:
    def init(self, id, team):
        self.id = id
        self.team = team
 
class soldier(unit):
    def follow(self, hero):
        print "Soldier with ID {} is following Hero with ID {}".format(self.id, hero.id)
 
class hero(unit):
    def init(self, id, team):
        unit.init(self, id, team)
        self.level = 0
 
    def levelup(self, team_size):
        self.level = team_size / 10
 
teams = ['good_team', 'bad_team']
gandalf = hero(1, teams[0])
sauron = hero(2, teams[1])
 
soldiers = []
good_team = [gandalf]
bad_team = [sauron]
 
for i in range(1,1000):
    soldiers.append(soldier(i, random.choice(teams)))
 
for warrior in soldiers:
    if warrior.team == 'good_team':
        good_team.append(warrior)
    else:
        bad_team.append(warrior)
 
print "Good team size: {}, Bad team size: {}".format(len(good_team), len(bad_team))
 
gandalf.levelup(len(good_team))
sauron.levelup(len(bad_team))
 
print "Gandalf lvl {}, Sauron lvl {}".format(gandalf.level, sauron.level)
 
random.choice(good_team).follow(gandalf)
"""
# import math

# class Complex(object):
#     def __init__(self, real, imaginary):
        
#     def __add__(self, no):
        
#     def __sub__(self, no):
        
#     def __mul__(self, no):

#     def __truediv__(self, no):

#     def mod(self):

#     def __str__(self):
#         if self.imaginary == 0:
#             result = "%.2f+0.00i" % (self.real)
#         elif self.real == 0:
#             if self.imaginary >= 0:
#                 result = "0.00+%.2fi" % (self.imaginary)
#             else:
#                 result = "0.00-%.2fi" % (abs(self.imaginary))
#         elif self.imaginary > 0:
#             result = "%.2f+%.2fi" % (self.real, self.imaginary)
#         else:
#             result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
#         return result

# if __name__ == '__main__':


# parts = list(map(float, input().split()))
# a = complex(parts[0], parts[1])
# parts = list(map(float, input().split()))
# b = complex(parts[0], parts[1])
# def p(comp):
#     if comp.real != 0 and comp.imag != 0:
#         print('%.2f %s %.2fi' % (comp.real, '+' if comp.imag >= 0 else '-', abs(comp.imag)))  
#     elif comp.imag == 0:
#         print("%.2f" % comp.real)
#     elif comp.real == 0:
#         print("%.2fi" % comp.imag)
    
# p(a+b)
# p(a-b)
# p(a*b)
# p(a/b)
# print("%.2f" % abs(a))

