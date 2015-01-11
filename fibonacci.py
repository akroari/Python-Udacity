# Define a procedure, fibonacci, that takes a natural number as its input, and
# returns the value of that fibonacci number.

# Two Base Cases:
#    fibonacci(0) => 0
#    fibonacci(1) => 1

# Recursive Case:
#    n > 1 : fibonacci(n) => fibonacci(n-1) + fibonacci(n-2)

# recursive fibonacci definition
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-2) + fibonacci(n-1)
        
#faster fibonacci
def fibonacci(n):
    current = 0
    after = 1
    for i in range(0,n):
        current, after = after, current + after
    return current

#how long until mass of rabbits exceeds mass of earth?
mass_of_earth = 5.9722 * 10**24 # in kilos
mass_of_rabbit = 2              # 2 kg per rabbits

n = 1
while fibonacci(n)*mass_of_rabbit < mass_of_earth:
    n = n + 1
print n, fibonacci(n)

# now if rabbits die after 5 months
def rabbits(n):
    if n < 1: #base case
        return 0
    else:
        if n == 1 or n == 2:
            return 1
        else:
            return rabbits(n-1) + rabbits(n-2) - rabbits(n-5)

def hexes_to_udaciousness(n, spread, target):
    if n >= target:
        return 0
    else:
        return 1 + hexes_to_udaciousness(n * (1 + spread), spread, target)

print fibonacci(4)
#>>> 1
print fibonacci(2)
#>>> 2
print fibonacci(3)
#>>> 2
print fibonacci(36)
#>>>