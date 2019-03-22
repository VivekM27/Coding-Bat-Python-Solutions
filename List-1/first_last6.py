# FIRST_LAST6
def first_last6(nums):
  if (len(nums) == 1 and nums == 6) or (nums[0] == 6 or nums[len(nums)-1] == 6): return True
  else: return False