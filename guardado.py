# File       : diff_labels.py
# Author     : Rafael Estevez
# Company    : A2e technologies
# Created    : 16/03/2021
# -----------------------------------------------------------------------------
# Description: a script that analyzes the te output of git-diff and returns based on a files.md_FPGA of labels the corresponding label  
# -------------------------------------------------------------

import os.path as path
import argparse
import git
import re
import subprocess
from git import Repo
import json


parser = argparse.ArgumentParser(description='a tool to obtain the git diff and use the information to get a label depending on the changed files')
parser.add_argument('-bb','--branch_base',  type=str, default="",
                    help='branch_base.')
parser.add_argument('-ic','--id_commit', type=str,default="",
                    help="Id of the commit")
#The argument that will take from the pipeline will be the name of the base branch and the commit id 

def main():
    args = parser.parse_args()
    edited_lines(args.branch_base, args.id_commit)

def edited_lines(basebr,idcommit):
    label_fromsjson = []
    Openjson = open("labels.json", "r")
    data_json= json.loads(Openjson.read())
    print(data_json[2])
    for i in data_json['labels']: 
       label_fromsjson.append(i)
    repo = Repo()
    d= repo.git.diff(basebr, idcommit) 
    diff_lines= d.split('\n')
    found_first = False
    # adjust for added lines
    adjust = 0
    # how many lines since the start
    count_of_lines_edited = 0
    number_lines_edited_onSWmax = 0
    number_lines_edited_onSW = 0
    number_lines_edited_onFPGA = 0
    count_of_lines_edited_on_fpga= 0
    count_of_lines_edited_on_sw= 0
    sw = "sw/"
    fpga = "fpga/"    
    for line in diff_lines:
        if line.startswith('+++'):
            count_of_lines_edited = count_of_lines_edited + 1
            
            if fpga in line: 
                if not line.endswith(".md"):
                     a=str(label_fromsjson[6])                    
                     a=(a.replace('}', ''))
                     a=(a.replace('{', ''))
                     a= a.replace("'", "")
                     print(a)
            if sw in line: 
                if not line.endswith(".md"):
                     h=str(label_fromsjson[7])
                     h=(h.replace('}', ''))
                     h=(h.replace('{', ''))
                     h= h.replace("'", "")
                     print(h)     
    #this is an iteration of every line of the git diff and it will look for all the lines that start with a "+++" this would help to count the files edited 
                
    
    for lines in diff_lines:
        if lines.startswith('+'):
            number_lines_edited_onSW += 1
        if lines.startswith('-'):
            number_lines_edited_onFPGA+= 1
    #Here the for would help to count all the lines that were edited, and bellow the lines founded with +++ will rest, to count only the lines changed  
 
    number_lines_edited_onSW = number_lines_edited_onSW - count_of_lines_edited
    numbf = number_lines_edited_onFPGA -count_of_lines_edited
    number_lines_edited_onSWmax = number_lines_edited_onSW + number_lines_edited_onFPGA
    if count_of_lines_edited <= 1:
        b=str(label_fromsjson[0])
        b=(b.replace('}', ''))
        b=(b.replace('{', ''))
        b= b.replace("'", "")
        print(b)        
    if (count_of_lines_edited >= 1 and count_of_lines_edited <= 5 and number_lines_edited_onSWmax > 5) :
        c=str(label_fromsjson[1])
        c=(c.replace('}', ''))
        c=(c.replace('{', ''))
        c= c.replace("'", "")
        print(c)  
    if count_of_lines_edited >=5  and count_of_lines_edited < 30:
        d=str(label_fromsjson[2])
        d=(d.replace('}', ''))
        d=(d.replace('{', ''))
        d= d.replace("'", "")
        print (d)  
    if count_of_lines_edited >= 30 and count_of_lines_edited < 50:
        e=str(label_fromsjson[3])
        e=(e.replace('}', ''))
        e=(e.replace('{', ''))
        e= e.replace("'", "")
        print(e)  
    if count_of_lines_edited >= 30 and count_of_lines_edited < 50:
        f=str(label_fromsjson[4])
        f=(f.replace('}', ''))
        f=(f.replace('{', ''))
        f= f.replace("'", "")
        print(f)  
    if count_of_lines_edited >= 50:
        g=str(label_fromsjson[5])
        g=(g.replace('}', ''))
        g=(g.replace('{', ''))
        g= g.replace("'", "")
        print(g)  
    
    






if __name__ == "__main__":
 main()

