# Finds href of supplements

import os
from os import path
from bs4 import BeautifulSoup as bsp
import urllib as ul
import json

# This could have been anywhere on acq.gov
srch = 'https://www.acquisition.gov/dears/part-970%E2%80%94doe-management-and-operating-contracts'
# Open the url and save it as an html object
resp = ul.request.urlopen(srch)
html_res = resp.read()
# Turn it into html and parse out the content
soup = bsp(html_res, 'html.parser')
rt = soup.find('div', class_ = 'reg-container clearfix')
rt = rt.find_all('a')

# Load file
# Remove all its contents before writing anything, but only if it exists
jname = os.path.basename(__file__).split('.')[0]
jname = 'json/' + jname + '.json'
if path.exists(jname): open(jname, 'w').close()

with open(jname, 'w', encoding = 'utf8') as jf:
  jf.write('[')
  # Take-out the attributes
  for i in rt:
    reg_abb = i.get_text()
    reg_abb = reg_abb.strip()
    reg_name = i.attrs['href']
    reg_name = reg_name.strip()
    # Create dictionary to start adding values
    d = {
         'reg': reg_abb,
         'href': reg_name
        }
    json.dump(d, jf, indent = 2)
  # Add closing bracket to signify the end
  jf.write(']')

# Convert all dictionaries to strings, then add commas inbetween each object
# Then, overwrite old file with new changes as a list of strings
with open(jname, 'r') as jf:
  contents = jf.read()
  contents = contents.replace('}{', '},{')
with open(jname, 'w', encoding = 'utf8') as jf:
  jf.write(contents)

# Finally, reconvert the file back to a json file
with open(jname, 'r') as jf:
  contents = json.load(jf)
with open(jname, 'w', encoding = 'utf8') as jf:
  json.dump(contents, jf, indent = 2)

print('Finished pushing data to ' + jname)


