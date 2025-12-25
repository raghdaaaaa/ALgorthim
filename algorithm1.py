import time
import sys
# Increase recursion limit because the naive solution uses deep recursive calls for larger inputs
sys.setrecursionlimit(2000)
# ---------------------------------------------------
# Naive Recursive Algorithm for Longest Common Subsequence (LCS)
# Time Complexity: O(2^(m+n))  -> Exponential
# Space Complexity: O(m+n)     -> Recursion stack
# ---------------------------------------------------
def lcs_naive(s1, s2, m, n):
    # Base case: if either string is empty
    if m == 0 or n == 0:
        return 0

    # If last char match, include it in LCS
    if s1[m - 1] == s2[n - 1]:
        return 1 + lcs_naive(s1, s2, m - 1, n - 1)

    # If last char do not match,
    # take the max of the two possibilities
    else:
        return max(
            lcs_naive(s1, s2, m, n - 1),
            lcs_naive(s1, s2, m - 1, n)
        )
# ------------------- User Input -------------------
print("----- LCS Naive Approach -----")
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# ------------------- Time Measurement -------------------
start_time = time.perf_counter()
result = lcs_naive(string1, string2, len(string1), len(string2))
end_time = time.perf_counter()

# ------------------- Output -------------------
print("\nLCS Length:", result)
print(f"Execution Time: {(end_time - start_time) * 1000:.6f} ms")



