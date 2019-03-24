# MAKE_BRICKS
def make_bricks(small, big, goal):
  return True if(goal%5 <= small and goal-(big*5) <= small) else False
