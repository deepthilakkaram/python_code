
import sys


def longest_unique_substring_length(s: str) -> int:
    last = {}  # maps character -> last index seen
    maxlen = 0
    start = 0  # start index of current window
    for i, ch in enumerate(s):
        if ch in last and last[ch] >= start:
            start = last[ch] + 1
        last[ch] = i
        maxlen = max(maxlen, i - start + 1)
    return maxlen


def main() -> None:
    data = sys.stdin.read().strip().splitlines()
    if not data:
        return
    s = data[0].strip()
    # Problem guarantees lowercase letters only, but we don't enforce it here.
    print(longest_unique_substring_length(s))


if __name__ == "__main__":
    main()
