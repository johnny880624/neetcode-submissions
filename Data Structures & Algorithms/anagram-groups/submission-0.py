class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for i in range(len(strs)):
            sorted_s = sorted(strs[i])
            key = "".join(sorted_s)
            result[key].append(strs[i])
        
        return list(result.values())