'''
You are going to be given a word. Your job is to return the middle character of the word.

If the word's length is odd, return the middle character.

If the word's length is even, return the middle 2 characters.

'''

def get_middle(s):
    str_list = list(s)
    if len(str_list) % 2 == 0:
        return str_list[(len(str_list) // 2) - 1] + str_list[len(str_list) // 2]
    else:
        return str_list[len(str_list) // 2]