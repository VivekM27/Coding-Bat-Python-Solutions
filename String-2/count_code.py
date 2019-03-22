# COUNT_CODE
# TRY FOLLOWING CODE IN IDLE PYTHON IDE AS IT WORKS ON IDLE IDE BUT NOT ON CODINGBAT SITE
'''def count_code(str):
  c = 0
  i = 0
  if len(str)<4: return 0
  else:
    while i<len(str):
      if str[i:i+2]=='co' and str[i+3]=='e': c += 1
      i += 1
    return c
print(count_code('vivcopecode'))'''
	
# FOLLWONG CODE WORKS ON CODINGBAT SITE AS WELL
def count_code(str):
  c = 0
  i = 0
  if len(str)<4: return 0
  else:
    while i<len(str):
      if i == len(str)-3: break
      if str[i:i+2]=='co' and str[i+3]=='e': c += 1
      i += 1
    return c