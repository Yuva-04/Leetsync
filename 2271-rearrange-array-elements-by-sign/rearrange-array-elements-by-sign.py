class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        pos=0
        neg=1
        ans=[0] * len(nums)
        for i in range(len(nums)):
            if nums[i]<0:
                ans[neg]=nums[i]
                neg +=2
            else:
                ans[pos]=nums[i]
                pos +=2

        return ans


                
        