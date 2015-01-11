# Modify the crawl_web procedure so that instead of just returning the 
# index, it returns an index and a graph. The graph should be a 
# Dictionary where the key:value entries are:

#  url: [list of pages url links to] 

def crawl_web(seed): # returns index, graph of outlinks
    tocrawl = [seed]
    crawled = []
    graph = {}  # <url>:[list of pages it links to]
    index = {} 
    while tocrawl: 
        page = tocrawl.pop()
        if page not in crawled:
            content = get_page(page)
            add_page_to_index(index, page, content)
            outlinks = get_all_links(content)
            graph[page] = outlinks
            union(tocrawl, outlinks)
            crawled.append(page)
    return index, graph
    
index, graph = crawl_web('http://cs101.udacity.com/urank/index.html')
print graph['http://cs101.udacity.com/urank/index.html']