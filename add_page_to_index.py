# Define a procedure, add_page_to_index,
# that takes three inputs:
#   - index
#   - url (String)
#   - content (String)
# It should update the index to include
# all of the word occurences found in the
# page content by adding the url to the
# word's associated url list.

index = []

def add_to_index(index,keyword,url):
    for entry in index:
        if entry[0] == keyword:
            entry[1].append(url)
            return
    index.append([keyword,[url]])

def add_page_to_index(index,url,content):
	words = content.split()
	for word in words:
		add_to_index(index, word, url)


#add_page_to_index(index,'http://dilbert.com',"fake")
add_page_to_index(index,'http://www.certifiedhumane.org/index.php?page=restaurant-list',"visit")

print index
#>>> [['This', ['fake.text']], ['is', ['fake.text']], ['a', ['fake.text']],
#>>> ['test',['fake.text']]]


