class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        
        output = [1] * length

        front = 1
        back = 1

        for i in range(length):
            output[i] = front
            front *= nums[i]

        for i in range(length-1, -1, -1):
            output[i] *= back
            back *= nums[i]
           
            
        return output

        
            

        