def sorted_array(first, second):
    array = []
    for i in first + second:
        if i > 0:
            array.append(i)
    return sorted(array)    
