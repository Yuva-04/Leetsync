class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def Allocation_possible(barrier):
            allocated_student = 1
            pages = 0

            for i in range(len(nums)):

                if nums[i] > barrier:
                    return False

                elif pages + nums[i] > barrier:
                    allocated_student += 1
                    pages = nums[i]

                else:
                    pages += nums[i]

            if allocated_student > k:
                return False
            else:
                return True

        low = max(nums)
        high = sum(nums)
        res = -1

        while low <= high:
            mid = (low + high) // 2

            if Allocation_possible(mid):
                res = mid
                high = mid - 1
            else:
                low = mid + 1

        return res