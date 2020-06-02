'''
In this kata, you must create a digital root function.

A digital root is the recursive sum of all the digits in a number. 
Given n, take the sum of the digits of n. 
If that value has more than one digit, continue reducing in this way until a single-digit number is produced. 
This is only applicable to the natural numbers.

'''

def digital_root(n):

  digits = [int(i) for i in list(str(n))]

  summed = sum(digits)

  while len(str(summed)) >= 1:
      for i in list(str(summed)):
          answer = sum(int(x) for x in list(str(summed)))
          return answer