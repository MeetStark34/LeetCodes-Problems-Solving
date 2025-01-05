#2381. Shifting Letters II

class Solution:
    def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
        n = len(s)
        shift_accum = [0] * (n + 1)  # Difference array
        
        # Apply the shifts to the difference array
        for start, end, direction in shifts:
            delta = 1 if direction == 1 else -1
            shift_accum[start] += delta
            shift_accum[end + 1] -= delta

        # Compute the prefix sum of the difference array
        cumulative_shift = 0
        result = []
        for i in range(n):
            cumulative_shift += shift_accum[i]
            new_char = chr((ord(s[i]) - ord('a') + cumulative_shift) % 26 + ord('a'))
            result.append(new_char)

        return ''.join(result)

solution = Solution()

# Example 1
s1 = "abc"
shifts1 = [[0, 1, 0], [1, 2, 1], [0, 2, 1]]
print(solution.shiftingLetters(s1, shifts1))  # Output: "ace"

# Example 2
s2 = "dztz"
shifts2 = [[0, 0, 0], [1, 1, 1]]
print(solution.shiftingLetters(s2, shifts2))  # Output: "catz"
