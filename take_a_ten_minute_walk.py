'''

You live in the city of Cartesia where all roads are laid out in a perfect grid. 
You arrived ten minutes too early to an appointment, so you decided to take the opportunity to go for a short walk. 
The city provides its citizens with a Walk Generating App on their phones -- 
everytime you press the button it sends you an array of one-letter strings representing directions to walk (eg. ['n', 's', 'w', 'e']). 
You always walk only a single block in a direction and you know it takes you one minute to traverse one city block, 
so create a function that will return true if the walk the app gives you will take you exactly ten minutes (you don't want to be early or late!)
and will, of course, return you to your starting point. Return false otherwise.

Note: 
    you will always receive a valid array containing a random assortment of direction letters ('n', 's', 'e', or 'w' only). 
    It will never give you an empty array (that's not a walk, that's standing still!).

'''

from collections import Counter

def is_valid_walk(walk):

    dir_cnt = Counter(list(walk))
    n, s, e, w = 0, 0, 0, 0
    
    if 'n' in dir_cnt:
        n += dir_cnt['n']
        
    if 's' in dir_cnt:
        s += dir_cnt['s']
        
    if 'e' in dir_cnt:
        e += dir_cnt['e'] 

    if 'w' in dir_cnt:
        w += dir_cnt['w'] 

    sum = (abs(dir_cnt['n']-dir_cnt['s']) +abs(dir_cnt['e']-dir_cnt['w']))

    return True if (sum == 0 and (len(walk) == 10)) else False