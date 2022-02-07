from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        counted = Counter(nums)
        result = []
        for letter,count in counted.items():
            if count == 1:
                result.append(letter)
        return result