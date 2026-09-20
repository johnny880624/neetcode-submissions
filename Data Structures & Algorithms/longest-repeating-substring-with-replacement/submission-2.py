class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        d = defaultdict(int)
        re = 0

        for r in range(len(s)):
            d[s[r]] += 1
            while (r-l+1) - max(d.values()) > k:
                d[s[l]] -= 1
                l+=1
        
            re = max(re, r-l+1)
        
        return re 
