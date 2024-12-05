def bubbleSort(arr):
    n = len(arr)  # Length of the array
    for i in range(n):  # Outer loop for n iterations
        for j in range(n - i - 1):  # Inner loop to compare adjacent elements
            if arr[j] > arr[j + 1]:  # If the current element is greater than the next element
                # Swap the elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
