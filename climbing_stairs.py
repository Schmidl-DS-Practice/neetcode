# bottom up dynamic programming approach
class Solution:
    def climbing_stairs(self, n:int ) -> int:
        one, two = 1, 1

        for i in range(n - 1):
            one, two = one + two, one

        return one

n = 8

s = Solution()
print(s.climbing_stairs(n))