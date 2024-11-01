# Recurssive Solution

```python

def subset_sum_recussive(arr, lst_idx, target):

    # base cases
    if target == 0:
        return True

    # the case when n == 0 and target == 0 is already covered, so this case happen when arr = [] and target != 0.
    if lst_idx < 0:
        return False

    if arr[lst_idx] <= target:
        return subset_sum_recussive(
            arr, lst_idx - 1, target - arr[lst_idx]
        ) or subset_sum_recussive(arr, lst_idx - 1, target)

    else:
        return subset_sum_recussive(arr, lst_idx - 1, target)


def main():
    nums = [3, 34, 4, 12, 5, 2]
    target = 9
    result = subset_sum_recussive(nums, len(nums) - 1, target)
    print(f"{result}")


if __name__ == "__main__":
    main()
```

![[subset-sum-recussive.pdf]]

# Memoized Solution

```python

![[subset-sum-recussive.pdf]]idx, target, dp):

    # base cases
    if target == 0:
        return True

    # the case when n == 0 and target == 0 is already covered, so this case happen when arr = [] and target != 0.
    if lst_idx < 0:
        return False

    # memo code
    if dp[lst_idx][target] != -1:
        return dp[lst_idx][target]

    if arr[lst_idx] <= target:
        dp[lst_idx][target] = subset_sum_memo(
            arr, lst_idx - 1, target - arr[lst_idx], dp
        ) or subset_sum_memo(arr, lst_idx - 1, target, dp)

    else:
        dp[lst_idx][target] = subset_sum_memo(arr, lst_idx - 1, target, dp)

    return dp[lst_idx][target]


def main():
    nums = [3, 34, -4, 12, 5, 2]
    target = -1
    dp = [[-1 for _ in range(target + 1)] for _ in range(len(nums))]
    result = subset_sum_memo(nums, len(nums) - 1, target, dp)
    print(f"{result}")


if __name__ == "__main__":
    main()
```

# Bottom Up Approach

```python
"""
    given a array, we have to find is it possible to make a subset with sum equal to the given sum..

"""


def subset_sum(arr, target):

    n = len(arr)
    dp = [
        [False] * (target + 1) for _ in range(n + 1)
    ]  # meaning for each of the iteration generate [False] * (target + 1)

    for i in range(n + 1):
        dp[i][0] = True

    for i in range(1, n + 1):
        for j in range(1, target + 1):
            if arr[i - 1] <= j:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][target]


def main():
    nums = [3, 34, 4, 12, 5, 2]
    target = 9
    result = subset_sum(nums, target)
    print(f"{result}")


if __name__ == "__main__":
    main()
```

![[2-subset sum problem.pdf]]
