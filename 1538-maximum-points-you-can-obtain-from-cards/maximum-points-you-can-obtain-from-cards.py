class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        n=len(cardPoints)
        window_size=n-k
        if window_size==0:
            return sum(cardPoints)

        window_sum= sum(cardPoints[:window_size])
        min_sum=window_sum

        for i in range(window_size,n):
            window_sum += cardPoints[i] - cardPoints[i-window_size]
            min_sum = min(min_sum,window_sum)

        return sum(cardPoints) - min_sum
        