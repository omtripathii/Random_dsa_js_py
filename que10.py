# Given n non—negative integers representing an elevation map where the Width Of each bar is corn pute
# how much water it can trap after raining.

n = list(map(int, input().strip().split()))

# Edge case: If there are less than 3 bars, no water can be trapped
if len(n) < 3:
    print(0)
    exit()

left_max = [0] * len(n)
right_max = [0] * len(n)

# Compute left max for each index
left_max[0] = n[0]
for i in range(1, len(n)):
    left_max[i] = max(left_max[i - 1], n[i])

# Compute right max for each index
right_max[-1] = n[-1]
for i in range(len(n) - 2, -1, -1):
    right_max[i] = max(right_max[i + 1], n[i])

# Calculate trapped water
total_water = 0
for i in range(len(n)):
    total_water += min(left_max[i], right_max[i]) - n[i]

print(total_water)
