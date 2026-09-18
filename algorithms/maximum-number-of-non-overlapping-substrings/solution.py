class Solution(object):
    def maxNumOfSubstrings(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        

        n = len(s)

        # first[i] = first occurrence of character i
        # last[i] = last occurrence of character i
        first = [-1] * 26
        last = [-1] * 26

        # Find first and last occurrence
        for i in range(n):
            c = ord(s[i]) - ord('a')

            if first[c] == -1:
                first[c] = i

            last[c] = i

        # Store valid intervals
        intervals = []

        # Try every character
        for c in range(26):

            if first[c] == -1:
                continue

            left = first[c]
            right = last[c]

            valid = True

            # Expand the interval
            i = left

            while i <= right:

                current = ord(s[i]) - ord('a')

                # Character occurs before our left boundary
                if first[current] < left:
                    valid = False
                    break

                # Character occurs after our current right boundary
                if last[current] > right:
                    right = last[current]

                i += 1

            if valid:
                intervals.append((left, right))

        # Sort by ending position
        intervals.sort(key=lambda x: x[1])

        answer = []

        previous_end = -1

        # Select non-overlapping intervals
        for left, right in intervals:

            if left > previous_end:

                answer.append(s[left:right + 1])

                previous_end = right

        return answer
        