# ALARM_CLOCK
def alarm_clock(day, vacation):
  if vacation: return 'off' if day==0 or day==6 else '10:00'
  else: return '10:00' if day==0 or day==6 else '7:00'