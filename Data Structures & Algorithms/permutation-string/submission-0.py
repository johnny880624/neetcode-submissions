class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = 0 
        d = defaultdict(int)

        for i in range(len(s1)):
            d[s1[i]] +=1 
        
        for r in range(len(s2)):
            d[s2[r]] -= 1

            if (r-l+1) > len(s1):
                d[s2[l]] += 1
                l += 1
            
            if (r-l+1) == len(s1) and all(v == 0 for v in d.values()):
                return True
        
        return False
            
