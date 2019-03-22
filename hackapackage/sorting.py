def bubble_sort(items):

    '''Return array of items, sorted in ascending order'''
    n = len(items)
    for i in range(n):
        for j in range(0,n-i-1):
            if items[j]>items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]
    return items

def merge_sort(items):

    '''Return array of items, sorted in ascending order'''
    if len(items)<2:
        return sorted(items)
    new_items = []
    n = len(items)
    mid = int(n/2)
    x = merge_sort(items[:mid]) #recursively dividing the elements on the left of the middle element
    y = merge_sort(items[mid:]) #recursively dividing the elements on the right of the middle element
    i = 0
    j = 0
    while i < len(x) and j < len(y):
        if x[i] > y[j]:
            new_items.append(y[j])
            j += 1
        else:
            new_items.append(x[i])
            i += 1
    new_items += x[i:]
    new_items += y[j:]
    return new_items

def quick_sort(items):

    '''Return array of items, sorted in ascending order'''
    less = [] #for elements less than the pivot
    greater = [] #for elements greater than the pivot
    equal = [] #for the element equal to the pivot
    n = len(items)
    if n <= 1:
        return items
    else:
        pivot = items[0]
        for i in items:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                greater.append(i)
            else:
                equal.append(i)
        return quick_sort(less) + equal + quick_sort(greater) # 
