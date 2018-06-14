
#importing things needed
import numpy as np
from urllib.parse import urlparse
import os.path
from posixpath import basename, dirname

#I will use this later
#for i in range(0,M-1):
#    ra=i*(360./M),
#    print(ra)

#not sure what I'm doing with this yet
#def func(prodcell, subcell): #function that accepts the projection cell and subcell

#    return prodcell
#    return subcell
#    print("Projection Cell: ", prodcell)
#    print("Subcell: ", subcell)

for p,s in range(635,2008), range(1,100):
    repos = np.DataSource()
    repos.exists('http://ps1images.stsci.edu/cgi-bin/ps1filenames.py?skycell=p.s)
                 True

#not sure if this reads the file or just downloads to /Documents/panstarrs/data
#    ds = DataSource('/Documents/panstarrs/data')
#    urlname = 'http://ps1images.stsci.edu/cgi-bin/ps1filenames.py?skycell=p.s'
#    gfile = ds.open('http://ps1images.stsci.edu/cgi-bin/ps1filenames.py?skycell=p.s')  # remote file
#    ds.abspath(urlname)

    path = urlparse.urlparse('http://ps1images.stsci.edu/cgi-bin/ps1filenames.py?skycell=p.s').path   
        print path

def urlfunc(): #this will need to go in the loop
    url = 'http://ps1images.stsci.edu/cgi-bin/ps1filenames.py?skycell=p.s'
    parse_object = urlparse(url)
    a = dirname(parse_object.path) #so will this return ps1filenames.py?skycell=p.s? Because we just want p and s
    return a 


    os.path.split(path)


#not sure if these will work
#    url = np.DataSource.open(destpath="http://ps1images.stsci.edu/cgi-bin/ps1filenames.py?skycell=p.s")

#def analyze(filename):
    #data = np.loadtxt(http://ps1images.stsci.edu/cgi-bin/ps1filenames.py?skycell=1405.053,
