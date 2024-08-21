"""def last(a):
  return a[-1]
def sort_last(tuples):
  return sorted(tuples, key=last)

def front_x(words):
  # +++your code here+++
  # LAB(begin solution)
  # Put each word into the x_list or the other_list.
  x_list = []
  other_list = []
  for w in words:
    if w.startswith('x'):
      x_list.append(w)
    else:
      other_list.append(w)
  return sorted(x_list) + sorted(other_list)
front_x(['ded', 'mix', 'xyz'])

def front_x(words):
  # +++your code here+++
  # LAB(begin solution)
  # Put each word into the x_list or the other_list.
  x_list = []
  other_list = []
  for w in words:
    if w.startswith('x'):
      x_list.append(w)
    else:
      other_list.append(w)
  return sorted(x_list) + sorted(other_list)
words = ['hey', 'dear', 'xyz']

def match_ends(words):
  # +++your code here+++
  # LAB(begin solution)
  count = 0
  for word in words:
    if len(word) >= 2 and word[0] == word[-1]:
      count = count + 1
  return count
"""