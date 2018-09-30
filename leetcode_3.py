class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s=="":
            return 0
        longest=1
        for i in range(len(s)-1):
            substr=s[i]
            for j in range(i+1, len(s)):
                if s[j] in substr:
                    break
                else:
                    substr+=s[j]
            if len(substr)>longest:
                longest=len(substr)
        return longest

a=Solution()

s=""
b=a.lengthOfLongestSubstring(s)
print(b)
