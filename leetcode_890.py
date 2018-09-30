class Solution:
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        def match(word):
            print(word)
            m1, m2 = {}, {}
            for w, p in list(zip(word, pattern)):
                if w not in m1:
                    m1[w] = p
                if p not in m2:
                    m2[p] = w
                if (m1[w], m2[p]) != (p, w):
                    return False
            return True

        return list(filter(match, words))
'''
class Solution:
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        res=[]
        for word in words:
            m1, m2 = {}, {}
            isMatch=True
            for i in range(len(pattern)):
                w = word[i]
                p = pattern[i]
                if w not in m1: 
                    m1[w] = p
                if p not in m2: 
                    m2[p] = w
                if (m1[w], m2[p]) != (p, w):
                    isMatch=False
                    break
            if isMatch:
                res.append(word)

        return res
'''

w=["abc","deq","mee","aqq","dkd","ccc"]
p="abb"

print(Solution().findAndReplacePattern(w,p))