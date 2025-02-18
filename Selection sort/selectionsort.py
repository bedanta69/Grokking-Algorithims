def Selectionsort(arr):
    newArr=[]
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
        return newArr
    
