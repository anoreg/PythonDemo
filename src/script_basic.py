# -*- coding: utf-8 -*-
# system default encoding is utf-8, you can chage to another by adding the comment above
#----------------------------my first python demo
my_name = "Fahy"
print("Hello and welcome " + my_name + "!")
print('single quote works well')

var_example_5 = "variable"
print(var_example_5)
# python variable is case-sensitive
# variable scope (A-z, 0-9, _)
x = 1  # int
y = 2.8  # float
z = 1j  # complex
print(type(x), type(y), type(z))
print(x + z)
# isinstance
print(isinstance(x, int))


class A:
    pass


class B(A):
    pass


isinstance(A(), A)  # returns True
type(A()) == A  # returns True
isinstance(B(), A)  # returns True
type(B()) == A  # returns False
# type()不会认为子类是一种父类类型。
# isinstance()会认为子类是一种父类类型
# Note：在 Python2 中是没有布尔型的，它用数字 0 表示 False，用 1 表示 True。到 Python3 中，把 True 和 False 定义成关键字了，但它们的值还是 1 和 0，它们可以和数字相加。

# print
print("hello")
print("hello", end=" ")  # defult end is \n, replace it with " "
print("hello")
#-----------------------------math
print("--------------------------------------math module start")
a = input("\n\nreceive use input")
print(a) 
print(25 * 68 + 13 / 28)
# 指数exponnent, 8的2次方 print 64
print(8 ** 2)
# 4 to the half power, or 2
print(4 ** 0.5)

a, b = 0, 1
a, b = b, a + b
print(a)

birthday_string = "I am "
age = 10
birthday_string_2 = " years old today!"

# Note: Multiplying a string just makes a new string with the old one repeated!
repeat = "na" * 6
print("repeat na 6 times is: " + repeat)

# 1、Python可以同时为多个变量赋值，如a, b = 1, 2。
# 2、一个变量可以通过赋值指向不同类型的对象。
# 3、数值的除法包含两个运算符：/ 返回一个浮点数，// 返回一个整数。
# 4、在混合计算时，Python会把整型转换成为浮点数
print("----------------------------------math module end")

#-----------------------------string
print("----------------------------------------------string module start")
full_birthday_string = birthday_string + str(age) + birthday_string_2

# Prints "I am 10 years old today!"
print(full_birthday_string)

# If you're trying to print() a numeric variable
# you can use commas to pass it as a different argument
# rather than converting it to a string.
# This also prints "I am 10 years old today!"
print(birthday_string, age, birthday_string_2)

# multiline str
multi_str1 = """
hello, we want to have
dinner, go with us? """
print(multi_str1)
multi_str2 = '''
hello, we want to have
dinner, go with us? '''
print(multi_str2)

# multiline comment
# use triple-quoted strings. When they're not a docstring (first thing in a class/function/module), they are ignored.
"""sfahe
afadsf"""
print("multiline comment")

# str() repr()
# str()： 函数返回一个用户易读的表达形式
# repr()： 产生一个解释器易读的表达形式, 可以转义字符串中的特殊字符, 参数可以是 Python 的任何对象
strn = "hello\n"
print("str:", str(strn))
print("repr:", repr(strn))

# slice
my_name = "fahy"
print(my_name[1:3], my_name[1:], my_name[:2], my_name[-1], my_name[-3:-1])
# escape characters
my_str = "hey ! \"bob\""
print(my_str, "ey" in my_str)
# split str
mysplit = "ba na na"
print(mysplit.split(), mysplit.split("n"), mysplit.split("a"))
# join str, use delimiter to join each words, for example the space " "
reapers_line_one_words = ["Black", "reapers", "with", "the", "sound", "of", "steel", "on", "stones"]
reapers_line_one = " ".join(reapers_line_one_words)
print(reapers_line_one)
# find str return indice
god_wills_it_line_one = "The very earth will disown you"
disown_placement = god_wills_it_line_one.find("disown")
print(disown_placement)

# format str according to arguments order
def poem_title_card(poet, title, times):
    poem_desc = "The poem \"{}\" is written by {}, {} times".format(title, poet, times)
    return poem_desc


print(poem_title_card("Walt Whitman", "I Hear America Singing", 10))


# format str with placeholder makes str more readable
def poem_description(publishing_date, author, title, original_work):
    poem_desc = "The poem {title} by {author} was originally published in {original_work} in {publishing_date}.".format(publishing_date=publishing_date, author=author, title=title, original_work=original_work)
    return poem_desc


my_beard_description = poem_description(1974, "Shel Silverstein", "My Beard", "Where the Sidewalk Ends")
print(my_beard_description)
# format str with typed placeholder in old python version 
print("%s 说: 我 %d 岁。" % ("hf", 10))

# '!a' (使用 ascii()), '!s' (使用 str()) 和 '!r' (使用 repr()) 可以用于在格式化某个值之前对其进行转化:
fpi = 3.1415926
print('常量 PI 的值近似为: {}。'.format(fpi))
print('常量 PI 的值近似为: {!r}。'.format(fpi))

# 可选项 ':' 和格式标识符可以跟着字段名。 这就允许对值进行更好的格式化。 下面的例子将 Pi 保留到小数点后三位：
print('常量 PI 的值近似为: {0:.3f}。'.format(fpi))

# 在 ':' 后传入一个整数, 可以保证该域至少有这么多的宽度。 用于美化表格时很有用。
table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
for name, number in table.items():
    print('{0:10} ==> {1:10d}'.format(name, number))


print("---------------------------------------string module end")

#------------------------------function
print("-----------------------------------------function module start")
def loading_screen():
    print("This page is loading...")


loading_screen()


# using intend to seperate in function or out of function
def about_this_computer():
	print("This computer is running on Whackintosh version Everest Puma")


print("This is your desktop")
about_this_computer()


# fuction parameters, using keyword paramters, defind a default value to the keyword
def create_spreadsheet(title, row_count=1000):
  print("Creating a spreadsheet called " + title + " with " + str(row_count) + " rows.")

  
create_spreadsheet("Downloads")
create_spreadsheet("Applications", 10)
create_spreadsheet("Applications", row_count=10)


# function return
# single return
def calculate_age(current_year, birth_year):
  age = current_year - birth_year
  return age


my_age = calculate_age(2018, 1993)
dads_age = calculate_age(2018, 1953)
print("I am " + str(my_age) + " years old and my data is " + str(dads_age) + " years old")


# multi return
def get_boundaries(target, margin):
  low_limit = target - margin
  high_limit = target + margin
  return low_limit, high_limit


low, high = get_boundaries(100, 20)
print("Low limit: " + str(low) + ", high limit: " + str(high))
print("--------------------------------------function module end")
     
#-----------------------Flow, Data, and Iteration
print("-------------------------------------------if elif else, operator, try start")
# bool
isSuccess = True
isFail = False
print(isSuccess, isFail)


# if elif else
def greater_than(x, y):
  if x != y:
    print("These numbers are not same")
    if x > y:
      return x
    else:
      return y 
  else:
    return "These numbers are the same"

    
print(greater_than(10, 9))

    
def graduation_reqs(credits):
  if credits >= 120:
    return "You have enough credits to graduate!"

  
print(graduation_reqs(120))
# three statement
result = True if 2 > 1 else False
print("ternary expression:" + str(result))
# and or not, It likes && || !
print(1 + 1 < 3 and 2 + 2 > 3)
print(1 + 1 < 1 or 2 + 2 > 3)
# not should place at the very beigin of the statement
print(not (4 + 5 <= 9))
print(not 3 != 4)
gpa = 4
credits = 110
if (gpa >= 2.0) and not (credits >= 120):
    print("you don't have enough credit")


# try except
# throw a exception like java
def raises_value_error():
  raise ValueError


try:
	raises_value_error()
except ValueError as err:
  print("You raised a ValueError:{}".format(err))
except:
  # 最后一个except子句可以忽略异常的名称，它将被当作通配符使用。你可以使用这种方法打印一个错误信息，然后再次把异常抛出。
  print("Unexcept error")

#try:
#    do something
#except (AError, BError, CError):
#    do something

print("-------------------------------------------------if elif else, operator, try end")

#------------------------------------------list
print("--------------------------------------list module start")
ints_and_strings = [1, 2, 3, 'four', 'five']
ages = [['Aaron', 15], ['Dhruti', 16]]
# zip list
names = ['Jenny', 'Alexus', 'Sam', 'Grace']
heights = [61, 70, 67, 65]
names_and_heights = zip(names, heights)
print(names_and_heights)
print(list(names_and_heights))
my_empty_list = []
my_empty_list.append(1)
print(my_empty_list)

new_list = my_empty_list + [4]
print(new_list, my_empty_list)
# range,
# generates numbers starting at 0 and ending at the number before the input
my_range = range(10)
print(list(my_range))
# create a list that starts at a different number
my_list = range(2, 9)
print(list(my_list))
# range(2, 9, 2) will give us a list where each number is 2 greater than the previous number:
# the third args means the skip num, create list from 2-9
my_range2 = range(2, 9, 2)
print(list(my_range2))

# select last element
print(my_list[-1])
# slice list
suitcase = ['shirt', 'books', 'pants', 'glass', 'pajamas']
beginning = suitcase[0:4]

midlen = len(suitcase) / 2
floorlen = len(suitcase) // 2
print(midlen, floorlen)

middle = suitcase[floorlen - 1 : floorlen + 1]
print(beginning, middle)

start3 = suitcase[:3]
last3 = suitcase[-3:]
start1ToEnd = suitcase[1:]
print(start3, last3, start1ToEnd)

# count elements in list
votes = ['Jake', 'Jake', 'Laurie', 'Laurie', 'Laurie', 'Jake', 'Jake', 'Jake', 'Laurie', 'Cassie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie']

jake_votes = votes.count('Jake')
print(jake_votes)
# sort list
# sort() doesn't generate a new list, only affect origin list
suitcase.sort()
print(suitcase, suitcase.sort())
# sorted generate new list but don't affect origin list
games = ['Portal', 'Minecraft', 'Pacman', 'Tetris', 'The Sims', 'Pokemon']
games_sorted = sorted(games)
print(games, games_sorted)


# remove elements
def remove_middle(lst, start, end):
#  return lst[:start] + lst[end+1:]
  del lst[start:end + 1]
  return lst


print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))


# middle element
def middle_element(lst):
  count = len(lst)
  if count % 2 == 0:
    mid = int(count / 2)
    sum = lst[mid] + lst[mid - 1]
    return sum / 2
  else:
    return lst[mid]


print(middle_element([5, 2, -10, -4, 4, 5]))

print("---------------------------------list module end")
#-------------------------------------------------loop
print("-----------------------------------loop module start")
dog_breeds = ['french_bulldog', 'dalmation', 'shihtzu', 'poodle', 'collie']
for breed in dog_breeds:
    if breed == 'french_bulldog':
      continue
    if breed == 'poodle':
      break
    print(breed)
    
for i in range(3):
    print("hello" + str(i))

all_students = ["Alex", "Briana", "Cheri", "Daniele", "Dora", "Minerva", "Alexa", "Obie", "Arius", "Loki"]
students_in_poetry = []

for i in range(3):
  print("index:" + str(i))
  student = all_students.pop(i)
  students_in_poetry.append(student)
  
print(students_in_poetry)

# List Comprehensions
words = ["@coolguy35", "#nofilter", "@kewldawg54", "reply", "timestamp", "@matchamom", "follow", "#updog"]
usernames = []
usernames = [word for word in words if word[0] == '@']
copyList = []
copyList = [word for word in words]
print(usernames, copyList)

messages = [user + " please follow me!" for user in usernames]
print(messages)

celsius = [0, 10, 15, 32, -5, 27, 3]
fahrenheit = [temp * (9 / 5) + 32 for temp in celsius]
print(fahrenheit)
# 列表嵌套解析
matrix_3_4 = [
     [1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12]
]
matrix_4_3 = [[row[i] for row in matrix_3_4] for i in range(4)]
print(matrix_4_3)

print("----------------------------------------loop module end")

#---------------------------------------module
print("-------------------------------------import module start")
# 1. 一个模块只会被导入一次，不管你执行了多少次import。这样可以防止导入模块被一遍又一遍地执行
# 2. Python的搜索路径，搜索路径是由一系列目录名组成的，Python解释器就依次从这些目录中去寻找所引入的模块。
# 3. 搜索路径是在Python编译或安装的时候确定的，安装新的库应该也会修改。搜索路径被存储在sys模块中的path变量
# 4. sys.path 返回路径列表, 通过 sys.path.append(path) 追加引用模块路径, sys.path[0] 一般是当前路径
# 5. 语法:
# a. 在 python 用 import 或者 from...import 来导入相应的模块。
# b. 将整个模块(somemodule)导入，格式为： import somemodule
# c. 从某个模块中导入某个函数,格式为： from somemodule import somefunction
# d. 从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc
# e. 将某个模块中的全部函数导入，格式为： from somemodule import *
import sys
print(sys.path) 

from sys import api_version
print(api_version)

# __name__属性, 每个模块都有一个__name__属性
# 一个模块被另一个程序第一次引入时，其主程序将运行。如果我们想在模块被引入时，模块中的某一程序块不执行，我们可以用__name__属性来使该程序块仅在该模块自身运行时执行。
#!/usr/bin/python3
# Filename: using_name.py

if __name__ == '__main__':
    print('程序自身在运行')
else:
    print('我来自另一模块')
   
# $ python using_name.py
# 程序自身在运行

# $ python
# >>> import using_name
# 我来自另一模块

print("-----------------------------import module end")

# -----------------------------------------dictionary
print("-------------------------------------------dictionary module start")
my_map = {"1":1, 2:2}
print(my_map)
user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
user_ids.update({"theLooper": 138475, "stringQueen": 85739})
print(user_ids)

# List Comprehensions to Dictionaries
# demo1
drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]
zipped_drinks = zip(drinks, caffeine)
drinks_to_caffeine = {key:value for key, value in zipped_drinks}
print(drinks_to_caffeine)
songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]
# demo2
plays = {song:playcount for [song, playcount] in zip(songs, playcounts)}
print(plays)
# get value raise exception
caffeine_level = {"espresso": 64, "chai": 40, "decaf": 0, "drip": 120}
try:
  print(caffeine_level['matcha'])
except KeyError:
  print("Unknown Caffeine Level")
# get value safely
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
tc_id = user_ids.get("teraCoder", 100000)
print(tc_id)
stack_id = user_ids.get("superStackSmash", 100000)
print(stack_id)
java_id = user_ids.get("javaid")
print(java_id)
# remove value
user_pop = user_ids.pop("teraCoder")
print(user_pop)
user_pop = user_ids.pop("tera", 1000)
print(user_pop)
# get keys, values, they ar view object which can't be modified
print(user_ids.keys(), user_ids.values())
print(list(user_ids.values()))
for x, y in user_ids.items():
  print(x, y)
  
# keyword
import keyword
print(keyword.kwlist)
# ['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

print("-------------------------------------dictionary module end")
#-------------------------------tuple
print("---------------------------------------tuple module start")
# tuple element can't be modified, but the element can be editable item like list, or dict
tup = (1, 2, 3, 4, 5, 6)
tup1 = ()  # 空元组
tup2 = (20,)  # 一个元素，需要在元素后添加逗号
print(tup[0])
print(tup[1:5])
print(tup + tup2)
# 元组在输出时总是有括号的，以便于正确表达嵌套结构。在输入时可能有或没有括号， 不过括号通常是必须的（如果元组是更大的表达式的一部分）
# string、list和tuple都属于sequence（序列）。

print("-----------------------------------tuple module end")
#------------------------------------set
print("-----------------------------------set module start")
# 无重复集合
student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'} 
print(student)  # 输出集合，重复的元素被自动去掉

emptyset = set()
print(emptyset)

thisset = set(("apple", "banana", "cherry", "apple"))  # note the double round-brackets
print(thisset)

# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')
 
print(a)
print(a - b)  # a 和 b 的差集
print(a | b)  # a 和 b 的并集
print(a & b)  # a 和 b 的交集
print(a ^ b)  # a 和 b 中不同时存在的元素

# update
emptyset.update(thisset)
emptyset.update(["orange", "mango", "grapes"])
print(emptyset)

print("--------------------------------set module end")

# -------------------------------file
print("---------------------------------file module start")
# open(filename, mode[optional, default r])
# check mode at http://www.runoob.com/python3/python3-inputoutput.html
# mode: r: read, x: create, a: append, w: write, b: open as binary, +: pointer of file will start at beginning

# read file
fname = "../testfile"
f = open(fname, "a")
f.write("append sentence\n")
f.close()

f = open(fname)
flimit = f.read(5)
print("limit:\n{}".format(flimit))
fcontent = f.read()
print("content:\n{}".format(fcontent))
f.close()
# after read, the pointer will move to end of the read line

# read line 
# 从文件中读取单独的一行。换行符为 '\n'。f.readline() 如果返回一个空字符串, 说明已经已经读取到最后一行。
f = open(fname)
line = f.readline()
print("line: " + line)
f.close()

# read lines
# 返回该文件中包含的所有行。如果设置可选参数 sizehint, 则读取指定长度的字节, 并且将这些字节按行分割。
f = open(fname)
print("lines:\n{}".format(f.readlines()))
f.close()

f = open(fname)
for line in f:
    print(line, end="")
f.close()

# write file
wname = "../testfilewrite"
f = open(wname, "w")
num = f.write("hello")
print("char wrote: {}".format(num))
f.close()

# serial object
# pickle: pickle.dump(obj, file, [,protocol])
import pickle
import pprint
data1 = {'a': [1, 2.0, 3, 4 + 6j],
         'b': ('string', u'Unicode string'),
         'c': None}

# serializable         
output = open('../data.pkl', 'wb')
# Pickle dictionary using protocol 0.
pickle.dump(data1, output)
output.close()

# unserializable
pkl_file = open('../data.pkl', 'rb')
data1 = pickle.load(pkl_file)
pprint.pprint(data1)
pkl_file.close()

# with
# 当处理一个文件对象时, 使用 with 关键字是非常好的方式。在结束后, 它会帮你正确的关闭文件。 而且写起来也比 try - finally 语句块要简短:
with open(fname) as f:
    read_data = f.read()
print(f.closed)

#-----------------------------------os
import os

os.chdir("../")
cur_dir = os.getcwd()
print(cur_dir)

create_dir = "testdir"
if os.path.exists(create_dir) and os.path.isdir(create_dir):
    content = os.listdir(create_dir)
    if content:
        for path in content:
            filepath = os.path.join(create_dir, path)
            print(filepath)
            if os.path.isfile(filepath):
                os.remove(filepath)
            else:
                os.rmdir(filepath)
    os.rmdir(create_dir)
os.mkdir(create_dir)
print(os.listdir(cur_dir))  # only unix, windows

fdfile = os.path.join(create_dir, "foo.txt")
print("filedir:{}, filename:{}".format(os.path.dirname(fdfile), os.path.basename(fdfile)))
fd = os.open(fdfile, os.O_RDWR | os.O_CREAT)
strbytes = "hello, this is a test file, 你好, 这是测试文件".encode()
print(strbytes)
os.write(fd, strbytes);
os.close(fd)

fd = os.open(fdfile, os.O_RDWR)
content = os.read(fd, os.path.getsize(fdfile))
print(content.decode())

newname = os.path.join(create_dir, "testosfile")
os.rename(fdfile, newname)
print(os.listdir(create_dir))
print(os.path.getctime(newname))  # seconds as unit

os.system("mkdir systemcmd") # 执行系统命令 mkdir
print(os.listdir(cur_dir))

os.chdir("src") # go back to src working directory
print(os.getcwd())
print("---------------------------------file module end")

print("---------------------------------standard lib start")
# print(dir(os)) # returns a list of all module functions
# help(os) # returns an extensive manual page created from the module's docstrings

# 针对日常的文件和目录管理任务，:mod:shutil 模块提供了一个易于使用的高级接口:
import shutil
shutil.copyfile('../data.pkl', '../systemcmd/archive.db')

# File Wildcards 文件通配符
import glob
print(glob.glob('*.py')) # search all file which name contains *.py

# command line arguments
# 通用工具脚本经常调用命令行参数。这些命令行参数以链表形式存储于 sys 模块的 argv 变量。例如在命令行中执行 "python demo.py one two three" 后可以得到以下输出结果:
import sys
print(sys.argv)

# 错误输出重定向和程序终止, 大多脚本的定向终止都使用 "sys.exit()"。
sys.stderr.write("this is a error\n")

# datetime
from datetime import datetime

print("----------------------datetime module")
i = datetime.now()
print ("当前的日期和时间是 %s" % i)
print ("ISO格式的日期和时间是 %s" % i.isoformat() )
print ("当前的年份是 %s" %i.year)
print ("当前的月份是 %s" %i.month)
print ("当前的日期是  %s" %i.day)
print ("dd/mm/yyyy 格式是  %s/%s/%s" % (i.day, i.month, i.year) )
print ("当前小时是 %s" %i.hour)
print ("当前分钟是 %s" %i.minute)
print ("当前秒是  %s" %i.second)

from datetime import date
today = date.today()
print("today:" + str(today))
mydate = date(2018, 11, 11) # new a date instance with specific time
print(mydate.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))

# dates support calendar arithmetic
birthday = date(1989, 7, 30)
age = today - birthday
print("age:{}; days:{}; years:{}".format(age, age.days, age.days/365))

# time
import time

print("---------------time module")
print ('在'+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+'，我写了人生中第一行Python代码\n它的内容虽然简单，不过是平凡的一句print(1+1)\n但我知道：人类传承千万年的璀璨文明，正是从最简单的1+1开始\n我的编程之路亦如此，一切在这一刻起开始变得不同\n以下，是这行代码的运算结果：' )

ticks = time.time()
print ("当前时间戳为:", ticks)
localtime = time.localtime(ticks)
print ("本地时间为 :", localtime)
simple_converttime = time.asctime(localtime)
print("本地时间为 :", simple_converttime)
# 格式化成2016-03-20 11:45:39形式
print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
# 格式化成Sat Mar 28 22:24:24 2016形式
print (time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))
# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2018"
print (time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")))
# python中时间日期格式化符号：
'''
%y 两位数的年份表示（00-99）
%Y 四位数的年份表示（000-9999）
%m 月份（01-12）
%d 月内中的一天（0-31）
%H 24小时制小时数（0-23）
%I 12小时制小时数（01-12）
%M 分钟数（00=59）
%S 秒（00-59）
%a 本地简化星期名称
%A 本地完整星期名称
%b 本地简化的月份名称
%B 本地完整的月份名称
%c 本地相应的日期表示和时间表示
%j 年内的一天（001-366）
%p 本地A.M.或P.M.的等价符
%U 一年中的星期数（00-53）星期天为星期的开始
%w 星期（0-6），星期天为星期的开始
%W 一年中的星期数（00-53）星期一为星期的开始
%x 本地相应的日期表示
%X 本地相应的时间表示
%Z 当前时区的名称
%% %号本身
'''

# Import random below:
import random
# Create random_list below:
random_list = [random.randint(1, 101) for i in range(101)]
print(random_list)
# Create randomer_number below:
randomer_number = random.choice(random_list)
# Print randomer_number below:
print(randomer_number)

random_sample = random.sample(range(100), 10) # # sampling without replacement
print(random_sample)
random_float = random.random() # random float
print(random_float) 
random_range_float = random.uniform(1.5, 1.9) # return N between (a, b) included
print(random_range_float)
random_int = random.randrange(6)    # random integer chosen from range(6)
print(random_int)

# platform
import platform
print(platform.system()) # 获取当前运行系统
#dir(platform)

# zlib, 直接支持通用的数据打包和压缩格式：zlib，gzip，bz2，zipfile，以及 tarfile
import zlib
s = b"witch which has which witches wrist watch" # convert str to bytes
print(len(s))
t = zlib.compress(s) # accept bytes
print(len(t))
print(zlib.decompress(t))
print(zlib.crc32(s)) # checksum

# performance
# 使用元祖交换元素值
from timeit import Timer
t = Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
print(t)
t =  Timer('a,b = b,a', 'a=1; b=2').timeit()
print(t)
# 相对于 timeit 的细粒度，:mod:profile 和 pstats 模块提供了针对更大代码块的时间度量工具。

# test module
# doctest
def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

import doctest
print(doctest.testmod())   # 自动验证嵌入测试

# unittest, unittest模块不像 doctest模块那么容易使用，不过它可以在一个独立的文件里提供一个更全面的测试集:
import unittest

class TestStatisticalFunctions(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        self.assertRaises(ZeroDivisionError, average, [])
        self.assertRaises(TypeError, average, 20, 30, 70)

print(unittest.main()) # Calling from the command line invokes all tests

# decimal
from decimal import Decimal

# Fix the floating point math below:
three_decimal_points = 0.2 + 0.69
print(three_decimal_points)

four_decimal_points = 0.53 * 0.65
print(four_decimal_points)

three_decimal_points = Decimal("0.2") + Decimal("0.69")
print(three_decimal_points)

four_decimal_points = Decimal("0.53") * Decimal("0.65")
print(four_decimal_points)

print("---------------------------------standard lib end")
