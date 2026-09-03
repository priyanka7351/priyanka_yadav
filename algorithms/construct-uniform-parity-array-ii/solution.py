class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        

        min_odd = float('inf')
        min_even = float('inf')

        for x in nums1:
            if x % 2 == 0:
                min_even = min(min_even, x)
            else:
                min_odd = min(min_odd, x)

        # All numbers are even or all numbers are odd
        if min_even == float('inf') or min_odd == float('inf'):
            return True

        # To make every number odd, every even number
        # needs a smaller odd number
        return min_odd < min_even
    
        