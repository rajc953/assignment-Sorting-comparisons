# comparison of bubble sort and selection sort
'''
Selection Sort : 
The selection sort algorithm generally is the first sorting algorithm that is taught to us.
Here in every iteration of the inner loop, the smallest element is replaced with the starting 
element in each loop. After the end of each loop, we increment the starting position by 1 and 
run it till the second last element in the array. Hence, by doing so at the end of the outer loop 
we will be having a sorted array.'''
def Selection_Sort(arr, n):
     
    for i in range(n - 1):
        min_index = i 
         
        for j in range(i + 1, n):
            if (arr[j] < arr[min_index]):
                min_index = j
                 
        arr[i], arr[min_index] = arr[min_index], arr[i] 
         

n = 5
arr = [ 2, 0, 1, 4, 3 ]
Selection_Sort(arr, n)
 
print("The Sorted Array by using " \
      "Selection Sort is : ", end = '')
for i in range(n):
    print(arr[i], end = " ")
    
#Bubble sort
def Bubble_Sort(arr, n):
    for i in range(1, n):
        for j in range(0, n - i):
            if (arr[j] > arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                 
    return arr
     
# Driver Code
n = 5
arr = [ 2, 0, 1, 4, 3 ]
arr = Bubble_Sort(arr, n)
 
print("The Sorted Array by using Bubble Sort is : ", end = '')
for i in range(n):
    print(arr[i], end = " ")

''' 	Selection Sort	Bubble Sort
1.	Selection sorting is a sorting algorithm where we select the minimum element from the array and put that at its correct position.	Bubble sorting is a sorting algorithm where we check two elements and swap them at their correct positions.
2.	Its Time complexity in the Best case is O(N^2)	Its Time complexity in the Best case is O(N)
3.	Its Time complexity in the worst case is O(N^2)	Its Time complexity in Worst case is O(N^2)
4.	This sorting algorithm uses the selection method	This sorting algorithm uses exchanging method
5.	It is an efficient sorting technique.	It is not an efficient sorting technique.
6.	This method is faster.	This method is slower.'''
# Python3 program for the above approach
 
# Function for bubble sort
def Bubble_Sort(arr, n):
    flag = True
     
    # Iterate from 1 to n - 1
    for i in range(1,n):
        flag = False
        # Iterate from 0 to n - i - 1
        for j in range(n-i):
            if (arr[j] > arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = True
         
        if (flag == False):
            break
         

n = 5
arr = [2, 0, 1, 4, 3]
Bubble_Sort(arr, n)
print("The Sorted Array by using Bubble Sort is : ", end='')
for i in range(n):
    print(arr[i], end= " ")
