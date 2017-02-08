import math
import random
import sys
import time

from matplotlib import pyplot

from bubble_sort import bubble_sort
from quick_sort_concept import quick_sort


def get_running_time(data_list):
    tic = time.clock()
    bubble_sort(data_list)
    toc = time.clock()
    bsort_running_time = toc - tic
    
    tic = time.clock()
    quick_sort(data_list)
    toc = time.clock()
    qsort_running_time = toc - tic
    
    return bsort_running_time, qsort_running_time

def get_running_time_vs_size():
    size_list = [2**p for p in range(4, 14)]
    size_running_time_list = []
    for size in size_list:
        data_list = [random.randint(0, 1000) for _ in range(0, size)]
        bubble_sort_time, quick_sort_time = get_running_time(data_list)
        size_running_time_list.append((size, bubble_sort_time, quick_sort_time))
    return size_running_time_list
    

def plot_running_time_vs_size(size_running_time_list, add_log_reference=False, factoring=False):
    fig = pyplot.figure(figsize=[20, 10])  

    sizes = [s for s,_,_ in size_running_time_list]
    bsort_running_time_list = [t for _,t,_ in size_running_time_list]
    qsort_running_time_list = [t for _,_,t in size_running_time_list]

    fig.add_subplot(121)      
    pyplot.plot(sizes, bsort_running_time_list, 'ro--')
    pyplot.plot(sizes, qsort_running_time_list, 'bs-.')
    pyplot.xlabel('Size of List (n)')
    pyplot.ylabel('Running Time (second)')
    pyplot.title('Running Time vs. Size of List')
    pyplot.legend(['Bubble Sort', 'Quick Sort'], loc='upper left')
    
    fig.add_subplot(122)      
    pyplot.loglog(sizes, bsort_running_time_list, 'ro--')
    pyplot.loglog(sizes, qsort_running_time_list, 'bs-.')
    legend_list = ['Bubble Sort', 'Quick Sort']
    if add_log_reference:
        if factoring:
            bsort_factor = bsort_running_time_list[-1]/sizes[-1]**2 
            qsort_factor = qsort_running_time_list[-1]/(sizes[-1]*math.log(sizes[-1]))
        else:
            bsort_factor = 1
            qsort_factor = 1
        pyplot.loglog(sizes, [bsort_factor*s**2 for s in sizes], 'g*--')
        pyplot.loglog(sizes, [qsort_factor*s*math.log(s) for s in sizes], 'mx-.')
        legend_list.append(r'$n^2$')
        legend_list.append(r'$n\log(n)$')
    pyplot.xlabel('Size of List (n)')
    pyplot.ylabel('Running Time (second)')
    pyplot.title('Running Time vs. Size of List (in Log-Log Scale)')
    pyplot.legend(legend_list, loc='upper left')
    
    pyplot.show()
    

if __name__ == '__main__':
    sys.setrecursionlimit(max(sys.getrecursionlimit(), 2000000))   
    size_running_time_list = get_running_time_vs_size()
    plot_running_time_vs_size(size_running_time_list, add_log_reference=False, factoring=False)