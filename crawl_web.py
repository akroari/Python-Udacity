def crawl_web(seed):
	tocrawl = [seed]
	crawled = []
		while tocrawl:
			page = tocrawl.pop()