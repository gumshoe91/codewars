
'''
Write a function named sumDigits which takes a number as input 
and returns the sum of the absolute value 
of each of the number's decimal digits.

'''

import re

def sum_digits(number):

    num_string = str(number)
    
    dig_str_list = re.findall(r'\d', num_string)
    
    dig_list = [int(i) for i in dig_str_list]
    
    return sum(dig_list)