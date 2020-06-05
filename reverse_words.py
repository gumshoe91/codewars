'''
Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

'''

def reverse_words(text):

  words = text.split()
  
  rev_list = []
  solution = []
  
  for w in words:
      rev_list.append(list(reversed(w)))
  for r in rev_list:
      solution.append(''.join(r))
  
  double_spaced_str = '  '.join(text.split())
  
  if double_spaced_str == text.strip():
      return '  '.join(solution[0::])
  else:
      return ' '.join(solution[0::])