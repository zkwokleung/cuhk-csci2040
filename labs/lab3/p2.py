def quicksort(lista, listb):
    # merge the list
    l = lista + listb
    if len(l) < 1:
        return []
    # pivot
    p = l[0]
    # Smaller elements
    small = [x for x in l[1:] if x < p]
    # Larger elements
    larger = [x for x in l[1:] if x >= p]
    # recursive and combine with larger on left smaller on right
    return quicksort(larger, []) + [p] + quicksort(small, [])
