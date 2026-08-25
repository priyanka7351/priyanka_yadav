class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
    
        n = len(stones)

        # Convert stones into prefix sums
        for i in range(1, n):
            stones[i] += stones[i - 1]

        # Start from the total sum
        ans = stones[-1]

        # Calculate from right to left
        for i in range(n - 2, 0, -1):
            ans = max(ans, stones[i] - ans)

        return ans
        