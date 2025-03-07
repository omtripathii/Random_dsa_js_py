# Ques
# A plumber wants to check whether a pipe junction where N incoming pipes and M outgoing pipes are
# balanced, and, if not, needs to balance the junction by adding an input pipe or an output pipe of a suitable
# capacity. At the junction, there are a set of input pipes and a set of output pipes. Each pipe has a rated
# capacity and an actual capacity. The actual capacity for each pipe is lower than the rated capacity by a
# constant R, the "rust factor", which depends on the material of the pipe, and is the same for all the pipes
# at the junction.
# For example, if the rated capacity is 65, and R is 2, the actual capacqty is 63.

# A junction is balanced if the sum of the actual capacities of the input pipes is the same as the sum of the
# actual capacities of the output pipes. If it is not balanced, the plumber needs to add one input pipe or one
# output pipe to balance the junction, and determine the rated capacity of that added pipe.
# Hel Here we have N incoming pipes and M outgoing pipes. The incoming pipes may be of different rated
# capacities. Similarly, the outgoing pipes may also be of different rated capacities.
# Find the rated capacity of the pipe required to make the junction balanced. If the combined actual capacity
# of the incoming pipes is more than the combined actual capacity of the outgoing pipes then the plumber
# will need to add an outgoing pipe. Conversely, if the combined actual capacity of the incoming pipes is less
# than the combined actual capacity of the outgoing pipes then the plumber will need to add an incoming
# pipe.
# If an outgoing pipe is added then denote its rated capacity as a negative number. If an incoming pipe is
# added then denote its rated capacity as a positive number.


# Find the rated capacity of the pipe required to make the junction balanced. If the combined actual capacity
# of the incoming pipes is more than the combined actual capacity of the outgoing pipes then the plumber
# will need to add an outgoing pipe. Conversely, if the combined actual capacity of the incoming pipes is less
# than the combined actual capacity of the outgoing pipes then the plumber will need to add an incoming
# pipe.
# If an outgoing pipe is added then denote its rated capacity as a negative number. If an incoming pipe is
# added then denote its rated capacity as a positive number.


# Input
# The input has three lines
# The first line contains three space separated integers N M R denoting the number of incoming pipes,
# outgoing pipes and rust factor respectively.
# The second line contains N space separated integers denoting the rated capacity of each incoming pipe.
# The third line contains M space separated integers denoting the rated capacity of each outgoing pipe.
# Output
# Print the rated capacity of the pipe required to balance the junction OR print "BALANCED" if the junction is
# already balanced.
# Activate Vli nd D.A.'s


# input
# 332
# 185 75 95
# 70 80 45
# Output
# -62
# Explanation
# There are 3 input pipes, 3 output pipes, and the rust factor is 2.


n = list(map(int,input().strip().split()))
inc = list(map(int, input().strip().split()))[:n[0]]
out = list(map(int,input().strip().split()))[:n[1]]

actual_input = sum(inc) - (n[0] * n[2])
actual_output = sum(out) - (n[1] * n[2])

if actual_input == actual_output:
    print("BALANCED")
else:
    if actual_input > actual_output:
        val = (actual_input - actual_output)+ n[2]
        print(-val)
    else:
        val = (actual_output - actual_input) + n[2]
        print(val)



# # Read input
# N, M, R = map(int, input().split())
# inc = list(map(int, input().split()))[:N]
# out = list(map(int, input().split()))[:M]

# # Compute actual capacities
# actual_input = sum(inc) - (N * R)
# actual_output = sum(out) - (M * R)

# # Determine if balanced or compute required pipe capacity
# if actual_input == actual_output:
#     print("BALANCED")
# else:
#     required_capacity = abs(actual_input - actual_output) + R
#     if actual_input > actual_output:
#         print(-required_capacity)  # Need an outgoing pipe
#     else:
#         print(required_capacity)   # Need an incoming pipe
