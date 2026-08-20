class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:

        reserved = {}

        # Store reserved seats for each row
        for row, seat in reservedSeats:
            if row not in reserved:
                reserved[row] = set()

            reserved[row].add(seat)

        # Every row initially contributes 2 groups
        result = 2 * n

        # Recalculate only rows containing reservations
        for row in reserved:
            result -= 2

            seats = reserved[row]

            left_available = not any(seat in seats for seat in [2, 3, 4, 5])

            middle_available = not any(seat in seats for seat in [4, 5, 6, 7])

            right_available = not any(seat in seats for seat in [6, 7, 8, 9])

            if left_available and right_available:
                result += 2
            elif left_available or middle_available or right_available:
                result += 1

        return result
        