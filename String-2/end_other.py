# END_OTHER
def end_other(a, b):
  a = a.lower()
  b = b.lower()
  if len(a)>len(b): return check(a,b)
  elif len(a)<len(b): return check(b,a)
  else: return True if a==b else False

def check(x,y):
  val = len(x) - len(y)
  return True if x[val:]==y else False