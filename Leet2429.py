#2429. Minimize XOR
class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        # Count the number of set bits in num2
        num2_set_bits = bin(num2).count('1')

        # Start with num1 and modify it to have the same number of set bits as num2
        result = 0

        # Set bits in num1 from the most significant bit to the least
        for i in range(31, -1, -1):
            if num1 & (1 << i):  # Check if the bit is set in num1
                if num2_set_bits > 0:  # If we still need set bits
                    result |= (1 << i)  # Set this bit in the result
                    num2_set_bits -= 1  # Decrease the remaining set bits count

        # If we still need to add more set bits
        for i in range(32):
            if num2_set_bits == 0:  # Stop if we've added enough set bits
                break
            if not (result & (1 << i)):  # If this bit is not set in the result
                result |= (1 << i)  # Set this bit
                num2_set_bits -= 1  # Decrease the remaining set bits count

        return result

# Example usage for testing
solution = Solution()
print(solution.minimizeXor(3, 5))  # Output: 3
print(solution.minimizeXor(1, 12))  # Output: 3