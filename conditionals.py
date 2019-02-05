## floor division divides two nums and rounds down to an integer

# minutes = 105
# hours = minutes//60
# print(hours)

# remainder = minutes - hours * 60
# # print('The movie is ' + hours + ' hours ' + ' and ' + remainder + ' minutes') # cannot concatenate 'str' and 'int' objects

# print('The movie is ' + str(hours) + ' hours ' + ' and ' + str(remainder) + ' minutes')

## ========== 5.11 KEYBOARD INPUT ==========

# temp = input('What is your name? \n')
# temp

## ========== 7.3 WHILE STATEMENT ==========

# def countdown(n):
#   while n > 0:
#     print(n)
#     n = n -1
#   print('Blastoff!')

# countdown(3)

# while True:
#     line = input('> ')
#     if line == 'done':
#         break
#     print(line)

# print('Done!')


## ========== 8.3 FOR LOOP ==========
prefixes = 'JKLMNOPQ'
suffix = 'ack'

for letter in prefixes:
    print(letter + suffix)