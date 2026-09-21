class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        r = 0
        re = ""
        d = {}
        

        for char in t:
            if char not in d:
                d[char] = 1
            else:
                d[char] += 1


        for r in range(len(s)):

            # re = re + s[r]
            if s[r] in d:    
                d[s[r]] -= 1
                    
            while max(d.values()) < 1:
                if re == "" or (r-l+1) <= len(re):
                    re = s[l:r+1]
                if s[l] in d:
                    d[s[l]] += 1
                l += 1
            
        return re

            



