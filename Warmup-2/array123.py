# ARRAY123
def array123(nums):
  if len(nums)<3: return False
  elif nums == [1,2,3]: return True
  string = ''
  flag = False
  for i in range(len(nums)):
    string += str(nums[i])
  return func1('123', string)

def func1(n, str):
  flag = False
  for i in range(len(str)-3):
    if str[i:i+3] == n:
      flag = True
      break
  if str[len(str)-3:] == '123': flag = True
  return flag