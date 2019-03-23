# HAS22
def has22(nums):
  i = 0
  while i<len(nums)-1:
    if nums[i] == 2 and nums[i] == nums[i+1]:
      return True
      break
    i += 1
  return False