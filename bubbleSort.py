

def BubbleSort(listOfElements):
    """
    for elements:
       - get the highest element in to its sorted postion 
    
    45   19,26,20,2,6,1,12 ,
    0+1  1            i
    i    i+1
    """
    lengthOfList = len(listOfElements)
    for j in range(lengthOfList - 1): # 0,1,2
    # [1, 2, 6, 12, 19, 20, 26, 45]
        for i in range(lengthOfList - 1): # -> this for loop will get the sorted place of one element 
            if listOfElements[i] > listOfElements[i+1]:
                temp = listOfElements[i]
                listOfElements[i] = listOfElements[i+1]
                listOfElements[i+1] = temp 
            ## listOfElements[i], listOfElements[i+1] = listOfElements[i+!],listOfElements[i]

elements = [45,19,26,20,2,6,1,12]

BubbleSort(elements)
print(elements)

"""
1. acs --> dec 

2. [45,19,26,20   ,2,6,1,12]

    acs           dec 

-> 5 mins 

"""







