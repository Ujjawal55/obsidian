#### Problem

```text
find the maximum sum subarray...
```

```python
import random


def find_cross_sum(arr, lo, mid, hi):

    left_max = float("-Inf")

    left_sum = 0
    left_idx = 0

    for i in range(mid, lo - 1, -1):
        left_sum += arr[i]
        if left_sum > left_max:
            left_max = left_sum
            left_idx = i

    right_max = float("-Inf")
    right_sum = 0
    right_idx = 0

    for i in range(mid + 1, hi + 1):
        right_sum += arr[i]
        if right_sum > right_max:
            right_max = right_sum
            right_idx = i

    return left_idx, right_idx, left_max + right_max


def maximum_sum_subarray(arr, lo, hi):

    # base case
    if lo == hi:
        return lo, hi, arr[lo]

    mid = (hi + lo) // 2

    left_low, left_high, left_sum = maximum_sum_subarray(arr, lo, mid)

    right_low, right_high, right_sum = maximum_sum_subarray(arr, mid + 1, hi)

    cross_low, cross_high, cross_sum = find_cross_sum(arr, lo, mid, hi)

    if left_sum > right_sum and left_sum > cross_sum:
        return left_low, left_high, left_sum
    elif right_sum > left_sum and right_sum > cross_sum:
        return right_low, right_high, right_sum
    else:
        return cross_low, cross_high, cross_sum


def main():

    arr = list()
    for _ in range(10):
        arr.append(random.randrange(-10, 10))

    lidx, ridx, max_sum = maximum_sum_subarray(arr, 0, len(arr) - 1)
    print(f"The original array is {arr}")

    print(f"The maximum sum subarray is {arr[lidx:ridx+1]}")
    print(f"The maximum sum {max_sum}")


if __name__ == "__main__":
    main()
```

![[maximum_sum_subarray.pdf]]

**_ finally after calculating the all the sum there is three possible cases at the end _**

#### three cases:

1. a > b and a > c
2. b > a and b > c
3. c > a and c > b
