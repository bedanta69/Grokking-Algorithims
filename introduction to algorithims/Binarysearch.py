def binary_search(list,items):
    low = 0
    high =len(list)-1
    while low <= high:
        mid = low + high //2
        guess = list[mid]
        if(guess == item):
            return mid
            break;
        elif(guess>mid):
            high = mid - 1
        else:
            low = mid + 1

    return NUll
