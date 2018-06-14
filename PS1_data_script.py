#Sample python scripts for downloading PS1 data: https://archive.stsci.edu/vo/python_examples.html

#!/usr/local/bin/python

# change above line to point to local 
# python executable

import urllib, urlparse, string, time
 

# create URL with desired search parameters

url = "http://archive.stsci.edu/pointings/search.php?"
url = url + "primary=ACS&outputformat=CSV"
url = url + "&pnt_ucountp=%3C5&pnt_icountp=%3E1&bao=and"
url = url + "&galactic=Above&galsearch=75"
url = url + "&action=Search+Exposures"

print url

# retrieve URL and  write results to filename

filename = "out_py.txt"

urllib.urlretrieve(url,filename)

### Done!
