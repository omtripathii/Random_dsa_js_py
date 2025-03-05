# In network marketing a person who sells some merchandise becomes the root node of a so-called network
# marketing tree. When the first person inducts someone into the network marketing tree the first person
# becomes the supervisor. Likewise, if this new recruit inducts a third person into the network marketing
# tree the new recruit becomes supervisor of the third person. The tree grows so on and so forth.
# c
# Whenever anybody in the network marketing tree makes a profit, they have to pass a certain percentage
# of that profit to their supervisor. The percentage of the profit passed to the superior will be rounded to the
# nearest integer, and hence will always be an integer at each level. Calculate the profit of the person at the
# root of the network marketing tree coming from a p%rticular individual at Nth level in the tree.
# The first line contains an integer N, which determines the height of the network mark
# E: xyz > New Section
# The second line contains an integer M, which denotes the profit earned by a particular individual at Nth
# level
# The third line contains an integer P, which denotes profit % that needs to be passed on to supervisor. Each
# supervisor will always get an integer amount of the profit (rounded to the nearest integer) from his
# subordinate.
# Output
# The profit earned by the pelson at the root of the network marketing tree coming from a particular
# individual at Nth level in the tree, rounded off to the nearest integer.


n = int(input())
m = int(input())
p = int(input())

i = 0
while i < n-1:
    m = (p * m) / 100
    i+=1
print(int(m))

