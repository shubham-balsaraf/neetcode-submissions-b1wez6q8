class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        for x in s:
            if x not in d:
                d[x] =1
            else:
                d[x]+=1
        for y in t:
            if y not in d:
                return False
            else:
                d[y]-=1
        for k, v in d.items():
            if v>=1:
                return False
        return True
        

        