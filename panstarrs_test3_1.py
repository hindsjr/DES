import numpy as np

#changes each column to an array
b_dec = np.genfromtxt("out_py_3",unpack=True, usecols=(1,2,3,4))
f_filter1 = np.genfromtxt("out_py_3",unpack=True, usecols=(5), dtype='str')
a = np.genfromtxt("out_py_3",unpack=True, usecols=(0), dtype='str')
c = np.genfromtxt("out_py_3",unpack=True, usecols=(2), dtype='str')
d = np.genfromtxt("out_py_3",unpack=True, usecols=(3), dtype='str')
e = np.genfromtxt("out_py_3",unpack=True, usecols=(4), dtype='str')
b = np.genfromtxt("out_py_3",unpack=True, usecols=(1))

#fixes the outputs so it can be used for DECam
for n, i in enumerate(f_filter1):
    if i == 'u':
        f_filter1[n] = 0
    if i == 'g':
        f_filter1[n] = 1
    if i == 'r':
        f_filter1[n] = 2
    if i == 'i':
        f_filter1[n] = 3
    if i == 'z':
        f_filter1[n] = 4
    if i == 'y':
        f_filter1[n] = 5
#changes all the arrays back to columns
filterdata = np.array([f_filter1]).T
decdata = np.array([b_dec]).T
adata = np.array([a]).T
bdata = np.array([b]).T
cdata = np.array([c]).T
ddata = np.array([d]).T
edata = np.array([e]).T

#puts the columns in a table format
g = np.column_stack((adata,bdata,cdata,ddata,edata,filterdata))

#saves table to a new folder f
fn = 'f'
with open(fn, 'w+') as f: 
    np.savetxt(f, g, fmt='%s', delimiter=' ')


