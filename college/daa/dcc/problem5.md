```text

"""
Consider an array of A[1, 2, 3, ..., n] be an array of n distinct num-
bers. If i < j and A[i] > A[j], then we call the the pair (i, j) as
an inversion of A. For example, the five inversions in the array
A :< 2, 3, 8, 6, 1 > are (1, 5), (2, 5), (3, 4), (3, 5), (4, 5). Given an
array of numbers, design the pseudocode and the corresponding
code that follows ‘Divide-Conquer-Combine’ strategy for com-
puting the number of inversions in the array and analyse the
same.
    """
```

```python


import random


def merge(arr, lo, mid, hi):

    inversion = 0

    left_ptr = lo
    right_ptr = mid + 1

    temp = []

    while left_ptr <= mid and right_ptr <= hi:
        if arr[left_ptr] <= arr[right_ptr]:
            temp.append(arr[left_ptr])
            left_ptr += 1
        else:
            inversion = inversion + (right_ptr - left_ptr + 1)
            temp.append(arr[right_ptr])
            right_ptr += 1

    while left_ptr <= mid:

        temp.append(arr[left_ptr])

        left_ptr += 1

    while right_ptr <= hi:
        temp.append(arr[right_ptr])
        right_ptr += 1

    for i in range(len(temp)):
        arr[lo + i] = temp[i]

    return inversion


def count_inversion(arr, lo, hi):

    inversion = 0

    if lo < hi:

        mid = (hi + lo) // 2

        inversion = inversion + count_inversion(arr, lo, mid)

        inversion = inversion + count_inversion(arr, mid + 1, hi)

        return merge(arr, lo, mid, hi)

    return inversion


def main():

    arr = list()
    for _ in range(5):
        arr.append(random.randrange(-10, 10))

    print(f"The original arr is {arr}")
    count = count_inversion(arr, 0, len(arr) - 1)
    print(f"The number of inversion pair is {count}")


if __name__ == "__main__":
    main()
```
