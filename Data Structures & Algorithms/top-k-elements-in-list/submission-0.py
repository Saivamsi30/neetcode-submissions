class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for i in nums:
            if i not in hashmap:
                hashmap[i] = 0
            hashmap[i] += 1

        heap = []
        for key,value in hashmap.items():
            heapq.heappush(heap,(value,key))

            if len(heap) > k:
                heapq.heappop(heap)

        return [key for value,key in heap]

        