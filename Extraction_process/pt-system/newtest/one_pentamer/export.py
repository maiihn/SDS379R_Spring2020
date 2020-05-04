import os
import numpy as np

class Method:
    def __init__(self):
        self.method = ''
    def get_method(self, method):
        if method == '-rs':
            method = 'ransearch'
        elif method == '-kdb':
            method = 'onlykdb'
        elif method == '-both':
            method = 'kdbransearch'
        return str(method)


class Doc:
    def __init__(self, path):
        self.path = path

    # write a csv for each method
    def export_saddle_data(self, newpath, num_saddle):
        thepath1 = self.path + '/processtable'
        doc1 = open(thepath1,'r')
        new_doc = open(newpath + '.csv', 'w')
        line = doc1.readline()
        new_doc.write('proc #,saddle energy,prefactor,product,product energy,product prefactor,barrier,rate,repeats,force call minimization,force call saddle\n')
        for num in range(num_saddle):
            line = doc1.readline()
            thepath2 = self.path + '/procdata/results_' + str(num) + '.dat'
            doc2 = open(thepath2,'r')
            for i in range(4):
                doc2.readline()
            min_fc = doc2.readline().split()[0]
            saddle_fc = doc2.readline().split()[0]
            line_s = line.split()
            new_line = ''
            for i in range(len(line_s)):
                new_line += line_s[i] + ','
            new_line += min_fc + ',' + saddle_fc + '\n'
            new_doc.write(new_line)
            doc2.close()
        doc1.close()
        new_doc.close()

    # write a csv for each state
    def export_forcecall(self, newpath, num_saddle):
        new_doc = open(newpath + '.csv', 'w')
        new_doc.write('force call minization,force call saddle\n')
        for num in range(num_saddle):
            thepath = self.path + '/procdata/results_' + str(num) + '.dat'
            doc = open(thepath,'r')
            for i in range(4):
                doc.readline()
            min_fc = doc.readline().split()[0]
            saddle_fc = doc.readline().split()[0]
            new_line = min_fc + ',' + saddle_fc + '\n'
            new_doc.write(new_line)
            doc.close()
        new_doc.close()

    # write a csv summing the force call for each state
    def export_sum_forcecall(self,newpath,num_state):
        new_doc = open(newpath + '.csv', 'w')
        new_doc.write('state,number of saddle,sum force call minimization,sum force call saddle,total force call,% force call minimization,% force call saddle\n')
        for n in range(num_state):
            sum_min = 0
            sum_saddle = 0
            pathw = self.path + str(n)
            num_saddle = Number(pathw).get_num_saddle()
            for num in range(num_saddle):
                thepath = pathw + '/procdata/results_' + str(num) + '.dat'
                doc = open(thepath,'r')
                for i in range(4):
                    doc.readline()
                min_fc = int(doc.readline().split()[0])
                saddle_fc = int(doc.readline().split()[0])
                sum_min += min_fc
                sum_saddle += saddle_fc
                doc.close()
            totalfc = sum_min + sum_saddle
            min_percent = sum_min*100/totalfc
            sad_percent = sum_saddle*100/totalfc
            new_line = str(n) + ',' + str(num_saddle) + ',' + str(sum_min) + ',' + str(sum_saddle) + ',' + str(totalfc) + ',' + str(min_percent) + ',' + str(sad_percent) + '\n'
            new_doc.write(new_line)
        new_doc.close()

    # export saddle info
    def export_state_saddle(self, newpath, numstate, method):
        new_doc = open(newpath + '.csv', 'w')
        new_doc.write('state,good saddles,bad saddles,total saddles,unique saddles,force call saddle\n')
        for i in range(numstate):
            doc = open(self.path + '/' + str(i) + '/' + method + '/states/0/info','r')
            line = doc.readline()
            line = doc.readline().split()
            while len(line) > 0:
                if line[0] == 'bad_saddles':
                    bad_s = line[-1]
                elif line[0] == 'good_saddles':
                    good_s = line[-1]
                elif line[0] == 'unique_saddles':
                    unique_s = line[-1]
                line = doc.readline().split()
            doc.close()
            sfc = 0
            for j in range(int(unique_s)):
                doc = open(self.path + '/' + str(i) + '/' + method + '/states/0/procdata/results_' + str(j) + '.dat','r')
                line = doc.readline()
                line = doc.readline().split()
                while len(line) > 0:
                    if line[-1] == 'force_calls_saddle':
                        sfc += int(line[0])
                    line = doc.readline().split()
                doc.close()
            total_s = int(bad_s) + int(good_s)
            new_line = str(i)+','+str(good_s)+','+str(bad_s) +','+str(total_s)+','+str(unique_s)+','+str(sfc) + '\n'
            new_doc.write(new_line)
            doc.close()
        new_doc.close()

    # write a csv for dynamics
    def export_dynamics(self, newpath):
        new_doc = open(newpath + '.csv', 'w')
        doc = open(self.path + '/dynamics.txt','r')
        line = doc.readline()
        line_s = line.split()
        new_line = ''
        for i in range(len(line_s)):
            if i != len(line_s) - 1:
                new_line += line_s[i] + ','
            else:
                new_line += line_s[i] + '\n'
        new_doc.write(new_line)
        line = doc.readline()
        line = doc.readline()
        while line != '':
            new_line = ''
            line_s = line.split()
            for i in range(len(line_s)):
                if i != len(line_s) - 1:
                    new_line += line_s[i] + ','
                else:
                    new_line += line_s[i] + '\n'
            new_doc.write(new_line)
            line = doc.readline()
        doc.close()
        new_doc.close()

class Number:
    def __init__(self,path):
        self.path = path

    # get the number of saddles in that state
    def get_num_saddle(self):
        self.path += '/info'
        doc = open(self.path,'r')
        line = doc.readline().split()
        signal = False
        while signal == False:
            if line[0] == 'unique_saddles':
                signal = True
            else:
                line = doc.readline().split()
        num_saddle = int(line[-1])
        return num_saddle

    # get the number of states
    def get_num_state(self):
        self.path += '/state_table'
        doc = open(self.path,'r')
        num_state = 0
        line = doc.readline()
        while line != '':
            num_state +=1
            line = doc.readline()
        return num_state

        

        


