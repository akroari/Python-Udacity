def main():
	print "This program calculates the future value of a 10-year investment."
	
	principal = input("Enter the initial principal: ") 
	apr = input("Enter the annualized interest rate: ")
	for i in range(10):
		principal = principal * (1 + apr)
	
print "The amount in 10 years is:", principal 

main()