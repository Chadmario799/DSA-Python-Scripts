def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

array = list(map(int, input("Enter a list of elements : ").split(" ")))
print("The unsorted array is : ", array)
selection_sort(array)
print("The sorted array is : ", array)