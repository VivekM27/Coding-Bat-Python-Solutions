# ARRAY_FRONT9
def array_front9(nums):
  flag = False
  if len(nums)<1: return False
  elif len(nums)>4:
    for i in range(4):
      if nums[i] == 9:
        flag = True
        break
    return flag
  else:
    for i in range(len(nums)):
      if nums[i] == 9:
          flag = True
          break
    return flag