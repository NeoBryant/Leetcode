import math
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        isPositive=1 if x>=0 else -1
        num = abs(x)
        
        res=0
        while num!=0:
            res *= 10
            res += num%10
            num //= 10
        
        if res<(-1*(2**31)) or res>(2**31-1):
            return 0

        res*=isPositive
        return res

b=Solution()
a=1534236469
print(b.reverse(a))