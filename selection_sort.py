
#Time Complexity:  O(n2).
#Auxiliary Space: O(1).

#Selection sort is a simple comparison-based sorting algorithm. It works by repeatedly selecting the minimum (or maximum) element from an unsorted part of the list and moving it to the beginning of the sorted part. Here's a step-by-step explanation using an example:


#method 1
def find_minindex(arr,start):
    min_idx=start
    for i in range(start+1,n):
        if arr[min_idx]>arr[i]:
            min_idx=i
    return min_idx
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx=find_minindex(arr,i)
        arr[min_idx],arr[i]=arr[i],arr[min_idx]
    return arr
arr=list(map(int,input().split()))
n=len(arr)
print(selection_sort(arr))

#method2
def selectionsort(arr,n):
    for i in range(n):
        min_idx=i
        for j in range(i+1,n):
            if arr[j]<arr[min_idx]:
                min_idx=j
        arr[i],arr[min_idx]=arr[min_idx],arr[i]
    return arr
arr=list(map(int,input().split()))
n=len(arr)
print(selectionsort(arr,n))
