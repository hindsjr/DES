
#importing things needed
import numpy as np
import os.path
from posixpath import basename, dirname
import pandas as pd
from urlparse import urlparse

#I will use this later - determining RA
#for i in range(0,M-1):
#    ra=i*(360./M),
#    print("RA: ", ra)

#not sure what I'm doing with this yet
#def func(prodcell, subcell): #function that accepts the projection cell and subcell

#    return prodcell
#    return subcell
#    print("Projection Cell: ", prodcell)
#    print("Subcell: ", subcell)

for PC,SC in range(635,2008), range(1,100):
#    repos = np.DataSource()
#    repos.exists('http://ps1images.stsci.edu/cgi-bin/ps1filenames.py?skycell=PC.SC)
#                 True

    a = pd.read_table("http://ps1images.stsci.edu/cgi-bin/ps1filenames.py?skycell=1405.053")





#not sure if this reads the file or just downloads to /Documents/panstarrs/data
#    ds = DataSource('/Documents/panstarrs/data')
#    urlname = 'http://ps1images.stsci.edu/cgi-bin/ps1filenames.py?skycell=PC.SC'
#    gfile = ds.open('http://ps1images.stsci.edu/cgi-bin/ps1filenames.py?skycell=PC.SC')  # remote file
#    ds.abspath(urlname)

    path = urlparse.urlparse('http://ps1images.stsci.edu/cgi-bin/ps1filenames.py?skycell=PC.SC').path   
        print path

def urlfunc(): #this will need to go in the loop
    url = 'http://ps1images.stsci.edu/cgi-bin/ps1filenames.py?skycell=PC.SC'
    parse_object = urlparse(url)
    a = dirname(parse_object.path) #so will this return ps1filenames.py?skycell=PC.SC? Because we just want PC and SC
    return a 


    os.path.split(path)


#not sure if these will work
#    url = np.DataSource.open(destpath="http://ps1images.stsci.edu/cgi-bin/ps1filenames.py?skycell=PC.SC")

#def analyze(filename):
    #data = np.loadtxt(http://ps1images.stsci.edu/cgi-bin/ps1filenames.py?skycell=1405.053,
