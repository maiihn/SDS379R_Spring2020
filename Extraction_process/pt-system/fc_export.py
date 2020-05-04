#!/usr/bin/env python3

import os
import numpy as np
import export
from sys import argv

if len(argv) != 2 or '-h' in argv:
    print('Use flag \n \t \t -rs    :  random searching \n \t \t -kdb   :  only kdb \n \t \t -both  :  kdb + random searching')
    exit()
elif len(argv) == 2:
    if argv[1] not in ['-rs','-kdb','-both']:
        print('Invalid method')
        print('Use flag \n \t \t -rs    :  random searching \n \t \t -kdb   :  only kdb \n \t \t -both  :  kdb + random searching')
        exit()
    else:
        method = argv[1]

path = export.Method('akmc-pt-')
pathway = path.get_method(method)

thepath = '/home/maiihn/code/eon/calculation/pt-system/' + pathway + '/states/'
thenewpath = '/home/maiihn/code/eon/calculation/pt-system/OUTPUT/' + pathway + '/force_call' + '/result_state'
num_state = export.Number(thepath).get_num_state() - 1

for i in range(num_state):
    state = i
    
    path = thepath + str(state) 
    newpath = thenewpath + str(state) 
    num_saddle = export.Number(path).get_num_saddle()
    
    doc = export.Doc(path)
    doc.export_forcecall(newpath,num_saddle)

# do the sums for force calls
path = thepath
newpath = '/home/maiihn/code/eon/calculation/pt-system/OUTPUT/' + pathway + '/force_call' + '/state_result'
doc = export.Doc(path)
doc.export_sum_forcecall(newpath,num_state)


print('The csv of the force calls in', num_state, 'states for', pathway, 'has been exported in the OUTPUT directory.')

