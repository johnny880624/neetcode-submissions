class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        rsp = defaultdict(int)
        for num in nums:
            rsp[num] += 1
        
        bucket = [[]for i in range(len(nums)+1)]
        for num, cnt in rsp.items():
            bucket[cnt].append(num)

        result = []
        for i in range(len(nums), 0, -1):
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result
        
        return result
            
