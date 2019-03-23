# ROUND_SUM
def round_sum(a, b, c):
  return round10(a) + round10(b) + round10(c)

def round10(n):
  if n%10>4: 
    n/=10
    return (n+1) * 10
  else:
    n/=10
    return n * 10