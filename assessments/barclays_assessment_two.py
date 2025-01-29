# Question
# the company decides to place a distortion
# avoidance device at all such locations. Find the number of devices the company needs to place.
# Write an algorithm to find the number of distortion avoidance devices the company needs to place.

# Input
# The first line of the input consists of two space-separated integers -
# num and coordinate Count, representing the number of routes (N) and the number of coordinates of the two locations connected by a route (M is always equal to 4). The next N lines consist of M space- separated integers representing the respective x and y coordinates of the two locations that are connected to each other.

# Output
# Print an integer representing the number of distortion avoidance devices the company needs to place.

# Constraints
# 0s nums 104
# 0sx,ys 109; x and y represents x and y
# coordinates of a location

# Example Input:
# 34
# 1145
# 0332
# 2453
# Output:
# 2
# Explanation:
# The route of the coordinates (1,1), (4,5)
# intersects with the routes of the coordinates (0,3), (3,2) and (2,4), (5,3).
# Two distortion avoidance devices must be placed here.
# So, the output is 2.