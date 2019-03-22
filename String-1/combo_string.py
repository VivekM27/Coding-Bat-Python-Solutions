# COMBO_STRING
def combo_string(a, b):
  if len(a)<1: return b
  elif len(b)<1: return a
  else:
    return a+b+a if(len(a)<len(b)) else b+a+b