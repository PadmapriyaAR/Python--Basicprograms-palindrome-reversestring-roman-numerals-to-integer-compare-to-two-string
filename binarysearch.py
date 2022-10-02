integerSet = [2,4,8,23,45,67,68,93]

def binary_search(integerSet, startIndex, endIndex, search_Value):
    if(endIndex > startIndex):
        midIndex = (endIndex + startIndex) // 2
        if integerSet[midIndex] == search_Value:            
            return midIndex
        elif search_Value < integerSet[midIndex] :
            return binary_search(integerSet, startIndex, midIndex, search_Value)
        else:
            return binary_search(integerSet, midIndex+1, endIndex, search_Value)
    else:
       return -1

if __name__ == "__main__":
    print("Result ", binary_search(integerSet, 0, len(integerSet), int(input("Enter a number : "))))