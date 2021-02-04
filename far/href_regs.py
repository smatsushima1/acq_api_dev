# Finds href of supplements

import os
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
jname = os.path.basename(__file__).split('.')[0] + '.json'
open(jname, 'w').close()
jfile = open(jname, 'a', encoding = 'utf8')
jfile.write('[')

# Take-out the attributes
for i in rt:
  reg_abb = i.get_text()
  reg_abb = reg_abb.strip()
  reg_name = i.attrs['href']
  reg_name = reg_name.strip()
  
  d = {
       'reg': reg_abb,
       'href': reg_name
      }
  json.dump(d, jfile, indent = 2)
  
# Add closing bracket to signify the end
jfile.write(']')
jfile.close()

# Add commas inbetween each object
jfile = open(jname, 'r')
contents = jfile.read()
contents = contents.replace('}{', '},{')
jfile.close()

# Overwrite old file with new changes
jfile = open(jname, 'w')
jfile.write(contents)

print('Finished pushing data')



      
      
      
      
      
      