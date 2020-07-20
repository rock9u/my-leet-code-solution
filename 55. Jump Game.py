class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''
        first scan if there is elemnt able to reach to the end of the index

        for all item
            if item.value can reach end
                if index is 0:
                    return true:
                else:
                    return canJump([0:thisIndex])
            else return false
        '''
        if len(nums) == 1:
            return True

        return self.backtrack(nums)

    def backtrack(self,nums):
        jumpable = None
        zeroIndex = None
        
        for i in range(len(nums)-1):
            if (nums[i] + i) >= (len(nums)-1):
                jumpable = min(i,jumpable) if jumpable != None else i
            if nums[i] == 0:
                zeroIndex = max(zeroIndex,i) if zeroIndex != None else i

        if jumpable == None:
            return False

        if jumpable == 0:
            return True
        else:
            if zeroIndex == None :
                return True
            else:
                jumpIndex = min(zeroIndex+2,jumpable)
                return self.backtrack(nums[0:jumpIndex+1])
        