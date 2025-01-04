#1930. Unique Length-3 Palindromic Subsequences
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        # Initialize the result set to store unique palindromes
        unique_palindromes = set()
        
        # Create arrays to track seen characters to the left and right
        n = len(s)
        left_seen = [set() for _ in range(n)]
        right_seen = [set() for _ in range(n)]

        # Populate the left_seen array
        for i in range(1, n):
            left_seen[i] = left_seen[i - 1].copy()
            left_seen[i].add(s[i - 1])

        # Populate the right_seen array
        for i in range(n - 2, -1, -1):
            right_seen[i] = right_seen[i + 1].copy()
            right_seen[i].add(s[i + 1])

        # Iterate through the string, using each character as the middle
        for i in range(1, n - 1):
            for char in left_seen[i]:
                if char in right_seen[i]:
                    unique_palindromes.add((char, s[i], char))

        return len(unique_palindromes)

# Example usage
solution = Solution()
print(solution.countPalindromicSubsequence("aabca"))  # Output: 3
print(solution.countPalindromicSubsequence("adc"))    # Output: 0
print(solution.countPalindromicSubsequence("bbcbaba"))  # Output: 4
