def number_of_items(arr):
    if(arr==[]): #base case
        return 0
    else: #recursive case
        return 1 + number_of_items(arr[1:])
    
    


