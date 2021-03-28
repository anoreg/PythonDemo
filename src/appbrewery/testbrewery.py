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

# ---------------Type check/error/conversion
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





