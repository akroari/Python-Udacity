# Define a procedure, total_enrollment,
# that takes as an input a list of elements,
# where each element is a list containing
# three elements: a university name,
# the total number of students enrolled,
# and the annual tuition fees.

# The procedure should return two numbers,
# not a string, 
# giving the total number of students
# enrolled at all of the universities
# in the list, and the total tuition fees
# (which is the sum of the number
# of students enrolled times the
# tuition fees for each university).

# define a procedure, called traffic, that takes as input 
# a list and returns as output three numbers providing the 
# total number of page views, unique visitors
# and page views per visitor. 
# For now we will not worry about sig figs.

list_1 = [['site',4500,25000]]

list_2 = [ ['site1',2175,37704],
              ['site2',19627,39849],
              ['site3',10566,40732],
              ['site4',7802,37000],
              ['site5',5879,35551],
              ['site6',19535,40569],
              ['site7',11701,40500]  ]

def total_traffic(p):
	total_unique_visitors = 0
	total_page_views = 0
	for site, unique_visitors, page_views in p:
		total_unique_visitors = total_unique_visitors + unique_visitors
		total_page_views = total_page_views + page_views
		pv_uv = total_page_views / total_unique_visitors
	return total_unique_visitors, total_page_views, pv_uv
	
print total_traffic(list_1)
#>>> (4500, 25000, 5)
print total_traffic(list_2)
#>>> (77285, 271905, 3)


# The L is automatically added by Python to indicate a long
# number. If you are trying the question in an outside 
# interpreter you might not see it.

#print total_traffic(list_2)
#>>> (77285,3058581079L)
    
