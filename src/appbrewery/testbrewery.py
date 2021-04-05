import random
import bmi
# ----------------Input
# input always return a string as a result
# print("hello:" + input("what's your name"))

# ----------------String
print("123" + "456")
print(len("hello"[1]))  # subscript

# ----------------Integer
print(123 + 456)
i = 123_456_789
print(i)

# --------------Type check/error/conversion
# type check
num_char = 87
print(type(num_char))
# type conversion
print("It's string " + str(num_char))
print(float(num_char))
two_digit = str(num_char)
print(int(two_digit[0]) + int(two_digit[1]))


# --------------Math operator
print(type(6 / 3))
print(3 * 2)  # asterisk
print(3 ** 2)  # exponent

# Priority: PEMDASLR(Parentheses, Exponent, Multiplication & Division, Addition & Subtraction, Left & Right)
# (), **, * /, + -
print(3 * (3 + 3) / 3 - 3)  # Left is prior to Right

# round numbers
print(round(8 / 3, 2))  # keep 2 decimals
print(8 // 3)  # get integer instead of the default the float value

# f-string (front of string)
value = 12
print(f"value: {value}")

# ternary operator
number = 11
print("Even number" if number % 2 == 0 else "Odd number")

# leap year
year = 2020
isLeapYear = (year % 400 == 0) | ((year % 4 == 0) & (year % 100 != 0))
print(f"isLeapYear {isLeapYear}")

# type hint(introduced from python3.5)
typehint: int = "11.5"
print(f"typehint {typehint}")
print(type(typehint))

# --------------------String
str_value: str = "String String value"
print("lowercase " + str_value.lower())
print(str_value.count("S"))
print('''Multiline string
 ________________________________________________________
/  ____________________________________________________  \
| |<_> <_> <_> <_> <_> <_> <_> <_> <_> <_> <_> <_> <_> | |
| |_|___|___|___|___|___|___|___|___|___|___|___|___|__| |
|  ____________________________________________________  |
| | |   |   |   |   |   |   |   |   |   |   |   |   |  | |
| |<_> <_> <_> <_> <_> <_> <_> <_> <_> <_> <_> <_> <_> | |
| |<_> <_> <_> <_> <_> <_> <_> <_> <_> <_> <_> <_> <_> | |
| |<_> <_> <_> <_> <_> <_> <_> <_> <_> <_> <_> <_> <_> | |
| |<_> <_> <_> <_> <_> <_> <_> <_> <_> <_> <_> <_> <_> | |
| |<_>_<_>_<_>_<_>_<_>_<_>_<_>_<_>_<_>_<_>_<_>_<_>_<_>_| |
\___________________________________________________LGB__/
''')

# --------------------Random
print(random.randint(0, 10))
print(random.random())  # random float, return [0.0, 1.0)
print(random.uniform(1, 10))  # random float return[a, b)
print(bmi.roundedBMI)
randomNames = [1, 2, 3]
print(f"random choice: {random.choice(randomNames)}")

# -------------------- List
fruits = ["item1", "item2"]
print(fruits[0] + fruits[-2])  # both positive and negative index
fruits.append("item3")  # add single item to end of list
print(fruits)
fruits.extend(["item4", "item5"])  # add items to end of list
print(fruits)

namesStr = "A, B, C"
names = namesStr.split(", ")
print(names)

dyadicList = [[1, 2, 3], [4, 5, 6]]  # dyadic list
print(f"sum([1, 2, 3]): {sum(dyadicList[0])}")

# -------------------- Map
row1 = [1, 2, 3]
row2 = [4, 5, 6]
row3 = [7, 8, 9]
rowMap = [row1, row2, row3]
print(f"row map:\n{row1}\n{row2}\n{row3}")
vertical = 2  # row
horizontal = 1  # column
print(f"point {vertical, horizontal} is {rowMap[vertical][horizontal]}")

# ------------------------- Loop
for fruit in fruits:
    print(f"loop {fruit}", end=",")
    # TODO: do sth.
print("loop end")

# [0, 10), step = 2, all even num between 0 ~ 10
for num in range(0, 10, 2):
    print(f"loop range {num}", end=",")
print("range end")


