#importing everything
import pandas as pd

#use this to collect data from the url and write it to one output file
filename = "out_py.txt"
for PC in range(1405,1410):  #these ranges are only test ranges
    for SC in range(53,59):
        url = "http://ps1images.stsci.edu/cgi-bin/ps1filenames.py?skycell=" + str(PC) + "." + str(SC)
        print(url)
        print(PC)
        print(SC)
        with open(filename, 'a') as f: 
            a = pd.read_table(url)
            b = str(a)
            f.write(b)
            f.write('\n')
