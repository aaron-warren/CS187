def merge(arr1, arr2):
    # Initializes variables
    arr = []
    i = 0
    j = 0

    # Loops until both arrays are fully checked
    while True:
        # Checks if first pointer is still within range
        # Then checks if the 2nd array is fully checked or if the 1st array has the lower value
        if i < len(arr1) and (j >= len(arr2) or arr1[i] <= arr2[j]):
            arr.append(arr1[i]) # If so then it will append the new value to the new array
            i = i + 1 # And then increment the pointer
        else: # Same thing except for array 2
            arr.append(arr2[j])
            j = j + 1

        # If both arrays are fully checked then it will break out of the loop
        if i >= len(arr1) and j >= len(arr2): 
            break

    # And then return the final array with the values
    return arr


if __name__ == "__main__":
    arr1 = [1, 2, 7, 11]
    arr2 = [3, 7, 13, 16, 29]

    print(merge(arr1,arr2))
    pass