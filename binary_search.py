def binary_search(lst, left, right, key):

    if left == right:
        if key == lst[left]:
            return left
        else:
            return "element not found"

    while left <= right:
        mid = (left + right) //2

        if lst[mid] == key:
            return mid

        if key < lst[mid]:
            right = mid -1
        else:
            left = mid +1
        
    return -1

if __name__ == "__main__":
    lst = [3,2,6,7,8,9,30.44]
    lst2 = [10]
    result = binary_search(lst2,0, len(lst2)-1,9)
    print(result)


