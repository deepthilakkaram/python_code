# python_code
# problem 2
# solution.py
import sys

def max_k_sum(nums, k):
    n = len(nums)
    if k == 0:
        return 0
    # initial window
    curr = sum(nums[:k])
    best = curr
    for i in range(k, n):
        curr += nums[i] - nums[i - k]
        if curr > best:
            best = curr
    return best

def main():
    tokens = sys.stdin.read().strip().split()
    if not tokens:
        return
    vals = list(map(int, tokens))
    n = vals[0]
    if n == 0:
        print(0)
        return
    # next n integers are the readings
    if len(vals) < 1 + n + 1:
        # not enough tokens for readings + k
        raise ValueError("Input does not contain the expected number of integers.")
    readings = vals[1:1 + n]
    k = vals[1 + n]
    print(max_k_sum(readings, k))

if __name__ == "__main__":
    main()
