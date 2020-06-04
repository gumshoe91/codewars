'''
Write a function that turns a string of words (e.g. "hello my friend") into PascalCase ("HelloMyFriend").

'''

def pascal_case(string):
    str_list = string.split(" ")
    capitalized = []
    for s in str_list:
        capitalized.append(s.capitalize())
        
    return "".join(capitalized)