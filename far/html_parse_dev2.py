from bs4 import BeautifulSoup as bsp
from googlesearch import search
import urllib as ul

# delete file
hfile = '317_all.html'
open(hfile, 'w').close()

str_acq = 'https://www.acquisition.gov/'
str_reg = 'hhsar'
str_part = '317'
str_srch = str_acq + str_reg + ' ' + str_part

# only give the first search result and save it as a string
# if google can't find it, no one can - there's no use in seaching beyond 1
srch_res = search(str_srch, num = 1, stop = 1)
for i in srch_res:
  res = str(i)

# open the url and save it as an html object
resp = ul.request.urlopen(res)
html_res = resp.read()

# turn it into html and parse out the content
# text is always found in the <div id="middlecontent"> area on the webpage
soup = bsp(html_res, 'html.parser')
reg_txt = soup.find('div', id = 'middlecontent')

with open(hfile, 'w', encoding = 'utf8') as h:
  h.write(reg_txt.prettify())
  h.close()

#print(reg_txt.prettify())
# look into .extrar() for beautiful soup to extract contents in between tags
# changin the names of tags and attributes





# reg
# part
# subpart
# section
# http_link
# html







