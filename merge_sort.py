def mergeSort(inputList):
    length = len(inputList)
    if length <= 1:
        return inputList

    middleIndex = length // 2
    left = inputList[:middleIndex]
    right = inputList[middleIndex:]

    left = mergeSort(left)
    right = mergeSort(right)
    return list(merge(left, right))

def merge(left, right):
    sorted = []
    i = 0 # pointer to keep track of index in left list
    j = 0 # pointer to keep track of index in right list

    while i < len(left) and j < len(right):
        # at each step, compare the next values from left & right.
        # Choose the lowest of the two values to append to the result list 
        if left[i] <= right[j]:
            sorted.append(left[i])
            i += 1
        else:
            sorted.append(right[j])
            j += 1

    # If the lists are different length, we may need to also transfer over the additional elements from the longer list. There are other ways to implement this, but this version provides an easy catch-all without additional logic
    sorted.extend(left[i:])
    sorted.extend(right[j:])
    return sorted

# Test cases:
unsortedList = [1, 97, 36, -4, 0, 124, 3000]
print(mergeSort(unsortedList)) # -4, 0, 1, 36, 97, 124, 3000