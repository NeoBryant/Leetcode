class Solution:
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        Alex = 0
        Lee = 0
        
        isTurnToAlex = 1 #1->Alex, -1->Lee

        front = 0
        end = len(piles)-1

        while front != end:
            #get the more number of piles
            if piles[front] > piles[end]:
                number = piles[front]
                front += 1
            else:
                number = piles[end]
                end -= 1
            # choose the player to get the piles
            if isTurnToAlex==1:
                Alex += number
            else:
                Lee += number

            isTurnToAlex *= -1

        return Alex>Lee

a=[5,3,4,5]
print(Solution().stoneGame(a))