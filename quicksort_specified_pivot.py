#!/usr/bin/env python
def sort(array):
    quicksort(array, 0, len(array)-1)
    return array
    
def quicksort(array, start, end):
    if start >= end:
        return 
    delim = partition(array, start, end)
    quicksort(array, start, delim)
    quicksort(array, delim+1, end)
    
def partition(array, start, end):
    pivot = array[(start+end)/2]
    while start < end:
        while array[start] < pivot:
            start += 1
        while array[end] > pivot:
            end -= 1
        if start <= end:
            swap(array, start, end)
            start += 1
            end -= 1
    return start-1 
        
def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp
    
A = [3, 4, 2, 5, 3, 8, 1]
B = [-5, 3, -2, 3, 19, 5]
print sort(A)
print sort(B)  

#another sol, using more space
def quicksort_another(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    worse = []
    better = []
    for e in arr[1:]:
        if e <= pivot:
            worse.append(e)
        else:
            better.append(e)
    return quicksort_another(worse) + [pivot] + quicksort_another(better)
    
alist = [54,26,93,17,77,31,44,55,20]
print quicksort_another(alist)