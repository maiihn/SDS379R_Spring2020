#!/usr/bin/env python3

import os
import numpy as np
import export
from sys import argv

if len(argv) != 3 or '-h' in argv:
    print('Use: <script> <method flag> <state number>')
    print('<method flag> \n \t \t -rs    :  random searching \n \t \t -kdb   :  only kdb \n \t \t -both  :  kdb + random searching \n \t \t -all   :  all 3 methods')
    exit()
elif len(argv) == 3:
    if argv[1] not in ['-rs','-kdb','-both','-all']:
        print('Invalid method')
        print('Use flag \n \t \t -rs    :  random searching \n \t \t -kdb   :  only kdb \n \t \t -both  :  kdb + random searching')
        exit()
    else:
        num_state = int(argv[2])

    if argv[1] != '-all':
        method = argv[1]

        path = export.Method()
        pathway = path.get_method(method)


        for i in range(num_state):
    
            state = i
            thepath = '/home/maiihn/code/eon/calculation/pt-system/newtest/one_pentamer/' + str(state) + '/' + str(pathway) + '/states/'
            thenewpath = '/home/maiihn/code/eon/calculation/pt-system/newtest/one_pentamer/OUTPUT/' + str(pathway) + '/result'

    
            path = thepath + str(0)
            newpath = thenewpath + str(state) 
            num_saddle = export.Number(path).get_num_saddle()
    
            doc = export.Doc(path)
            doc.export_saddle_data(newpath,num_saddle)

        print('The csv of saddle info for', pathway, 'has been exported in the OUTPUT directory.')


    else:
        method_lst = ['-rs','-kdb','-both']
        for m in method_lst:
            method = m
            
            path = export.Method()
            pathway = path.get_method(method)

            for i in range(num_state):
    
                state = i
                thepath = '/home/maiihn/code/eon/calculation/pt-system/newtest/one_pentamer/' + str(state) + '/' + str(pathway) + '/states/'
                thenewpath = '/home/maiihn/code/eon/calculation/pt-system/newtest/one_pentamer/OUTPUT/' + str(pathway) + '/result'
                
                path = thepath + str(0)
                newpath = thenewpath + str(state)
                num_saddle = export.Number(path).get_num_saddle()
                
                doc = export.Doc(path)
                doc.export_saddle_data(newpath,num_saddle)

        print('The csv of saddle info has been exported in the OUTPUT directory.')

