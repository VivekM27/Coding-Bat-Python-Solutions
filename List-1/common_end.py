# COMMON_END
def common_end(a, b):
  if len(a) == len(b) and a[0] == b[0]: return True
  elif a[0] == b[0] or a[len(a) - 1] == b[len(b) - 1]: return True
  else: return False