# CLOSE_FAR
def close_far(a, b, c):
  if abs(a-b)<2:
    return True if abs(b-c)>1 and abs(a-c)>1 else False
  elif abs(b-c)<2:
    return True if abs(c-a)>1 and abs(a-b)>1 else False
  elif abs(c-a)<2:
    return True if abs(a-b)>1 and abs(b-c)>1 else False
  else: return False