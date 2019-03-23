# BIG_DIFF
def big_diff(nums):
  if len(nums) == 1: return 0
  else:
    Max = nums[len(nums)-1]
    Min = nums[0]
    for i in nums:
      Max = max(Max,i)
      Min = min(Min, i)
  return Max-Min