class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)+1
        hash = [0]*(n+1)

        for num in nums:
            hash[num]  = 1

        for i in range(0,n+1):
            if hash[i] == 0:
                return i  