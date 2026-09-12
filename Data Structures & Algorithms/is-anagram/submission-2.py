class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        dict_s = {}
        for a in s:
            if a not in dict_s:
                dict_s[a] = 1;
            else:
                dict_s[a] += 1;
        
        for a in t:
            if a not in dict_s:
                return False
            else:
                dict_s[a] -= 1;
                if dict_s[a] < 0:
                    return False
        return True

