
# In a town, the houses are marked with
# English letters. A town committee wants to renovate each house. Because funds are limited, 
# they decide to renovate only the houses marked with vowels. 
# The committee head gives the list of houses to the members and asks them to identify the houses that will not be renovated.
# Write an algorithm to help the committee members find the list of houses that will not be renovated.

# Input
# The input consists of a string houses, representing the sequence of house markings.

# Output

# Print a string representing the list of houses that will not be renovated. If no such house is found then donot print anything.

# Constraints
# All the house markings are English letters.

# Note
# The vowels are A, E, I, O, U, a, e, i, o, u.

# Example

# Input:
# MynameisAnthony

# Output: Mynmsnthny

# Explanation:
# The list of houses that will not be renovated is Mynmsnthny.

def renHouse(houses):
    vowels='A, E, I, O, U, a, e, i, o, u'
    vow=vowels.replace(', ','')
    # print(vow)
    ren_houses=list()

    for i in range(len(houses)):
        if houses[i] not in vow:
            ren_houses.append(houses[i])
    x=''.join(ren_houses) 
    return x



houses='MynameisAnthony'

print(renHouse(houses))
