# STRING_MATCH
def string_match(a, b):
  c = 0
  m = min(len(a),len(b))
  for i in range(m-1):
    s1 = a[i:i+2]
    s2 = b[i:i+2]
    if s1 == s2: c += 1
  return c