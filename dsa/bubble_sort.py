def bubble_sort(lst):
    size = len(lst)
    for passes in range(size):
        swapped=False
        for j in range(size-1-passes):
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1]=lst[j+1],lst[j]
                swapped=True
        if not swapped:
            break
    return lst


            
lst = [64, 34, 25, 12, 22, 11, 90]
result=bubble_sort(lst)

print(result)