import random
def binary_search(list,target):
    low = 0 
    high = len(list)-1
    if low >= high:
        return -1 
    while high >= low:
        midpoint = (low + high)//2
        if list[midpoint] == target:
            return midpoint
        if target >= list[midpoint]:
            low = midpoint + 1
        else: 
            high = midpoint - 1
def guessing(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in list")
books =  ["The Cat in the Hat", "Green Eggs and Ham", "Oh the Places You'll Go","The Grinch", "Horton", "The Lorax"]
books.sort()
result = binary_search(books, random.choice(books))
guessing(result)