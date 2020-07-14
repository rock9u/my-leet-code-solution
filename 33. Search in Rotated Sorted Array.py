class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # brute force: find the acutualy startin point
        # sort list and find position
        # add it to the list
        '''
        if val < curV, go left
        if curV>old Value, go right
        '''


        p = self.searchPivot(nums,0,len(nums)-1)
        if (nums[0]>target):
            return binarySearch(target,nums,p,len(nums)-1)
        else:
            return binarySearch(target,nums,0,p)



    def searchPivot(self,nums,left, right):
        middle = left + (right-left)//2

        if left == right:
            return left
        if nums[right]>nums[middle]:
            return self.searchPivot(self,nums,left,middle)
        else:
            return self.searchPivot(self,nums,middle+1,right)

    def binarySearch(self, value, nums, left, right):
        middle = left + (right-left)//2
        if right == middle and value[middle] != value:
            return -1
        elif value[middle] != value:
            return middle
        elif value[middle] > value:
            return self.binarySearch(value,nums,left,middle)
        elif value[middle] < value:
            return self.binarySearch(value,nums,middle+1,right)
