# Python Unit 1

## Algorithm #1
Bubble sort

## Algorithm #2

### My solution:
- Given an integer (20), start counting by 0
- If the current number is divisible by 3, print "fizz" and if the number is divisible by 5, print "buzz"
- If the number is neither divisible by 3 nor 5 just print the number
- If the number is divisible by both 3 & 5, print fizz buzz

### Thinkful's Solution:
For each number from 1 to 100:
  If the number is evenly divisible by 3 and evenly divisible by 5 then say FizzBuzz
  Otherwise if the number is evenly divisible by 3 then say Fizz
  Otherwise if the number is evenly divisible by 5 then say Buzz
  Otherwise say the number

## Algorithm #3

For number between 0 to 100:
  Guess the value of x
  Take the number in the middle 50 and compare it x
  Best case scenario is the number is 50
  Otherwise, if x >= 50 , then you can eliminate guesses from 0 to 49. 
  If x < 50, eliminate guessing from 50 to 100, num is between 1 - 49

## Working with Strings
```python
>>> li = [1, 2, 4, 3, 5]
# Select a range between index 1 and 3 (closed/open range, in math terms)
>>> li[1:3]
[2, 4]
# Omit the beginning or end
>>> li[2:]
[4, 3, 5]
>>> li[:3]
[1, 2, 4]
# Select every second entry (i.e. step by 2)
>>> li[::2]
[1, 4, 5]
# Reverse the list
>>> li[::-1]
[5, 3, 4, 2, 1]
# Note the syntax for the above is: li[start:end:step]
# Delete the 3rd item
>>> del li[2]
>>> li
[1, 2, 3, 5]
# Search the list li to see if 1 is in it
>>> 1 in li
True
# What's the length of the list li?
>>> len(li)
4
```

## Working with sets 
```python
# using curly bracket notation
>>> my_set = {1, 2, 2, 3, 4, 5, 6, 7}
>>> my_set
{1, 2, 3, 4, 5, 6, 7}
# using the built-in `set` function
>>> your_set = set([6, 7, 8, 9, 10])
>>> your_set
{8, 9, 10, 6, 7}
# Set intersection - finds the common elements
>>> my_set & your_set
{6, 7}
# Set union - combines the two sets into one
>>> my_set | your_set
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# Set difference - finds the elements in one set but not in the other
>>> my_set - your_set
{1, 2, 3, 4, 5}
# Quickly check if 1 is a member of my_set
>>> 1 in my_set
True
```

## Working with dictionaries
```python
>>> stooges = {"Larry": "balding, with frazzled hair",
               "Curly": "short buzz-cut",
               "Moe"  : "bowl cut"}
>>> stooges
{'Larry': 'balding, with frazzled hair', 'Moe': 'bowl cut', 'Curly': 'short buzz-cut'}
```