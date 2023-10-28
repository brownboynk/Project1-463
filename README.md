# Hybrid Algorithms

## Insertion Sort:

### Insertion Sort takes an array and compares the first two elements, seeing which is larger and performing a swap if necessary. Each element is compared to the last until a swap can no longer be performed, meaning the array is sorted and completed.

The best case time complexity is O(N)

The worst case time complexity is O(N^2)

The average case time complexity is O(N^2)


## Quick Sort:

Quick Sort takes an array and partitions the elements in a way that the selected element is considered the pivot. Each element will be compared with the pivot until the elements are sorted, then the pivot is placed in the correct position.

The best case time complexity is 
Ω (N log (N))

The worst case time complexity is O (N2)

The average case time complexity
θ 
( N log (N))

## Hybrid Algorithm:

I am looking to combine these two algorithms and create a more efficient sorting algorithm. Quick Sort’s best average-case performance with Insertion Sort’s efficiency for small datasets optimizes sorting for a variety of input sizes when combined.

The time complexity of the hybrid algorithm is O(N^2)

Each screenshot below is a test with output arrays of numbers 1-1000, 1-10000, and 1-100000
![Screenshot 2023-10-27 215758](https://github.com/brownboynk/Project1-463/assets/78939104/c7c0f1a7-00f1-472a-8e54-72aaa6eec88c)
![Screenshot 2023-10-27 215748](https://github.com/brownboynk/Project1-463/assets/78939104/f671f53e-ed50-4de2-af57-45a4bc16ec71)
![Screenshot 2023-10-27 215729](https://github.com/brownboynk/Project1-463/assets/78939104/29cc1a35-64d0-4f97-8c44-2c593e153496)
![Screenshot 2023-10-27 215717](https://github.com/brownboynk/Project1-463/assets/78939104/73ce6caf-8c3c-40df-ad92-28246b94c7c3)
![Screenshot 2023-10-27 215707](https://github.com/brownboynk/Project1-463/assets/78939104/a0706aa1-b22c-413b-9d6f-b65e344561f7)
![Screenshot 2023-10-27 215635](https://github.com/brownboynk/Project1-463/assets/78939104/b544486d-5893-4bca-a708-c72deb32f239)
![Screenshot 2023-10-27 215622](https://github.com/brownboynk/Project1-463/assets/78939104/9657c39d-9c02-4cfd-a1f6-32bfd4591c0c)
![Screenshot 2023-10-27 215611](https://github.com/brownboynk/Project1-463/assets/78939104/14b369f6-8fb6-4b3b-8078-34f7710748c1)
![Screenshot 2023-10-27 215559](https://github.com/brownboynk/Project1-463/assets/78939104/b582a204-3d33-4c1d-a7a2-299270a2ea85)
![Screenshot 2023-10-27 215540](https://github.com/brownboynk/Project1-463/assets/78939104/a60e4d2e-f401-4f5e-87dc-95d970b5c69b)

In conclusion, Quick Sort proves to be the fastest among the other 2 Algorithms, but with the Hybrid Sort, it shows that the sorting method is definitely faster than the 2 individual algorithms.
