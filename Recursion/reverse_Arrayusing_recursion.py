def reverse_recursion(nums, left, right):
    if left >= right:
        return

    nums[left], nums[right] = nums[right], nums[left]
    reverse_recursion(nums, left + 1, right - 1)


numbers = [2, 3, 1, 3, 4, 2, 1]
reverse_recursion(numbers, 2, len(numbers) - 2)
print(numbers)
