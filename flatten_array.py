'''
given an array of arbitrary arrays, 
return a flattened array containing integers
'''
def flatten_array(arr):
    flattened_array = []
    for i in arr:
        #if i is an integer, no need to do anything
        if isinstance(i, int): 
            flattened_array.append(i)
        #if i is a list, flatten it through a recursive call and add it to flattened_array
        elif isinstance(i, list): 
            flattened_array = flattened_array + flatten_array(i)
    return flattened_array