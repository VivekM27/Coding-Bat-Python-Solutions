# CIGAR_PARTY
def cigar_party(cigars, is_weekend):
  if is_weekend == False and (cigars<40 or cigars>60): return False
  elif is_weekend == True and cigars<40: return False
  else: return True