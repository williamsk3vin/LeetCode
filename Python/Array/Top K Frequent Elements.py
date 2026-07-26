class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            counter[num] = counter.get(num,0) + 1
        freq = list(counter.items())
        result = sorted(freq, key=lambda item: item[1], reverse=True)
        first_elements = [item[0] for item in result[:k]]
        return first_elements


# Bucket Sort
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        answer = []
        for num in nums:
            counter[num] = counter.get(num,0) + 1
        buckets = [[] for _ in range(len(nums) + 1)]
        for number, frequency in counter.items():
              buckets[frequency].append(number)
        for frequency in range(len(buckets) - 1, 0, -1):
            for number in buckets[frequency]:
                answer.append(number)
                if len(answer) == k:
                    return answer
