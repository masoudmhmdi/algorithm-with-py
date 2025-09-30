def insertion_sort(arr):
    for i in range(1, len(arr)):
        # current card
        key = arr[i]

        # should iterate subArray
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            arr[j] = key
            j -= 1

    print(arr)



insertion_sort([5, 4, 3, 2, 1])