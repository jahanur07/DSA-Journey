def bubble_sort(numbers):
    n = len(numbers)

    for i in range(n - 1):
        swapped = False

        for j in range(n - 1 - i):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                swapped = True

        # Stop early when the list is already sorted.
        if not swapped:
            break

    return numbers


numbers = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(numbers))
