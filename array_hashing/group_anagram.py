# 49. Group Anagrams
# Medium
# Topics
# Companies
# Given an array of strings strs, group the 
# anagrams
#  together. You can return the answer in any order.

 

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]

# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Explanation:

# There is no string in strs that can be rearranged to form "bat".
# The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
# The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
# Example 2:

# Input: strs = [""]

# Output: [[""]]

# Example 3:

# Input: strs = ["a"]

# Output: [["a"]]

# def groupAnagrams(strs):
#     hash_map=dict()

#     for word in strs:
#         sorted_word="".join(sorted(word))
#         if sorted_word not in hash_map:
#             hash_map[sorted_word]=[]
#         hash_map[sorted_word].append(word)
#     return list(hash_map.values())
        

# strs = ["eat","tea","tan","ate","nat","bat"]

# print(groupAnagrams(strs))

# _________________________
from collections import defaultdict


def group_anagrams(strs):
    groups_anagram=defaultdict(list)

    for word in strs:
        char_count=[0]*26
        for char in word:
            char_count[ord('a')-ord(char)]+=1
        groups_anagram[tuple(char_count)].append(word)
    return list(groups_anagram.values())



strs = ["eat","tea","tan","ate","nat","bat"]

print(group_anagrams(strs))