class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        rsp = defaultdict(int)
        for num in nums:
            rsp[num] +=1
        
        arr = []
        for num, cnt in rsp.items():
            arr.append([cnt,num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res