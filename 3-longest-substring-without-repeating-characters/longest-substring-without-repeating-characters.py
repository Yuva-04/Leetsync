class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        hash_table = [-1] * 256

        n = len(s)
        l = 0
        r = 0
        max_len = 0

        while r < n:

            if hash_table[ord(s[r])] != -1:
                if hash_table[ord(s[r])] >= l:
                    l = hash_table[ord(s[r])] + 1

            length = r - l + 1
            max_len = max(length, max_len)

            hash_table[ord(s[r])] = r
            r += 1

        return max_len


# Create object and call method
obj = Solution()
print(obj.lengthOfLongestSubstring("abcabcbb"))