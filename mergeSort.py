

def mergesort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2

    left = arr[:mid]
    right = arr[mid:]

    left = mergesort(left)
    right = mergesort(right)

    return mergeSort_to_sorted(left, right)
    

def mergeSort_to_sorted(A,B):
    sortedTempArray = []
    lengthOfA = len(A)
    lengthOfB = len(B)

    i = j = 0

    while i<lengthOfA and j<lengthOfB:
        if A[i] <=  B[j]:
            sortedTempArray.append(A[i])
            i += 1 
        else:
            sortedTempArray.append(B[j])
            j += 1 
    
    while i < lengthOfA:
        sortedTempArray.append(A[i])
        i += 1

    while j < lengthOfB:
        sortedTempArray.append(B[j])
        j += 1

    return sortedTempArray

# a = [17,18,40,50]
# b = [1,9,20,25]

arr = [17,18,10,28,5,2,20,21]

print(mergesort(arr))
# 1,2,17,18,20,25,40,50


