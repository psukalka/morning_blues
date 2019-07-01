"""
For a given array A, make A[i] = A[A[i]] with O(1) extra space
Date: 29/06/19
# COULDN'T SOLVE
"""
import random

def replace(A):
    size = len(A)
    counter = 0
    for i in range(0,n):
        temp = A[i]
        if temp > i:
            A[i] = A[temp]
            counter += 1
            for j in range(0, n):
                if A[j] == i:
                    A[j] = temp
                    counter += 1
    return A


n = 3
arr = []
for i in range(n):
    arr.insert(i, random.randint(0, n-1))

print(arr)
replace(arr)
print(arr)