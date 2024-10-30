```python
def maxSubArray(nums):
    # Initialize variables to track maximum sum and current sum
    max_sum = current_sum = nums[0]

    # Start from the second element
    for num in nums[1:]:
        # Either extend previous subarray or start new subarray
        current_sum = max(num, current_sum + num)
        # Update maximum sum if current sum is greater
        max_sum = max(max_sum, current_sum)

    return max_sum
```

![[kadane-explanation.pdf]]