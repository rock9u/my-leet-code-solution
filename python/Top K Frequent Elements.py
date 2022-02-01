import heapq

class Node():
    def __init__(self, num):
        self.num = num
        self.count = 0

    def __lt__(self, other):
        return self.num > other.num
        
    def advance(self):
        self.count=+1
    

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # literate though and create a hash of unique elements
        # put all summed up into a max heap and pop k times the 
        
        maps = dict()
        heapList = []
        for num in nums:
            counts[str(num)] = maps[str(num)].advance if maps[str(num)] else Node(str(num))

        for key,value in maps.iteritems():
            heapList.append(value)
        
        maxHeap = heapq._heapify_max(heapList)
        result = []
        for i in range(k):
            result.append(heapq._heappop_max(maxHeap))

        return result


