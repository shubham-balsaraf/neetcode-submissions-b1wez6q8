class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        if len(s) != len(t):
            return False
        for x in s:
            if x not in d:
                d[x] =1
            else:
                d[x] +=1

        for x in t:
            if x not in d:
                return False
            else:
                d[x] -=1
        
        for key, value in d.items():
            if value < 0:
                return False

        return True

        