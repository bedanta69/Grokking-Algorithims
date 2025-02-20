def Quicksort(arr):
    if len(arr)<2: #base case
        return arr
    else: #recursive case
        pivot = arr[0]
        less = [i for i in arr[1:] if i < pivot]
        greater =[i for i in arr[1:] if i> pivot]
        return Quicksort(less) + [pivot] + Quicksort(greater)

