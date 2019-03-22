# IN1TO10
def in1to10(n, outside_mode):
  return True if((outside_mode==False and (n>0 and n<11)) or (outside_mode==True and (n<2 or n>9))) else False