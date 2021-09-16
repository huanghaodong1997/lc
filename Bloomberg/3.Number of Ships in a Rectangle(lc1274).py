# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
class Sea(object):
   def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
       # API
       return True
class Point(object):
	def __init__(self, x: int, y: int):
		self.x = x
		self.y = y

# Divide and Conquer
class Solution(object):
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        
        def helper(topRight, bottomLeft):
            x0, y0 = bottomLeft.x, bottomLeft.y
            x, y = topRight.x, topRight.y
            if x0 > x or y0 > y: return 0
            if x == x0 and y == y0:
                return 1 if sea.hasShips(topRight, bottomLeft) else 0

            if not sea.hasShips(topRight, bottomLeft): return 0
            mid_x, mid_y = (x + x0) // 2, (y + y0) // 2

            
            area1 = helper(Point(mid_x, mid_y), bottomLeft)
            area2 = helper(Point(x, mid_y), Point(mid_x + 1, y0))
            area3 = helper(Point(mid_x, y), Point(x0, mid_y + 1))
            area4 = helper(topRight, Point(mid_x + 1, mid_y + 1))
            return area1 + area2 + area3 + area4
        return helper(topRight, bottomLeft)
            