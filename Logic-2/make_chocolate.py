# MAKE_CHOCOLATE
def make_chocolate(small, big, goal):
	r = goal-big*5 if goal >= big*5 else goal%5
	if r <= small: return r
	return -1