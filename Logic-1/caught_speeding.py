# CAUGHT_SPEEDING
def caught_speeding(speed, is_birthday):
  if not is_birthday:
    if speed<61: return 0
    elif speed>60 and speed<81: return 1
    else: return 2
  else:
    if speed<61+5: return 0
    elif speed>60+5 and speed<81+5: return 1
    else: return 2