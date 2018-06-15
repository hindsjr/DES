#test file #2

#This works for a single PC and SC
import urllib, urlparse, string, time
url = "http://ps1images.stsci.edu/cgi-bin/ps1filenames.py?skycell=1405.053"
print url
filename = "out_py.txt"
urllib.urlretrieve(url,filename)

#but this gets an error message: "too many values to unpack" when put in a forloop
#for PC,SC in range(635,2008), range(1,100):
#    url = "http://ps1images.stsci.edu/cgi-bin/ps1filenames.py?skycell=PC.SC"
#    print url
#    filename = "ps1images.stsci.edu/cgi-bin/ps1filenames.py?skycell=PC.SC.txt"
#    urllib.urlretrieve(url,filename)
