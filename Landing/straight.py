class Solution:
   def solve(self, coordinates):
      (x0, y0), (x1, y1) = coordinates[0], coordinates[1]
      for i in range(2, len(coordinates)):
         x, y = coordinates[i]
         if (x0 - x1) * (y1 - y) != (x1 - x) * (y0 - y1):
            return False
      return True
ob = Solution()
coordinates = [[50, 80],[10, 30]]
print(ob.solve(coordinates))