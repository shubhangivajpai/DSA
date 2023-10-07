
#The function accepts two positive integers ‘r’ and ‘unit’ and a positive integer array ‘arr’ of size ‘n’ as its argument ‘r’ represents the number of rats present in an area, ‘unit’ is the amount of food each rat consumes and each ith element of array ‘arr’ represents the amount of food present in ‘i+1’ house number, where 0 <= i

#Note:

#Return -1 if the array is null
#Return 0 if the total amount of food from all houses is not sufficient for all the rats.
#Computed values lie within the integer range.
#Example:

#Input:

#r: 7
#unit: 2
#n: 8
#arr: 2 8 3 5 7 4 1 2
#Output:4
r = int(input())
unit = int(input())
n = int(input())
arr = list(map(int, input().split()))
total_amount = r * unit
start = 0
count = 0
curr_amt = 0

if n == 0:
    print(-1)
else:
    while start < n:
        if curr_amt < total_amount:
            curr_amt += arr[start]
            count += 1
            start += 1
        elif curr_amt >= total_amount:
            print(count)
            break
    else:
        print(-1)
