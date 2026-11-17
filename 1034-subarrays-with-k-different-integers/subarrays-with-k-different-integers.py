class Solution:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:

        def atMost(K):
            if K < 0:
                return 0

            left = 0
            count = 0
            freq = {}

            for right in range(len(nums)):
                freq[nums[right]] = freq.get(nums[right], 0) + 1

                while len(freq) > K:
                    freq[nums[left]] -= 1

                    if freq[nums[left]] == 0:
                        del freq[nums[left]]

                    left += 1

                count += right - left + 1

            return count

        return atMost(k) - atMost(k - 1)