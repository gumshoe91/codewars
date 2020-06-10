'''
Your task is to write function find_sum.

Upto and including n, this function will return the sum of all multiples of 3 and 5.

For example:

find_sum(5) should return 8 (3 + 5)

find_sum(10) should return 33 (3 + 5 + 6 + 9 + 10)

'''

def find_sum(n):
    sum = 0
    for i in range(n+1):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum