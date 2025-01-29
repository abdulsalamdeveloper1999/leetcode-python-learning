# #return index of the target if found else return -1


def linear_search(arr,target):
    size=len(arr)
    for index in range(0,size):
        if arr[index]==target:
            return index
        
    return -1





arr=[20,40,70,90]
target=70
result=linear_search(arr,target)
print(result)