
#importing things needed
import numpy as np
import urlparse
import os.path

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

for p,c in range(635,2008), range(1,100):
    repos = np.DataSource()
    repos.exists('http://ps1images.stsci.edu/cgi-bin/ps1filenames.py?skycell=p.c)
                 True

#not sure if this reads the file or just downloads to /Documents/panstarrs/data
#    ds = DataSource('/Documents/panstarrs/data')
#    urlname = 'http://ps1images.stsci.edu/cgi-bin/ps1filenames.py?skycell=p.c'
#    gfile = ds.open('http://ps1images.stsci.edu/cgi-bin/ps1filenames.py?skycell=p.c')  # remote file
#    ds.abspath(urlname)

    path = urlparse.urlparse('http://ps1images.stsci.edu/cgi-bin/ps1filenames.py?skycell=p.c').path   
    print path

    os.path.split(path)


#not sure if these will work
#    url = np.DataSource.open(destpath="http://ps1images.stsci.edu/cgi-bin/ps1filenames.py?skycell=p.c")

#def analyze(filename):
    #data = np.loadtxt(http://ps1images.stsci.edu/cgi-bin/ps1filenames.py?skycell=1405.053,
