# SUM67
def sum67(nums):
  sum = 0
  i = 0
  c = 0
  while i<len(nums):
    if nums[i] == 6:
      c += 1
    elif c>0:
      if nums[i] == 7: c = 0
      else: c += 1
    else: 
      sum += nums[i]
    i += 1
  return sum