def max(arr):
    if(len(arr)==2): #base case
        return arr[0] if arr[0]>arr[1] else arr[1]
    submax = max(arr[1:])# recursive case
    return arr[0] if arr[0]> submax else submax
        
    