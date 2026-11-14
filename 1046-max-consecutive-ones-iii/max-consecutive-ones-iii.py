class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left = 0
        zeroes = 0
        max_len = 0
        for right in range(len(nums)):
            if nums[right]==0:
                zeroes +=1
            while zeroes > k:
                if nums[left] == 0:
                    zeroes -=1
                left +=1
            
            length = right - left +1
            max_len=max(max_len,length)
        
        return max_len