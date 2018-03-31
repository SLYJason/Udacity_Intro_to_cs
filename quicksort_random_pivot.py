#!/usr/bin/env python
import random
def sort(A):
    quicksort(A, 0, len(A)-1)
    return A
    
def quicksort(A, start, end):
    if start > end:
        return 
    pivot_index = random.randint(start, end)
    swap(A, start, pivot_index)
    delim = partition(A, start, end)
    quicksort(A, start, delim-1)
    quicksort(A, delim+1, end)

def partition(A, left, right):
    pivot = A[left]
    i = left + 1
    for j in range(left+1, right+1):
        if A[j] < pivot:
            swap(A, i, j)
            i += 1
    swap(A, left, i-1)
    return i-1
 
def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp      
    
A = [3, 4, 2, 5, 3, 8, 1]
B = [-5, 3, -2, 3, 19, 5]
print sort(A)
print sort(B)  