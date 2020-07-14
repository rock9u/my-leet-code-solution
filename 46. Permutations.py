class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.list = []
        memo = []
        self.gen(nums,memo)
        print(self.list)
        return self.list
    
    def gen(self,nums,memo):
        numLen = len(nums);
        if numLen == 0:
            self.list.append(memo)
            return
        for i in range(numLen):
            n = nums[i]
            self.gen([*nums[:i],*nums[i+1:]],[*memo,n])