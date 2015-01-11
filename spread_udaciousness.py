# Spreading Udaciousness
 
# One of our modest goals is to teach everyone in the world to program and
# understand computer science. To estimate how long this will take we have
# developed a (very flawed!) model:

# Everyone answering this question will convince a number, spread, (input to 
# the model) of their friends to take the course next offering. This will 
# continue, so that all of the newly recruited students, as well as the original
# students, will convince spread of their
# friends to take the following offering of the course.
# recruited friends are unique, so there is no duplication among the newly
# recruited students. Define a procedure, users_to_ipo(n, spread,
# target), that takes three inputs: the starting number of users, the spread
# rate (how many new friends each Udacian convinces to join each cycle),
# and the target number, and outputs the number of cycles needed to reach 
# (or exceed) the target.

# For credit, your procedure must not use: while, for, or import math. 

def users_to_ipo(n, spread, target):
    if n >= target:
        return 0
    else:
        return 1 + users_to_ipo(n * (1 + spread), spread, target)
           
        
# 0 more needed, since n already exceeds target
print users_to_ipo(100000, 2, 36230) 
#>>> 0

# print users_to_ipo(100, 2, 5000000) 
# print users_to_ipo(100, 2, 70000000) 
# print users_to_ipo(100, 2, 7 * 10 ** 7) 
print users_to_ipo(100, 0.01, 5000000) 
print users_to_ipo(100, 0.1, 5000000) 
print users_to_ipo(100, 1.0, 5000000) 
print users_to_ipo(100, 10.0, 5000000) 

# after 1 cycle, there will be 100+ (100 * 2) users
# print users_to_ipo(1000, 2, 3000) 
# #>>> 1
# 
# need to match or exceed the target
# print users_to_ipo(50000, 2, 150001)
# #>>> 2 
# 
# only 13 months to exceed the current population of 7b!
# print users_to_ipo(100, 2, 7 * 10 ** 7) 
# #>>> 
# 
# more friends means faster world domination!
# print users_to_ipo(15000, 3, 7 * 10 ** 7)
# #>>> 
# 
# print users_to_ipo(100, 2, 10 ** 5) 
# print users_to_ipo(100, 2, 5000000) 
