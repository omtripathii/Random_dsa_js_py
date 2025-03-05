# A coding competition was conducted in company with e employees. Data of employees who participated
# and who did not participate in the competition is available. There were three problems in the coding
# competition. Data as mentioned below is available
# The number of employees who have solved only the first,
# only the second and only the third problem are equal.
# QI
# pl employees who solved the first ,second problem.
# p2 employees who solved the second , third problem.
# p3 employees who solved the third first problem.
# q employees who solved all the 3 problems.
# r employees who did not participate in competition.
# Answer the following questions based on data .

# • How many employees have solved the first problem?
# • How many employees have solved exactly one of the 3 problems.

p1 = int(input())
p2 = int(input())
p3 = int(input())
q = int(input())
e = int(input())
r = int(input())

res1 = (e-r + 2*q -p1-p2-p3) 
res2 = ((res1 // 3) - (p1 + p2) + q)
print(res1)
print(res2)