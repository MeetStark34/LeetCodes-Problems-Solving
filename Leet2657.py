#2657. Find the Prefix Common Array of Two Arrays
class Solution:
    def findThePrefixCommonArray(self, A, B):
        n = len(A)
        C = [0] * n
        seen_in_A = set()
        seen_in_B = set()
        common_count = 0

        for i in range(n):
            seen_in_A.add(A[i])
            seen_in_B.add(B[i])

            # Increment common count if the current element of A is also in B
            if A[i] in seen_in_B:
                common_count += 1
            # Increment common count if the current element of B is also in A
            if B[i] in seen_in_A and B[i] != A[i]:  # Avoid double counting
                common_count += 1

            C[i] = common_count

        return C

# Example driver code
if __name__ == "__main__":
    A1 = [1, 3, 2, 4]
    B1 = [3, 1, 2, 4]
    
    solution = Solution()
    print(solution.findThePrefixCommonArray(A1, B1))  # Output: [0, 2, 3, 4]

    A2 = [2, 3, 1]
    B2 = [3, 1, 2]
    print(solution.findThePrefixCommonArray(A2, B2))  # Output: [0, 1, 3]
