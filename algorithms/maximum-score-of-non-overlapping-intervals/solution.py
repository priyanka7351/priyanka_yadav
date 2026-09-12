class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        from bisect import bisect_left
        
        n = len(intervals)

        # [left, right, weight, original_index]
        arr = []

        for i, (l, r, w) in enumerate(intervals):
            arr.append((l, r, w, i))

        # Sort by right endpoint
        arr.sort(key=lambda x: (x[1], x[3]))

        # Right endpoints
        ends = [x[1] for x in arr]

        # previous[i] = last interval whose right < current left
        prev = [-1] * n

        for i in range(n):
            l = arr[i][0]

            # bisect_left gives first position where end >= l
            prev[i] = bisect_left(ends, l, 0, i) - 1

        # dp[i][k] = (maximum weight, indices)
        dp = [[(0, []) for _ in range(5)] for _ in range(n + 1)]

        def better(a, b):
            # Higher weight is better
            if a[0] != b[0]:
                return a if a[0] > b[0] else b

            # Same weight -> lexicographically smaller indices
            return a if a[1] < b[1] else b

        for i in range(1, n + 1):

            l, r, weight, idx = arr[i - 1]

            for k in range(1, 5):

                # Don't take current interval
                not_take = dp[i - 1][k]

                # Take current interval
                p = prev[i - 1]

                old_score, old_indices = dp[p + 1][k - 1]

                new_indices = old_indices + [idx]
                new_indices.sort()

                take = (
                    old_score + weight,
                    new_indices
                )

                dp[i][k] = better(not_take, take)

        # We can select at most 4 intervals
        ans = dp[n][0]

        for k in range(1, 5):
            ans = better(ans, dp[n][k])

        return ans[1]


        