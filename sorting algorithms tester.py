# -*- coding: utf-8 -*-
"""
Created on Sat Apr 12 15:33:08 2025

@author: Muhammad Rizohon
Project info:

A small project to measure the run time of different sorting algorithms
sorting algorithms incldued :
    Bubble sort
    selection sort
    insertion sort
    merge sort
    tim sort
    quick sort
    
datalists to be sorted include:
    already sorted lists
    unsorted lists
    reversely sorted lists
    
    each type will have different sized lists :
        length -> 10, 50, 100, 500, 1000, 2000, 5000, 10000, 15000

1) unsorted lists are created using random library
2) sorted and reversely sorted lists are created using for loop or 
    using built in sort() function for unsorted lists



Project plan:
    1. Creating unsorted lists in the form of matrix using random lib
    2. Creating sorted and reversely sorted lists in the form of matrix
    3. Creating a class with all sorting algorithms
    4. Creating a dictionary for each of the sorting algorithms
    5. PLotting the results


"""
import random
import matplotlib.pyplot as plt
import time

# WARNING!!! In case you want to set higher recursion to work with bigger dataset
#import sys
#sys.setrecursionlimit(7000)


# lengths
# this dataset requires higher recursion limit
#lengths = [10, 50, 100, 500, 1000, 1500, 2000, 3000, 5000]   #WARNING!!!

lengths = [10, 50, 100, 500, 1000, 1500, 1700, 1800, 2000]

# 1, 2 creating unsorted lists, sorted lists, and reversely sorted lists 
unsorted_lists = []
sorted_lists = []
reverse_sorted_lists = []

for length in lengths:
    # unsorted lists
    unsorted_lists.append([random.randint(-50, 50) for i in range(length)])
    
    # sorted lists
    sorted_lists.append([i for i in range(-length // 2, length // 2)])
    
    # reversely sorted lists
    reverse_sorted_lists.append([i for i in range(length // 2, -length // 2, -1)])



# 3 creating a class with different sorting algorithms
class sorting_algorithms:
    
    def bubble_sort(self, dataset):
        n = len(dataset)
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if dataset[j] > dataset[j+1]:
                    dataset[j], dataset[j + 1] = dataset[j + 1], dataset[j]
                    swapped = True
            if not swapped: break
        return dataset
    
    def selection_sort(self, dataset):
        for i in range(0, len(dataset) - 1):
            min_idx = i
            for j in range(i + 1, len(dataset)):
                if dataset[j] < dataset[min_idx]:
                    min_idx = j
            if min_idx != i: 
                dataset[i], dataset[min_idx] = dataset[min_idx], dataset[i]
        return dataset
        
    def insertion_sort(self, data):
        for i in range(1, len(data)):
            key = data[i]
            j = i - 1
            while j >= 0 and data[j] > key:
                data[j + 1] = data[j]  # shift element to the right
                j -= 1
            data[j + 1] = key  # insert key at the correct position
        return data
        
    def merge_sort(self, data):
        # a function to merge two sorted arrays in sorted order
        def merge(list1, list2):
            result = []
            i, j = 0, 0
            
            while i < len(list1) and j < len(list2):
                if list1[i] < list2[j]:
                    result.append(list1[i])
                    i += 1
                    
                else:
                    result.append(list2[j])
                    j += 1
            
            while i < len(list1):
                result.append(list1[i])
                i += 1
            
            while j < len(list2):
                result.append(list2[j])
                j += 1
            return result
        
        if len(data) == 1: return data
        
        listOne = self.merge_sort(data[0 : len(data) // 2])
        listTwo = self.merge_sort(data[len(data) // 2 : len(data)])
        
        return merge(listOne, listTwo)

        
    def tim_sort(self, data):
        min_run = 32
        
        def insertion_sort(data, left, right):
            for i in range(left + 1, right + 1):
                key = data[i]
                j = i - 1
                while j >= left and data[j] > key:
                    data[j + 1] = data[j]
                    j -= 1
                data[j + 1] = key
                
        # Step 2: Merge function
        def merge(left, right):
            result = []
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            result.extend(left[i:])
            result.extend(right[j:])
            return result
        
        
        # Step 3: Apply insertion sort for small chunks
        n = len(data)
        for start in range(0, n, min_run):
            end = min(start + min_run - 1, n - 1)
            insertion_sort(data, start, end)
        
        
        size = min_run
        while size < n:
            for start in range(0, n, size * 2):
                mid = min(n - 1, start + size - 1)
                end = min((start + size * 2 - 1), (n - 1))
                if mid < end:
                    data[start:end + 1] = merge(data[start:mid + 1], data[mid + 1:end + 1])
            size *= 2
        return data
        
    def quick_sort(self, data):
        # Helper function to perform the partition
        def partition(arr, low, high):
            pivot = arr[high]
            i = low - 1
            for j in range(low, high):
                if arr[j] <= pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            return i + 1
        
        def quick_sort_recursive(arr, low, high):
            if low < high:
                pi = partition(arr, low, high)
                quick_sort_recursive(arr, low, pi - 1)  # Recursively sort the left sublist
                quick_sort_recursive(arr, pi + 1, high)  # Recursively sort the right sublist

        quick_sort_recursive(data, 0, len(data) - 1)
        return data
        
# initializing an object
alg = sorting_algorithms()

def test_sorting_alg(method_name):
    method = getattr(alg, method_name)
    
    # first 9 correspond to unsorted, the next 9 sorted and the next 9 reversely sorted
    # datasets time taken
    times = [0 for _ in range(27)]  

    for i in range(9):
        # unsorted dataset
        start1 = time.perf_counter()
        method(unsorted_lists[i])
        times[i] = time.perf_counter() - start1
        
        # sorted dataset
        start2 = time.perf_counter()
        method(sorted_lists[i])
        times[i + 9] = time.perf_counter() - start2
        
        # reversely sorted dataset
        start3 = time.perf_counter()
        method(reverse_sorted_lists[i])
        times[i + 18] = time.perf_counter() - start3
        
    return times

        

algorithms = {
    'bubble_sort' : [],
    'selection_sort' : [],
    'insertion_sort' : [],
    'merge_sort' : [],
    'tim_sort' : [],
    'quick_sort' : []}

for name in algorithms:
    algorithms[name] = test_sorting_alg(name)



# plotting data
# start and end mean the part of the data, where 0-8 indexes are unsorted data sorting time,
# 9-17 indexes are sorted data sorting times, and 18-26 are reversely sorted sorting times
def plot_data(name, start, end):
    plt.figure()
    plt.title(name)
    plt.xlabel("size of the data")
    plt.ylabel("seconds")
    
    plt.plot(lengths, algorithms['bubble_sort'][start : end], label = "bubble sort", color = 'blue')
    plt.plot(lengths, algorithms['selection_sort'][start : end], label = "selection sort", color = 'skyblue')
    plt.plot(lengths, algorithms['insertion_sort'][start : end], label = "insertion sort", color = 'red')
    plt.plot(lengths, algorithms['merge_sort'][start : end], label = "merge sort", color = 'purple')
    plt.plot(lengths, algorithms['tim_sort'][start : end], label = "tim sort", color = 'yellow')
    plt.plot(lengths, algorithms['quick_sort'][start : end], label = "quick sort", color = 'cyan')
    
    plt.legend(loc = 'best')
    plt.show()

plot_data("Sorting unsorted lists", 0, 9)
plot_data("Sorting sorted lists", 9, 18)
plot_data("Sorting reversely sorted lists", 18, 27)




