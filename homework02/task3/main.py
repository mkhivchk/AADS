def max_subarray_sum(arr):
    max_ending_here = max_so_far = arr[0]

    for num in arr[1:]:
        max_ending_here = max(num, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far


# Пример использования
array = [1, -3, 4, -2, -1, 6]
max_sum = max_subarray_sum(array)
print("Максимальная сумма подмассива:", max_sum)