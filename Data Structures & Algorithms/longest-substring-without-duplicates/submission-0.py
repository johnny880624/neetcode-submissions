class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        count = 0
        duplicate_check = set()
        final = 0

        for i in range(len(s)):
            if s[i] not in duplicate_check:
                duplicate_check.add(s[i])
                r += 1
                count += 1
                if final < count:
                    final = count
            else:
                while s[l] != s[i]:
                    duplicate_check.remove(s[l])
                    l +=1
                    count -= 1
                l += 1
        return final
            

                
            
            
