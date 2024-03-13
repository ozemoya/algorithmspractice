def recursive_binary_search(list,target):
   low = 0
   high = len(list) - 1
   if low > high:
        return -1
   if len(list) == 0:
        return False
   else:
        midpoint = (len(list))//2 #midpoint
        if list[midpoint] == target:
            return midpoint
        else:
            if list[midpoint] < target:
                return recursive_binary_search(list[midpoint+1:],target)
            else: 
                return recursive_binary_search(list[:midpoint],target)

def verify(result):
    print("Target found: ", result)
    
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = recursive_binary_search(numbers, 12)
verify(result)
result = recursive_binary_search(numbers, 1)
verify(result)

