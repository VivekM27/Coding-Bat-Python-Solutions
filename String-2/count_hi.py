# COUNT_HI
def count_hi(str):
  c = 0;
  if len(str)>1:
    i = 1
    s = str[0]
    while i<len(str):
      s += str[i]
      if len(s) == 2:
        if s == 'hi':c += 1
        s = s[1]
      else: s = s[1]
      i+=1
    return c
  else: return 0