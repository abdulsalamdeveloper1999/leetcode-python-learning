#for binary we have to get start , mid, end part and array need to be sorted

def binary_search(arr,target):
    size=len(arr)
    start=0
    end=size-1

    while (start<=end):
        mid=(start+end)//2

        if arr[mid]==target:
            return mid
        
        elif arr[mid]>target:
            end=mid-1
        
        elif arr[mid]<target:
            start=mid+1
    return -1

arr=[12, 25, 72, 85, 116, 148, 152, 168, 220, 246, 
     286, 333, 344, 370, 426, 437, 442, 466, 472, 474,
      494, 496, 514, 530, 555, 561, 569, 581, 584, 587,
        622, 631, 637, 660, 672, 687, 699, 737, 757, 766, 
        774, 884, 890, 913, 941, 952, 968, 972, 975, 977]

target=631

result=binary_search(arr,target)


print(result)




