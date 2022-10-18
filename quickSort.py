



def quicksort(array, left, right):
    if  left < right:
        Povit_index = partition(array, left, right)
        quicksort(array, left, Povit_index - 1)
        quicksort(array, Povit_index + 1, right)


def partition(array, left, right):
    """
    28,18,38,48,58,78,98,88,   68        
    |                    |      |  10
    i                    j       p  
    """
    i= left
    j = right - 1
    p = array[right] 

    while i < j: # ig i is big than j which means i has corssed the j 
        # 1 . i should move till i < p
        while i < right and array[i] < p:
            i += 1 
        # 2.  j should move till i > p
        while j > left and array[j] >= p:
            j -= 1
        # 3.  swap the elements 
        if i < j:
            array[i], array[j] = array[j], array[i]

    # i <swap> p
    if array[i] > p:
        array[i], array[right] = array[right], array[i]

    # povit_index = i 

    return i
        
elements = [28,18,38,48,58,78,98,88,68]
quicksort(elements, 0, len(elements) - 1)
print(elements)

    




