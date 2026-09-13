class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final = defaultdict(list)
        
        for i in range(len(strs)):
            array = [0] * 26
            for s in strs[i]:
                array[ord(s) - ord('a')] +=1
            final[tuple(array)].append(strs[i])
        
        return list(final.values())