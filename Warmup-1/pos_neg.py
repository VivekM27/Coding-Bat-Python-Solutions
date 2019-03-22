# POS_NEG
def pos_neg(a, b, negative):
  return True if((negative == True and a<0 and b<0) or(negative == False and ((a>0 and b<0)or(a<0 and b>0)))) else False