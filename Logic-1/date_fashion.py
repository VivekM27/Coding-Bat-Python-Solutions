# DATE_FASHION
def date_fashion(you, date):
  if you == date:
    if you<3: return 0
    elif you>2 and you<8: return 1
    else: return 2
  else:
    if(you<3 and date>2) or (you>2 and date<3): return 0
    elif you>2 and you<8 and date>2 and date<8: return 1
    else: return 2