# SAME_FIRST_LAST
def same_first_last(nums):
  if len(nums) == 1: return True
  elif len(nums) < 1: return False
  else: return True if(nums[0] == nums[len(nums)-1]) else False