# # 242. Valid Anagram
# # Easy

# # Given two strings s and t, return true if t is an 
# # anagram
# #  of s, and false otherwise.

 
# # Example 1:

# # Input: s = "anagram", t = "nagaram"

# # Output: true

# # Example 2:

# # Input: s = "rat", t = "car"

# # Output: false

# # Constraints:

# # 1 <= s.length, t.length <= 5 * 104
# # s and t consist of lowercase English letters.
 
# # Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

def isAnagram( s: str, t: str) -> bool:
    #because anagram should have same lenght
    if len(s)!=len(t):
        return False
    
    dicS,dicT={},{}

    for i in range(len(s)):
        #get the key if not in dict assign 0 to it instead of throwing an error
        dicS[s[i]]=dicS.get(s[i],0)+1    
        dicT[t[i]]=dicT.get(t[i],0)+1

    for c in dicS:
        if dicS.get(c)!=dicT.get(c):
            return False
    return True
    

        

# s = "anagram"
# t = "nagaram"

s="rat"

t ="car"

result=isAnagram(s,t)

print(result)







