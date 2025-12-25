import time
# Super Optimized Dynamic Programming for LCS
# Time Complexity: O(m × n)
# Space Complexity: O(2 × n)
# ---------------------------------------------------
def lcs_super_optimized(s1, s2):
    m, n = len(s1), len(s2)

    # Create two rows for DP (current and previous)
    dp = [[0] * (n + 1) for _ in range(2)]

    for i in range(1, m + 1):
        curr = i % 2       # current row
        prev = 1 - curr    # previous row
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                # Characters match, extend LCS
                dp[curr][j] = 1 + dp[prev][j - 1]
            else:
                # Characters don't match, take max from left or top
                dp[curr][j] = max(dp[prev][j], dp[curr][j - 1])
                
    return dp[m % 2][n]

# ------------------- User Input -------------------
print("----- LCS Super Optimized DP -----")
string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

# ------------------- Time Measurement -------------------
start_time = time.perf_counter()
result = lcs_super_optimized(string1, string2)
end_time = time.perf_counter()

# ------------------- Output -------------------
print("-" * 40)
print("LCS Length:", result)
print(f"Execution Time: {(end_time - start_time) * 1000:.6f} ms")
print("-" * 40)




