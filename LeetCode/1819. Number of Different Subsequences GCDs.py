def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a%b)
class Solution(object):
    

    def countDifferentSubsequenceGCDs(self, nums):
        biggest = max(nums)+1
        dp = [0]*biggest
        ans = 0
        for x in nums:
            dp[x] = True
        for j in range(1,biggest):
            g =0
            for x in range(j,biggest,j):
                if dp[x]:
                    g = gcd(g,x)
                    if g == j:
                        break
            ans  += (g==j)

        return ans
    
