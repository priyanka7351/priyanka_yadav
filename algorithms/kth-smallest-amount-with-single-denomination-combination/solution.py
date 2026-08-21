from math import gcd
class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        

        def lcm(a, b):
            return a // gcd(a, b) * b

        n = len(coins)

        # Count how many distinct amounts <= x can be made
        def count(x):
            total = 0

            # Inclusion-Exclusion
            for mask in range(1, 1 << n):
                curr_lcm = 1
                bits = 0
                valid = True

                for i in range(n):
                    if mask & (1 << i):
                        bits += 1
                        curr_lcm = lcm(curr_lcm, coins[i])

                        if curr_lcm > x:
                            valid = False
                            break

                if not valid:
                    continue

                values = x // curr_lcm

                if bits % 2 == 1:
                    total += values
                else:
                    total -= values

            return total

        # Binary Search
        left = 1
        right = min(coins) * k

        while left < right:
            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left
        