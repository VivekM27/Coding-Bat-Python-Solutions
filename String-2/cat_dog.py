# CAT_DOG
def cat_dog(str):
  c = count(str, 'cat') 
  d = count(str, 'dog')
  return True if(c==d) else False

def count(str, val):
  c = 0;
  i = 0
  while i<len(str):
    if str[i:i+3] == val: c += 1
    i += 1
  return c