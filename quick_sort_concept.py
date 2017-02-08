
def quick_sort(data_list):
    '''
    This implementation demonstrates the concept of the Bubble Sort.
    
    This implementation does change the input argument (data_list).
    '''
        
    # check if the list is empty
    if not data_list: return data_list
    
    # pick a pivot
    pivot = data_list[0]

    # divide the data into two halves, one is smaller (or equal to) the pivot and the other greater
    less = [elem for elem in data_list[1:] if elem <= pivot]
    greater = [elem for elem in data_list[1:] if elem > pivot]
    
    # apply the same strategy to the two halves
    less = quick_sort(less)
    greater = quick_sort(greater)
    
    return less + [pivot] + greater

