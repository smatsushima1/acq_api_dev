# Clean-up first two json files

import json

# Start with 01_far_parts.json
jname = 'json/01_far_parts.json'
with open(jname) as jf:
  data = json.load(jf)

  for i in data:
    # Replace original 'RESERVED' string to just one word
    if 'RESERVED' in i['name']:
      i['name'] = 'RESERVED'
  # Save over the old data
  data = data

# Overwrire old data to new data
with open(jname, 'w', encoding = 'utf8') as jf:
  json.dump(data, jf, indent = 2)

print("Fished updating " + jname)

# Move on to 02_href_regs.json
jname = 'json/02_href_regs.json'
with open(jname) as jf:
  data = json.load(jf)

  for i in data:
    reg = i['reg']
    href = i['href']
    hrefc = href.count('/')
    # Remove objects that are not a regulation
    if 'Smart' in reg:
      data.remove(i)
    # Parse-out the regulation and convert to the real path
    elif hrefc > 1:
      hrefs = href.split('/')
      hrefsc = len(hrefs)
      href = '/' + hrefs[hrefsc - 1]
      i['href'] = href
  # Save over the old data
  data = data

with open(jname, 'w', encoding = 'utf8') as jf:
  json.dump(data, jf, indent = 2)

print("Fished updating " + jname)

  
