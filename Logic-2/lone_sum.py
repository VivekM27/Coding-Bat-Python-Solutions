# LONE_SUM
def lone_sum(a, b, c):
  if a==b: return 0 if b==c else c
  elif b==c: return 0 if a==c else a
  elif a==c: return 0 if b==c else b
  else: return a+b+c