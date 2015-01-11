# Given the variable countries defined as:

#             Name      Capital  Populations (millions)
countries = [['China','Beijing',1350],
             ['India','Delhi',1210],
             ['Romania','Bucharest',21],
             ['United States','Washington',307]]

# What multiple of Romania's population is the population
# of China? Please print your result.

China_pop = countries[0][2]
Romania_pop = countries[2][2]
China_multiple = China_pop / Romania_pop

#print China_pop
#print Romania_pop
print China_multiple

