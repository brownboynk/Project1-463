hybridSort(arr, low, high, threshold):
    if low < high:
        if high - low < threshold:
            # Switch to Insertion Sort for small sub-arrays
            insertionSort(arr[low:high+1])
        else:
            # Continue with Quick Sort for larger sub-arrays
            pivot = partition(arr, low, high)
            hybridSort(arr, low, pivot - 1, threshold)
            hybridSort(arr, pivot + 1, high, threshold)

insertionSort(arr):
    # Insertion Sort implementation

partition(arr, low, high):
    # Quick Sort partitioning logic

# Initial call to hybrid sort
hybridSort(arr, 0, len(arr) - 1, threshold)
