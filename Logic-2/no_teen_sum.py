# NO_TEEN_SUM
def no_teen_sum(a, b, c):
  return fix_teen(a) + fix_teen(b) + fix_teen(c)
  
def fix_teen(n):
  if (n == 15 or n == 16) or n<13 or n>19: return n
  elif n>12 and n<20: return 0