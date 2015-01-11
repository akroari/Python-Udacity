# define an algo that inserts a card, j into a sequence, A.
# once inserted, loop through the cards until they are sorted in non-desc order

def insertion_sort():
	mylist = [8, 2, 4, 9, 3, 6]
	for j in range(1, len(mylist)):
		key = mylist[j]
		i = j
		while i > 0 and key < mylist[i-1]:
			mylist[i] = mylist[i-1]
			i -= 1
			mylist[i] = key
			
print insertion_sort(5)
		
	