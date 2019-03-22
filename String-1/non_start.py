# NON_START
def non_start(a, b):
  if len(a) == len(b) and len(a)<1: return ''
  elif len(a)<1: return b[1:]
  elif len(b)<1: return a[1:]
  else: return a[1:]+b[1:]