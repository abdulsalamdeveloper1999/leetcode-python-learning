def contains_duplicate(nums):
    """
    Function to check if the array contains any duplicate elements.
    :param nums: List[int] -> The input list of integers
    :return: bool -> True if duplicates exist, False otherwise
    """
    # TODO: Implement this function using a hashmap
    hash_set=set()
    for i in nums:
        if i in hash_set:
           return True
        else:
            hash_set.add(i)
            return True



nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]

print(contains_duplicate(nums))