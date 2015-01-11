# Question 2. Triangular Numbers

# The triangular numbers are the numbers 1, 3, 6, 10, 15, 21, ...
# They are calculated as follows.

# 1
# 1 + 2 = 3
# 1 + 2 + 3 = 6
# 1 + 2 + 3 + 4 = 10
# 1 + 2 + 3 + 4 + 5 = 15

# Write a procedure, triangular, that takes as its input a positive
# integer n and returns the nth triangular number.

#def triangular(n):
#    for i in range(n):
#        return [i*(i+1)/2]

def triangular(n):
    for i in n:
        return i*(i+1)/2
    

#for i in n:
#    return [i*(i+1)/2]
#
#    return [i*(i+1)/2 for i in xrange(n)]
#    previous = 0
#    current = 1
#    while n:
        

#    current = 0
#    after = current + 1
#    for i in range(0, n):
#        current, after = after, current + after
#    return current


print triangular(1)
#>>>1

print triangular(3)
#>>> 6

print triangular(10)
#>>> 55

print triangular(2)
