import time, sys, random


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def partition(arr, low, high):
	pivot = arr[high]
	i = j = low
	for i in range(low, high):
		if arr[i]<pivot:
			a[i], a[j]= a[j], a[i]
			j+= 1
	a[j], a[high]= a[high], a[j]
	return j

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[random.randint(0, len(arr) - 1)]
    equal = [x for x in arr if x == pivot]
    less = [x for x in arr if x < pivot]
    greater = [x for x in arr if x > pivot]

    return quick_sort(less) + equal + quick_sort(greater)


def hybridsort(arr, low, high):
	while low<high:


		if high-low + 1<10:
			insertion_sort(arr, low, high)
			break

		else:
			pivot = partition(arr, low, high)


			if pivot-low<high-pivot:
				hybridsort(arr, low, pivot-1)
				low = pivot + 1
			else:

				hybridsort(arr, pivot + 1, high)
				high = pivot-1

def hybridsort(arr):
    if len(arr) <= 10:
        return insertion_sort(arr)
    else:
        return quick_sort(arr)

def generatearray(size):
    return [random.randint(1, 1000) for _ in range(size)]

def findtime_memory(sort_func, arr):
    start_time = time.time()
    sort_func(arr)
    end_time = time.time()
    memory_usage = sys.getsizeof(arr)

    return end_time - start_time, memory_usage


a = [ 14, 97, 40, 67, 88, 85, 15, 
	66, 53, 44, 26, 48, 78, 52, 
	45, 70, 90, 18, 34, 80, 23 ]

def test_algorithm(sort_func):

    inputdata = [1, 2, 45, 77, 23, 54 ,68, 9, 33, 6]
    output = [1, 2, 6, 9, 23, 33, 45, 54, 68, 77]
    assert sort_func(inputdata) == output

if __name__ == "__main__":
    array_size = 1000  
    unsorted = generatearray(array_size)


    hybrid_time, hybrid_memory = findtime_memory(insertion_sort, unsorted.copy())

 
    insertion_time, insertion_memory = findtime_memory(quick_sort, unsorted.copy())

 
    quick_time, quick_memory = findtime_memory(hybridsort, unsorted.copy())

    print(f"Insertion Sort - Time: {insertion_time:.6f} seconds, Memory: {insertion_memory} bytes")
    print(f"Quick Sort - Time: {quick_time:.6f} seconds, Memory: {quick_memory} bytes")
    print(f"Hybrid Sort - Time: {hybrid_time:.6f} seconds, Memory: {hybrid_memory} bytes")

    test_algorithm(insertion_sort)
    test_algorithm(quick_sort)
    test_algorithm(hybridsort)

    print("Tests are successful")
