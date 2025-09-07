class Solution (object):
    def climbStairs(self, n, d = {}):
        """
        :type n: int
        :rtype: int
        """
        try:
            return d[n]
        except KeyError:
            if n < 0:
                d[n] = 0
                return 0
            elif n == 0:
                d[n] = 1
                return 1
            else:
                d[n] = self.climbStairs(n - 1, d) + self.climbStairs(n - 2, d)
                return d[n]
        
s = Solution()
assert s.climbStairs(2) == 2, "#1"
assert s.climbStairs(3) == 3, "#2"
print(s.climbStairs(38))