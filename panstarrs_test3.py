#importing everything
import numpy as np
import os.path
from posixpath import basename, dirname
import pandas as pd
from urlparse import urlparse
import csv
import urllib, urlparse, string, time
import collections

#copied this from Jupyter Notebook: PanSTARRS_imaging_script so we'll see if it works here too
filename = "out_py.txt"
for PC, SC in zip(range(1405,1410), range(53,59)):
    url = "http://ps1images.stsci.edu/cgi-bin/ps1filenames.py?skycell=" + str(PC) + "." + str(SC)
    print url
    print PC
    print SC
    with open(filename, 'a') as f: 
            a = pd.read_table(url)
            b = str(a)
            f.write(b)
            f.write('\n')
