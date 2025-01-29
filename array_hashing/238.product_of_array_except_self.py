# 238. Product of Array Except Self
# Medium
# Topics
# Companies
# Hint
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
 

# Constraints:

# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.
 

# Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

from typing import List

#divison method
# def productExceptSelf(nums):
#     output=[]
#     product=1
#     for i in range(len(nums)):
#         product=product*nums[i]
#     for j in nums:
#         output.append(product//j)

       
#     print(product)        
#     return output
def productExceptSelf(nums):
    input_nums=[1]*len(nums)
    left_pos=1
    right_pos=1

            #start with left
    for i in range(len(nums)):
        input_nums[i]=left_pos
        left_pos=left_pos*nums[i]

    for j in range(len(nums)-1,-1,-1):
        input_nums[j]=right_pos*input_nums[j]
        right_pos=right_pos*nums[j]
            
    return input_nums 
            


nums = [1,2,3,4]


print(productExceptSelf(nums))