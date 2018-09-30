class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        counter=0
        for letter in S:
            if letter in J:
                counter+=1
        return counter


#a=Solution()
J="z"
S="ZZZ"
print(Solution().numJewelsInStones(J,S))