# Learning A Language (Python)
# 1. Terms
# 2. Data Types
# 3. Variables
# 4. Actions
# 5. Best Practices

int
float
bool
str
tuple
set
dict

# FUNDAMENTAL DATA TYPES

# int and float
# print(type(2 + 4))
# print(type(2 - 4))
# print(type(2 * 4))
# print(type(2 / 4))

# print(2 ** 2)
# print(2 // 4)
# print(5 % 4)

# # math functions
# print(round(3.9))
# print(abs(-20))

# # operator precedence

# print(20 + 3 * 4)

# # ()
# # **
# # * /
# # + -

# # print((5 + 4) * 10 / 2) # 45

# # print(((5 + 4) * 10) / 2) # 45

# # print((5 + 4) * (10 / 2)) # 45

# # print(5 + (4 * 10) / 2) # 25

# # print(5 + 4 * 10 // 2) # 0

# print(bin(5))
# print(int('0b101' , 2))

# # VARIABLES
# # snake_case
# # start with a lowercase or underscore
# # letters, numbers, underscores
# # case sensistive
# # don't overwrite

# iq = 190
# user_age = iq/4

# print(user_age)
# a,b,c = 1,2,3
# print(a)
# print(b)
# print(c)

# # CONSTANTS

# PI = 3.14

# # expressions and statements

# iq = 100
# user_age = iq / 5

# # augmented assignement operator

# some_value = 5
# some_value = 5 + 2

# # STRING

# first_name = 'Stefan'
# last_name = 'James'
# full_name = first_name + ' ' + last_name
# print(full_name)

# # Escape Sequence

# weather = "It\'s sunny"
# print(weather)

# # formatted strings

# name = 'Stefan'
# age = '36'

# print('Hi ' + name + '. You are ' + age + ' years old.')

# selfish = '01234567'
#         #  01234567

# # [start:stop:stepover]
# print(selfish[0:8:2])

# # BOOLEANS = True or False
# name = 'Stefan'
# is_cool = False
# is_cool = True

# name = 'Stefan James'
# age = 36
# relationship_status = 'married'
# print(relationship_status)

# birth_year = input('what year were you born?')

# age = 2020 - int(birth_year)

# print(f'your age is:{age}')

#Classes -> custom types

#Specialized Data Types

# None

# username = input('what is your username?')
# password= input('what is your password?')

# password_length = len(password)
# hidden_password = '*' * password_length

# print(f'{username}, your password, {hidden_password} is {password_length} letters long')

# Matrix

# matrix = [
#   [1,2,3],
#   [2,4,6],
#   [7,8,9]
# ]
# print(matrix)

# weapons = None

# DICTIONARY (unordered key value pair)
# dictionary = {
# 'weapons' : [1,2,3],
# 'greeting' : 'hello',
# 'is_Magic' : True
# }

# user = {
#   'basket': [1,2,3],
#   'greet' : 'hello',
#   'age' : 21
# }

# print (user.items())

# Tuple (immutable lists)
# my_tuple = (1,2,3,4,5)
# print(my_tuple.index(5))

# SET (unordered collection of unique objects)

# my_set = {1,2,3,4,5,}
# your_set = {4,5,6,7,8,9,10}

# print(my_set.difference(your_set))
# .dis

is_old = 'hello'
is_licensed = True

if is_old and is_licensed:
    print('you are old enough to drive, and you have a license!')

else:
    print('you are not of age')

print('okoko')

# Truthy and Falsy

# Tenary Operator 

# condition_if_true if condition else condition_if_else
is_friend = False
can_message = "message allowed" if is_friend else "not allowed to message"
print(can_message)

# Short Circuting
is_Friend = True
is_User = True

is_Friend and is_User:
print('best friends forever')