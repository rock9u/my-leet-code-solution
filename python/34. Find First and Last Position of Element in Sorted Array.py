class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # search left for the different, right b search fo the 
        
        result=[-1,-1]
        l = 0
        r = len(nums)-1
        
        if l == r == 0:
            if nums[0] == target:
                return [0,0]
            else:
                return [-1, -1]
        
        
        while(l<=r):
            m = l + (r-l)//2

            if nums[m] == target:
                if (m==0 or nums[m-1] != target):
                    result[0] = m
                    break
                else:
                    r = m
            elif l == r :
                break
            elif nums[m] < target:
                l = m+1
            elif nums[m] > target:
                r = m


        if result[0] == -1:
            return result
        l = result[0]
        r = len(nums)-1

        while(l<=r):
            m = l + (r-l)//2

            if nums[m] == target:
                if (m == len(nums)-1 or nums[m+1] != target):
                    result[1] = m
                    break
                else:
                    l = m+1
            elif l == r :
                break           
            elif nums[m] < target:
                l = m+1
            elif nums[m] > target:
                r = m
                

        return result