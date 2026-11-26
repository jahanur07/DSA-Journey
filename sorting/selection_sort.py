# def selection_sort(numbers):
#     n = len(numbers)

#     for i in range(n - 1):
#         min_index = i

#         for j in range(i + 1, n):
#             if numbers[j] < numbers[min_index]:
#                 min_index = j

#         numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

#     return numbers


# numbers = [64, 25, 12, 22, 11]
# print(selection_sort(numbers))

#t --> O(n2)
#s --> O(1)
def selection_sort(num):
  n=len(num)
  for i in range(0,n):
    min_ind=i
    for j in range(i+1,n):
      if num[j] < num[min_ind]:
        min_ind=j
    num[i],num[min_ind]=num[min_ind],num[i]
  return num
  


num = [3,4,2,4,0,6,7,3]

print(selection_sort(num))