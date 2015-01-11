# Define a procedure, lookup,
# that takes two inputs:
# - an index
# - keyword

# The procedure should return a list
# of the urls associated
# with the keyword. If the keyword
# is not in the index, the procedure
# should return an empty list.

index = [['corewheels', ['http://corewheelfitness.com', 'http://www.akrowheels.com']],
         ['computing', ['http://acm.org']]]

def lookup(index,keyword):
    for entry in index:
        if entry[0]==keyword:
            return entry[1]
        return []
        
print lookup(index,'corewheels')
#>>> ['http://corewheelfitness.com', 'http://www.akrowheels.com']
