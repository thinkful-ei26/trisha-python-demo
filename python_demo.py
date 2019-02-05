# # ====== First python program in script ======
# print("Hello")

# # ====== basic arithmetic in script ======
# num = 1 + 3 * 2
# print(num)

# # ====== concatenate strings & variables ======
# name = ' trisha'
# print("hello" + name + "time to play!")

# # ====== STRING OPERATIONS ======

# # addition (+)
#first = 'throat'
#second = 'warbler'
#first + second
# throatwarbler

# # multiply strings (3)
# 'Spam'*3  # SpamSpamSpam

# ====== 3.1 FUNCTIONS ======

# int() is a fn that converts floating-point values, BUT doesn't round off (chops @ the fraction part)
# print(int('32')) # 32 ok 
# # print(int('32.02')) # ValueError
# print(int('-32')) # -32 ok 
# # int('hello') # ValueError
# print(int(3.999023)) # 3 ok
# print(int(03.999023)) # 3 ok 

# float() converts integers & strings to floating-point values 
# print(float(32)) # 32.0
# print(float('3.1415')) # 3.1415

# str() converts args to string
# str(32) # '32'
# str(3.1415) # '3.1414'

# ====== 3.2 MATH FUNCTIONS ======
# a module is a file that contains a collection of related fns

# import math 
# print('math: ',math) # ('math: ', <module 'math' from '/usr/local/Cellar/python@2/2.7.15_1/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-dynload/math.so'>)

# ratio = 100 / 10  # 10 arbitrarily
# decibels = 10 * math.log10(ratio)
# print(decibels) # 10.0

# radians = 0.7
# height = math.sin(radians)
# print(height) # 0.644217687238

# degrees = 45
# radians = degrees / 180.0 * math.pi
# height = math.sin(radians)
# print(height) # 0.707106781187

# print('floating point: ',math.sqrt(2) / 2.0)
# print('integer: ',math.sqrt(2) / 2)

# ====== 3.4 ADDING NEW FNS ======

# def print_lyrics(): #header, ending with a colon
#     print("I'm a lumberjack, and I'm okay.")   # body
#     print("I sleep all night and I work all day.")

# print(print_lyrics())
# print('fn object: ',print_lyrics) # <function print_lyrics at 0x10200e578>
# print(type(print_lyrics)) # <type 'function'>

# def repeat_lyrics():
#     print_lyrics()
#     print_lyrics()

# repeat_lyrics()
# print('will invoke fn & then log NONE: ',repeat_lyrics())
# print('fn object: ',repeat_lyrics) # <function print_lyrics at 0x10200e578>
# print(type(repeat_lyrics)) # <type 'function'>

# # MUST DEFINE BEFORE INVOKING
# repeat_lyrics() # NameError: name 'repeat_lyrics' is not defined

# def repeat_lyrics():
#     print_lyrics()
#     print_lyrics()

# def print_lyrics():
#     print("I'm a lumberjack, and I'm okay.")
#     print("I sleep all night and I work all day.")

## ======= 3.8  Variables and parameters are local  =======
# param = variable
# args = actual value passed

# def print_twice(param):
#     print(param)
#     print(param)

# def cat_twice(pt1, pt2):
#   cat = pt1 + pt2
#   print_twice(cat)

## ======= 3.14 Exercises  =======

# def right_justify(s):
#   length = 70 - len(s)
#   spaces = ' '*length
#   print(spaces + s)

# right_justify('monty')

# def do_twice(f):
#   f()
#   f()

# def print_spam(str):
#   print(str)

# def do_twice(str, fn):
#   fn(str)
#   fn(str)

# # do_twice('spam', print_spam) # do_twice takes a fn as an arg

# def do_four(str, fn):
#   fn(str, print_spam)
#   fn(str, print_spam)

# do_four('spam', do_twice)

# def scene():
#   top = '+ - - - - + - - - - +'
#   body = '|         |         |'
#   print(top)
#   print(body)
#   print(body)
#   print(body)
#   print(top)
#   print(body)
#   print(body)
#   print(body)
#   print(top)

# scene()