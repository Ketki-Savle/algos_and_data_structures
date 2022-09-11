def mergeSort(lst):
    if len(lst) >1:
        mid = len(lst)//2
        left = lst[:mid]
        right = lst[mid:]
    
        mergeSort(left)
        mergeSort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst[k] = left[i]
                i = i+1
            else:
                lst[k] = right[j]
                j = j+1
            k = k+1

        #remaining elements:
        while i < len(left):
            lst[k] = left[i]
            i = i+1
            k += 1

        while j < len(right):
            lst[k] = right[j]
            j = j+1
            k += 1

        
if __name__ == '__main__':
    lst = [3, 2, 1, 5, 4]
    mergeSort(lst)
    print(lst)


