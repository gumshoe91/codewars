'''
Bob is preparing to pass IQ test. 
The most frequent task in this test is to find out which one of the given numbers differs from the others. 
Bob observed that one number usually differs from the others in evenness. Help Bob. To check his answers, 
he needs a program that among the given numbers finds one that is different in evenness, and return a position of this number.

Keep in mind that your task is to help Bob solve a real IQ test, which means indexes of the elements start from 1 (not 0)

'''

def iq_test(numbers):    

    number_list = numbers.split()
    
    evens, odds = [], []
    
    for i in number_list:
        if int(i) % 2 == 0:
            evens.append(number_list.index(i))
        else:
            odds.append(number_list.index(i))
        
    if len(evens) == 1:
        return evens[0] + 1
    else:
        return odds[0] + 1