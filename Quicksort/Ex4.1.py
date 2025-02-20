def sum(arr):

    if (len(arr)==0): #base case
        return 0
    else: #recursive case
        return arr[0] + sum(arr[1:])
    

    

  