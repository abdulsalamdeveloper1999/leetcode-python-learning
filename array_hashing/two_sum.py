# from typing import List


# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
# def two_sum(nums,target):
    
#     for i in range(len(nums)):
#         select_value=i
#         for j in range(i+1,len(nums)):
#             if (nums[select_value]+nums[j])==target:
#                 return [select_value,j]
# #case 1            
# # nums=[2,7,11,5]
# # target=9

# #case 2
# nums = [3,2,4]
# target = 6

# result=two_sum(nums,target)

# print(result)
           
# big O is o(n ^ 2)
    

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
def two_sum(nums,target):
    prev_map={}
    for i,n in enumerate(nums):
        diff=target-n
        if diff in prev_map:
            return [prev_map[diff],i]
        prev_map[n]=i
    return
# big O is o(1)

#case 1            
nums=[2,7,11,5]
target=9

#case 2
# nums = [3,2,4]
# target = 6

result=two_sum(nums,target)

print(result)

