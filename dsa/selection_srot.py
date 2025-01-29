def sort_selection(arr):
    size = len(arr)
    


    for i in range(size-1):
        min_index=i
        for j in range(i+1,size):
            if arr[min_index]>arr[j]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]

    return arr



arr=[11,33,12,5,60,55,90]

print(sort_selection(arr))

