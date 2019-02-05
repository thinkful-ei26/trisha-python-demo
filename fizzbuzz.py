## ======== FIZZBUZZ  ========
my_input = input("Enter an integer \n")
print(my_input)

def fizzbuzz(n):
  start = n - (n-1)
  print('start', start)
  for num in range(start, n):
    if num % 3 == 0:
        print('fizz')
    if num % 5 == 0:
        print('buzz')
    if num % 5 == 0 and num % 3 == 0:
        print('fizzbuzz')
    else:
      print(num)

fizzbuzz(my_input)

## ======== FIZBUZZ USER INPUT ========

