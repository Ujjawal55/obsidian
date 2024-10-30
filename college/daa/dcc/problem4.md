##### Problem

```text
n a ‘Maximum subarray Problem’, you are given an array A of
integers and the task is to find the nonnegative contiguous subar-
ray of A such that the sum of the values in the subarray is max-
imum. Here, the subarray returned by the code is ‘contiguous’
(cells of the subarray should be adjacent). Based on this, we pro-
pose a new problem : ‘Maximum non-contiguous subarray Prob-
lem’ where in the array of non-negative integers is taken as an
input and the task is to return the non-negative non-contiguous
subarraay whose sum is maximum and the subarray need not be
contiguous
```

#### Ultra Aaam Zindagi

```python

def recussive(arr, lo, hi):
    # base case
    if lo == hi:
        return arr[lo], [arr[lo]]

    mid = (lo + hi) // 2

    left_sum, left_number = recussive(arr, lo, mid)

    right_sum, right_number = recussive(arr, mid + 1, hi)

    combined_sum = left_sum + right_sum
    combined_number = left_number + right_number

    if left_sum > combined_sum and left_sum > right_sum:
        return left_sum, left_number
    elif right_sum > combined_sum and right_sum > left_sum:
        return right_sum, right_number
    else:
        return combined_sum, combined_number


def main():
    arr = list()

    for _ in range(10):
        arr.append(random.randrange(-10, 10))


    max_sum, lst = recussive(arr, 0, len(arr) - 1)
    print(f"The maximum sum is {max_sum}")
    print(f"The elements are {lst}")


if __name__ == "__main__":
    main()
```

![[recurssive-maximum-sum-elements.pdf]]

#### Aaam Zindagi

```python

import random

def max_sum_elements(arr):

    lst = [arr[0]]

    curr_max = arr[0]

    for i in range(1, len(arr)):
        if (curr_max + arr[i]) > curr_max:
            lst.append(arr[i])
            curr_max = curr_max + arr[i]

        else:
            if curr_max < arr[i]:
                lst.clear()
                lst.append(arr[i])
                curr_max = arr[i]

    return lst


def main():
    arr = list()

    for _ in range(10):
        arr.append(random.randrange(-10, 10))

    lst = max_sum_elements(arr)

    print(f"The original array  is {arr}")
    print(f"The maximum sum is {sum(lst)}")
    print(f"The elements are {lst}")

if __name__ == "__main__":
    main()
```

![[maximum-sum-elements.pdf]]

#### Mentos Zindagi

```python

import random


def simple_method(arr):
    lst = []

    for num in arr:
        if num >= 0:
            lst.append(num)

    if lst.count == 0:
        lst.append(max(arr))

    return lst

def main():
    arr = list()

    for _ in range(10):
        arr.append(random.randrange(-10, 10))

    lst = simple_method(arr)
    print(f"The maximum sum is {sum(lst)}")
    print(f"The elements are {lst}")


if __name__ == "__main__":
    main()

```
