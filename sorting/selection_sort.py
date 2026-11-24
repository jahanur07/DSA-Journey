def selection_sort(numbers):
    n = len(numbers)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            if numbers[j] < numbers[min_index]:
                min_index = j

        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

    return numbers


numbers = [64, 25, 12, 22, 11]
print(selection_sort(numbers))
