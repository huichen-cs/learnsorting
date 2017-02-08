
def bubble_sort(data_list):
    '''
    This implementation demonstrates the concept of the Bubble Sort.
    
    This implementation does change the input argument (data_list).
    '''
    data = data_list
    for num_elems in range(len(data)-1, 0, -1):
        # bubble the greatest element up
        for i in range(num_elems):
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]   
    return data
