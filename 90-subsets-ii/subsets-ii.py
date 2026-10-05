class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        result = []

        nums.sort()

        def backtrack(index, current):
            result.append(current.copy())

            for i in range(index, len(nums)):

                # Skip duplicate at the same level
                if i > index and nums[i] == nums[i - 1]:
                    continue

                current.append(nums[i])

                backtrack(i + 1, current)

                current.pop()

        backtrack(0, [])

        return result

        