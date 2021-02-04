from googlesearch import search

far_parts = list(range(1, 53))

for i in far_parts:
  srch_acq = 'https://www.acquisition.gov/'
  srch_reg = 'far'
  srch_part = str(i)
  srch_str = srch_acq + srch_reg + ' Part ' + srch_part

  srch_res = search(srch_str)
  for j in srch_res:
    res = str(j)
    if srch_part in res:
      print(res)
      break

# far, dfars, dfarspgi, gsam
# try searching for the index/far and then go to div class = "clearfix" to 
# display all the links. use bsp to search for a tags and loop through all the
# div ids

# afars, affars
# search for tbody and then hrefs in there
# div id = regulation-index-browse_wrapper




  
