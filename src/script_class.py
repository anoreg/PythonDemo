#---------------------------------------------class
class Facade:
  pass


facade_1 = Facade()
facade_1_type = type(facade_1)
print(facade_1_type)


# instance variables
# Instance variables and class variables are both accessed similarly in Python. This is no mistake, they are both considered attributes of an object. If we attempt to access an attribute that is neither a class variable nor an instance variable of the object Python will throw an AttributeError.
print("---------------------- instance variable start")
class Store:
  pass


alternative_rocks = Store()
isabelles_ices = Store()
store_attr = Store()

alternative_rocks.store_name = "Alternative Rocks"
isabelles_ices.store_name = "Isabelle's Ices"
store_attr.attr = "hello"
print(alternative_rocks.store_name, store_attr.attr)
# print(alternative_rocks.attr, store_attr.store_name)

# getattr(), hasattr()
# hasattr(class instance, "attribute name"), return True or False
# getattr(class instance, "attribute", default value) return attribute value or default's
# returns 800, the default value
how_many_s = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]
for element in how_many_s:
  if hasattr(element, "count"):
    print(element, element.count("s"))
    
print("--------------------------instance variable end")


print("--------------------------keyword start")
# self, this is default first argrument in method parameters
class Dog():
  dog_time_dilation = 7

  def time_explanation(self):
    print("Dogs experience {} years for every 1 human year.".format(self.dog_time_dilation))


pipi_pitbull = Dog()
pipi_pitbull.time_explanation()


# It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:
class Person:

  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)


p1 = Person("John", 36)
p1.myfunc()


# dir, list all class's attributes
# class
class FakeDict:
  pass


fake_dict = FakeDict()
fake_dict.attribute = "Cool"

print("class attrs: ", dir(fake_dict), "\n")
# list
fun_list = [10, "string", {'abc': True}]
print("list type: ", type(fun_list))
print("list attrs: ", dir(fun_list), "\n")
# int
print("int attrs: ", dir(5), "\n")


# function, function is also an object, like type()
def this_function_is_an_object(param):
  return "wtf"


print("function attrs: ", dir(this_function_is_an_object), "\n")
# native functions, like type(), dir(), etc.
print("type attrs: ", dir(type), "\n")

print("-----------------------------keyword end")

print("---------------------------------built-in methods start")
# class's constructor and string representation
class Circle:
  pi = 3.14

  # __init__, like java's constructor, but can't define multiple constructors. However, you can define a default value if one is not passed.
  def __init__(self, diameter=0, size=None):
    print("Creating circle with diameter {d}".format(d=diameter))
    self.radius = diameter / 2
    self.size = size
    
  def circumference(self):
    return 2 * self.pi * self.radius

  # __repr__, like java's toString()
  def __repr__(self):
    print("size:", self.size)
    return "Circle with radius {radius}, size {size} \n".format(radius=self.radius, size=self.size if self.size else "Not assigned")

  
medium_pizza = Circle(12, "medium")
teaching_table = Circle(36)
dynamic_table = Circle()

print(medium_pizza.circumference(), teaching_table.circumference())
print(medium_pizza, teaching_table  , dynamic_table)

# 类的专有方法：
# __init__ : 构造函数，在生成对象时调用
# __del__ : 析构函数，释放对象时使用
# __repr__ : 打印，转换
# __setitem__ : 按照索引赋值
# __getitem__: 按照索引获取值
# __len__: 获得长度
# __cmp__: 比较运算
# __call__: 函数调用
# __add__: 加运算
# __sub__: 减运算
# __mul__: 乘运算
# __truediv__: 除运算
# __mod__: 求余运算
# __pow__: 乘方

print("---------------------------------built-in methods end")


print("---------------------------------inheritance and  polymorphism start")
# exception hierarchy, https://docs.python.org/3/library/exceptions.html#exception-hierarchy
#   
# subclass, super, overide sample
class PotatoSalad:

    def __init__(self, potatoes, celery, onions):
        self.potatoes = potatoes
        self.celery = celery
        self.onions = onions

    
class SpecialPotatoSalad(PotatoSalad):

    def __init__(self, potatoes, celery, onions):
        super().__init__(potatoes, celery, onions)
        self.raisins = 40


# whether is subclass
print(issubclass(SpecialPotatoSalad, PotatoSalad))

class Parent:        # 定义父类
    def myMethod(self):
        print ('调用父类方法')
 
class Child(Parent): # 定义子类
    def myMethod(self):
        print ('调用子类方法')
 
c = Child()          # 子类实例
c.myMethod()         # 子类调用重写方法
super(Child,c).myMethod() #用子类对象调用父类已被覆盖的方法

# customer exception
class MyException(Exception):
    
    def __init__(self, value):
            self.value = value

    def __str__(self, *args, **kwargs):
        return repr(self.value)

# interface
class Chess:

  def __init__(self):
    pass

  def play(self):
    print("Playing chess!")


class Checkers:

  def __init__(self):
    pass

  def play(self):
    print("Playing checkers!")


def play_game(chess_or_checkers):
  chess_or_checkers.play()

  
chess_game = Chess()
checkers_game = Checkers()
chess_game_2 = Chess()

for game in [chess_game, checkers_game, chess_game_2]:
  play_game(game)


# interface demo
class InsurancePolicy:

  def __init__(self, price_of_item):
    self.price_of_insured_item = price_of_item
    
  def get_rate(self):
    pass

    
class VehicleInsurance(InsurancePolicy):

  def get_rate(self):
    return 0.001 * self.price_of_insured_item


class HomeInsurance(InsurancePolicy):

  def get_rate(self):
    return 0.00005 * self.price_of_insured_item


def get_rate(insuranceinterface):
    print(insuranceinterface.get_rate())


vehicle = VehicleInsurance(100)
home = HomeInsurance(1000)
IInsurance = InsurancePolicy(10)

for insurance in [vehicle, home, IInsurance]:
  get_rate(insurance)

# override built-int methods
# __add__
class Atom:

  def __init__(self, label):
    self.label = label
    
  def __add__(self, other):
    return Molecule([self, other])

    
class Molecule:

  def __init__(self, atoms):
    if type(atoms) is list:
	    self.atoms = atoms    

      
sodium = Atom("Na")
chlorine = Atom("Cl")
# salt = Molecule([sodium, chlorine])
salt = sodium + chlorine


class UserGroup:

  def __init__(self, users, permissions):
    self.user_list = users
    self.permissions = permissions

  def __iter__(self):
    return iter(self.user_list)

  def __len__(self):
    return len(self.user_list)

  def __contains__(self, user):
    return user in self.user_list


class User:

  def __init__(self, username):
    self.username = username


diana = User('diana')
frank = User('frank')
jenn = User('jenn')

can_edit = UserGroup([diana, frank], {'can_edit_page': True})
can_delete = UserGroup([diana, jenn], {'can_delete_posts': True})

print(len(can_edit))

for user in can_edit:
  print(user.username)

if frank in can_delete:
  print("Since when do we allow Frank to delete things? Does no one remember when he accidentally deleted the site?")

print("---------------------------------inheritance and  polymorphism end")

# import different module
print("---------------------------import")

from ModelImpl import ModelImpl
from ActionImpl import ActionImpl

modelImpl = ModelImpl()
actionImpl = ActionImpl()

