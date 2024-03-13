#Make a linear search function, list and function 
#to return index position of target

def linear_search(list, target): 
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None
    
    
#verify check if the item is in the list, if it is Target is found at index: 
def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in list")

numbers = [1,2,3,4,5,6,7,8,9,10]
result = linear_search(numbers, 6)
verify(result)