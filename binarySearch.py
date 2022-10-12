## lineary search 

from multiprocessing import reduction


def LinearSearch(nums_list, numberToBeSearch): # -> O(N)
    for i in range(len(nums_list)):
        if nums_list[i] == numberToBeSearch:
            return i
    else:
        return -1

## binary search 

"""
2,3,9,11,15,16,19,20,25
                     h
                         l
                     m

2,3,9,11,15,16,19,20,25
l      h m  l         h
                     

"""

def BinarySearch(nums_list, numberToBeSearch): # -> O(LonN)
    L = 0 
    H = len(nums_list) - 1

    mid_index = 0 
    while L <= H:
        mid_index = (L + H) // 2

        mid_number = nums_list[mid_index]

        if mid_number == numberToBeSearch:
            return mid_index
        elif mid_number < numberToBeSearch:
            L = mid_index + 1
        else:
            H = mid_index - 1

    return -1  


nums = [2,3,9,11,15,16,19,20,25]
print(BinarySearch(nums,19))


"""
1. [2,3,3,3,9,9,11,11,11,15,15,15,16,19,19,20,25,25]


-> all the indexs of 11

index_of_fist11 = ?


                   <-----------             index_of_fist11               ------------->

reslt = [ , , ,]


for left array 

index = index_of_fist11 -1 

loop 

index = index -1 

for Right array 

index = index_of_fist11 + 1 

loop 

index = index -1 


"""
