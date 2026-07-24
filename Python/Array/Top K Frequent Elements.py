class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            counter[num] = counter.get(num,0) + 1
        freq = list(counter.items())
        result = sorted(freq, key=lambda item: item[1], reverse=True)
        first_elements = [item[0] for item in result[:k]]
        return first_elements
