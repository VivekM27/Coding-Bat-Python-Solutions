# SUM13
def sum13(nums):
  Sum = 0
  i = 0
  while i<len(nums):
    if nums[i] == 13: i += 1
    else: Sum += nums[i]
    i += 1
  return Sum