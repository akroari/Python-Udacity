# Write Python code that assigns to the 
# variable url a string that is the value 
# of the first URL that appears in a link 
# tag in the string page.

# page = contents of a web page
page =('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://www.xkcd.com">')

# find the location of the first link on the page
start_link_location = page.find('<a href=')
end_link_location = page.find("/>", start_link_location)

url_length = start_link_location - end_link_location
print url_length

url = page[89:179]
print url
