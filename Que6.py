# Problem Description
# You are given the scores of a football league among a set of teams. You need to find the winner of the
# league and print the name of winner and points earned by the team. Each team gets 3 points for a win, 1
# point for a draw and O for a loss. The name of the teams is represented as upper case character viz. A B...
# z.
# Constraints
# There will only be one team which gets the highest points
# Input
# There are many lines in the input.
# 1
# The first line contains an integer, N, representing number of teams in the league. The next
# lines contain three space separated strings < Teaml, Team2, Score >


# Teaml is the name of the home team.
# Team2 is the name of the away team.
# Score represents the score of the match, (M-N), where M represents the score of the home team and N
# represents the score of the away team.

# Input
# 3
# A B 2-1
# B C 5-6
# C A 2-1

# Output
# c
# 6






n = int(input())  # Number of teams
freq = {}  # Dictionary to store team points

# Read input and process scores
for _ in range((n * (n - 1)) // 2):  # Total number of matches
    team1, team2, score = input().split()  # Read match details
    score1, score2 = map(int, score.split('-'))  # Extract M and N

    # Initialize teams in dictionary if not present
    if team1 not in freq:
        freq[team1] = 0
    if team2 not in freq:
        freq[team2] = 0

    # Update points based on match result
    if score1 > score2:
        freq[team1] += 3  # Home team wins
    elif score1 < score2:
        freq[team2] += 3  # Away team wins
    else:
        freq[team1] += 1  # Draw
        freq[team2] += 1  # Draw

# Find the team with the maximum points
max_team = max(freq, key=freq.get)
print(max_team)
print(freq[max_team])


        
        
