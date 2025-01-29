# 347. Top K Frequent Elements
# Medium
# Topics
# Companies
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.

# Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        key_value_count={}
        bucket_freq=[[] for i in range(len(nums)+1)]

        for i in nums:
            key_value_count[i]=key_value_count.get(i,0)+1
            #1:3
            #2:2
            #3:1

        for n,c in key_value_count.items():
            bucket_freq[c].append(n)
        #[[3],[2],[1],[],[],[]]

        res=[]
        for i in range(len(bucket_freq)-1,0,-1):
            #loop will run 6 times because we have 6 buckets from 5 to 0
            for n in bucket_freq[i]:
                #inner loop will come to index of bucket which is list also and takes its value and appent to res
                res.append(n)
                if (len(res)) == k:
                    #if res size is equal to k return
                    return res

        

        


