# CENTERED_AVERAGE
def centered_average(nums):
	nums.remove(min(nums))
	nums.remove(max(nums))
	return int(sum(nums)/len(nums))