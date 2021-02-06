# Start extracting links to the Parts and save href in json file

import os
from os import path
import json
from bs4 import BeautifulSoup as bsp
import urllib as ul
import re

###############################################################################
# Functions

# Return html text
def ret_href(addr):
  # Open the url and save it as an html object
  srch1 = 'https://www.acquisition.gov'
  srch2 = srch1 + addr
  resp = ul.request.urlopen(srch2)
  html_res = resp.read()
  soup = bsp(html_res, 'html.parser')
  
  # Start writing to html file
  with open(hname, 'a', encoding = 'utf8') as hf:
    lbr = '<br>'
    hf.write(lbr * 5 + addr)
  
    # Add before adding everything else
    # Square brackets = array of objects (list)
    # Curly brackets = object
    reg_num = addr.strip('/')
    jf.write('"' + reg_num + '"' + ': [')
  
    # Finding this div applies to FAR, DFARS, and GSAM
    # It would be 0 if this id wasn't even on the page
    htxt = soup.find('div', id = 'parts-wrapper')
    if htxt is not None:
      htxt = htxt.div
    else:
      htxt = soup.tbody
    hf.write(str(htxt.prettify()))
    
  # Then get a list of all the a's, which has our information
  htxt = htxt.find_all('a')
  for j in htxt:
    # The part numbers will always just be the text
    # Concatenate and complete the href
    hpart = ret_part(j.get_text())
    href = srch1 + j.attrs['href']
    d = {
         # Figure out how to change to int
         'part': hpart,
         'href': href,
         'html_text': 'N/A'
        }
    json.dump(d, jf, indent = 2)
  
  # Close the bracket  
  jf.write(']')

# Returns the part number regardless of what type it is
def ret_part(txt):
  txt_sp = txt.split()
  cnt = len(txt_sp)
  if cnt > 1:
    txt = txt_sp[cnt - 1]
  return txt
  
###############################################################################

# Load file
# Remove all its contents before writing anything, but only if it exists
jname = os.path.basename(__file__).split('.')[0]
jname = 'json/' + jname + '.json'
if path.exists(jname): open(jname, 'w').close()

# write html for each section just to get an idea of each structure
hname = os.path.basename(__file__).split('.')[0]
hname = 'html/' + hname + '.html'
if path.exists(hname): open(hname, 'w').close()

# Save all data from hrefs and regs into dictionary to loop through
jname2 = 'json/02_href_regs.json'
with open(jname2) as jf2:
  data = json.load(jf2)

# File will open here to start being added to
# Won't close until all the regs have been looped through
with open(jname, 'w', encoding = 'utf8') as jf:
  jf.write('{')  
  for i in data:
    reg = i['href']
    print(reg)
    ret_href(str(reg))

  jf.write('}')

# Convert all dictionaries to strings, then add commas inbetween each object
# Then, overwrite old file with new changes as a list of strings
with open(jname, 'r') as jf:
  contents = jf.read()
  contents = contents.replace('}{', '},{')
with open(jname, 'w', encoding = 'utf8') as jf:
  jf.write(contents)

# Finally, reconvert the file back to json
with open(jname, 'r') as jf:
  contents = json.load(jf)
with open(jname, 'w', encoding = 'utf8') as jf:
  json.dump(contents, jf, indent = 2)

print('Finished pushing data to ' + jname)  

  




  #print(html_contents)
  

  #rt = rt.find_all('a')

























#   # Add closing bracket to signify the end
#   jf.write(']')

















# open the url and save it as an html object
# resp = ul.request.urlopen(res)
# html_res = resp.read()

# turn it into html and parse out the content
# text is always found in the <div id="middlecontent"> area on the webpage
# soup = bsp(html_res, 'html.parser')
# reg_txt = soup.find('div', id = 'middlecontent')

# with open(hfile, 'w', encoding = 'utf8') as h:
#   h.write(reg_txt.prettify())
#   h.close()

#print(reg_txt.prettify())
# look into .extrar() for beautiful soup to extract contents in between tags
# changin the names of tags and attributes





# reg
# part
# subpart
# section
# http_link
# html







