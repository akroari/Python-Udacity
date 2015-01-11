def compute_ranks(graph):
	d = 0.8 # damping factor. 
	numloops = 10 # experiment with changing this
	
	ranks = {} #empty dictionary
	npages = len(graph) #num nodes in graph
	for page in graph:
		ranks[page] = 1.0 / npages
	
	for i in range(0, numloops):
		newranks = {}
		for page in graph:
			newrank = (1 - d) / npages
			for node in graph:
				if page in graph[node]:
					newrank = newrank + d * (ranks[node] / len(graph[node])
			newranks[page] = newrank 
		ranks = newranks
	return ranks
		
index, graph = crawl_web(http://cs101.udacity.com/urank/index.html')
ranks = compute_ranks(graph)
print ranks