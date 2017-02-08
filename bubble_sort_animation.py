from matplotlib import font_manager
from matplotlib import patches
from matplotlib import pyplot

import random


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
            draw_bubbles(data, num_elems, i+1)
        
    return data

def draw_bubbles(data_list, num_elems, bubble_idx):
    ffam = 'courier new'
    fp = font_manager.FontProperties(family=ffam, 
                                     style='normal', 
                                     size=30, 
                                     weight='normal', 
                                     stretch='normal')    
    ax = pyplot.gca()
    ax.clear()
    pyplot.hold(True)

    if not num_elems is None:
        pyplot.plot([0, 1], [(num_elems+1)/10, (num_elems+1)/10], 'r-')
    
    for idx,value in enumerate(data_list):
        if not bubble_idx is None and idx == bubble_idx:
            color = 'white'
        else:
            color = 'yellow'
        if not bubble_idx is None:
            box_high = bubble_idx/10+3/30
            box_low = (bubble_idx-1)/10
            pyplot.plot([0.4, 0.6, 0.6, 0.4, 0.4], [box_low, box_low, box_high, box_high, box_low],'b-')
        circ = patches.Circle((0.5,idx/10+1.5/30), 1/30, transform=ax.transAxes,
                      facecolor=color, alpha=0.5)
        ax.add_patch(circ)
        ax.text(0.5-len(str(value))*0.0125,idx/10+1.5/30-0.01, str(value), fontproperties=fp)
        
    if not num_elems is None:
        pyplot.plot([0, 1], [.05/30, .05/30], 'r-')    
        
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    pyplot.axis('off')

    if not num_elems is None:
        pyplot.pause(0.1)
    


if __name__ == '__main__':
    data = [random.randint(1, 10) for _ in range(0, 10)]

    pyplot.figure(figsize=[12, 12])
    pyplot.ion()
    sorted_data = bubble_sort(data)
    pyplot.clf()
    pyplot.ioff()
    draw_bubbles(sorted_data, None, None)
    pyplot.show()
