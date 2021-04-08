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
parser.add_argument('-id','--id_commit', type=str,default="",
                    help="Id of the commit")
#These arguments  will be taken from the pipeline and they are the name of the base branch and the commit id 

def main():
    args = parser.parse_args()
    edited_lines(args.branch_base, args.id_commit)

def edited_lines(basebr,idcommit):
    label_fromsjson = []
    Openjson = open("labels.json", "r")
    data_json= json.loads(Openjson.read())    
    for i in data_json['labels']: 
       label_fromsjson.append(i)
    repo = Repo()
    d= repo.git.diff(basebr, idcommit) 
    diff_lines= d.split('\n')
    found_first = False
    count_of_files_edited = 0
    count_of_files_edited_addmax = 0
    count_of_files_edited_add = 0
    number_directory_changed= 0
    sw = "sw/"
    fpga = "fpga/"
    
    count = len(data_json['labels'])
    a= data_json['labels'][count -1]['linesChanged']
    Biggestsvalue = data_json['labels'][count -2]['FilesChanged'].split("-")             
    Biggestsvalue =[int(i) for i in Biggestsvalue]
    Minorvalue= data_json['labels'][0]['linesChanged'].split("-")
    Minorvalue = [int(i) for i in Minorvalue]
    for lines in diff_lines:

        if (lines.startswith('+') or lines.startswith('-')):
            count_of_files_edited_add += 1
        if lines.startswith('+++ '):
            count_of_files_edited+= 1
        if (lines.startswith('----') or lines.startswith('+---') or lines.startswith('-+++') or lines.startswith('++++')):
            number_directory_changed+=1

            
    #Here the for would help to count all the lines that were edited, and bellow the lines founded with +++ will rest, to count only the lines changed  
 
    count_of_files_edited_add =  count_of_files_edited + number_directory_changed
    count_of_lines_edited_addmax = count_of_files_edited_add-count_of_files_edited - number_directory_changed   
    
 
    for x in range(count) :
        
        if ((data_json['labels'][x]['linesChanged'])!= a and count_of_files_edited_add == (min(Minorvalue))):
            data_json['labels'][x]['linesChanged']= data_json['labels'][x]['linesChanged'].split("-")
            data_json['labels'][x]['linesChanged']= [int(i) for i in data_json['labels'][x]['linesChanged']]
            if ((min(data_json['labels'][x]['linesChanged'])) <= count_of_lines_edited_addmax <= (max(data_json['labels'][x]['linesChanged']))):
                print("Label:",data_json['labels'][x]['label'])
            
            if (min(data_json['labels'][x]['linesChanged'])) > count_of_files_edited_addmax :
                print("Label:",data_json['labels'][x]['label'])
          
            
        if (data_json['labels'][x]['FilesChanged']!= '1' and data_json['labels'][x]['FilesChanged'] != data_json['labels'][count-1]['FilesChanged'] ):
            data_json['labels'][x]['FilesChanged']= data_json['labels'][x]['FilesChanged'].split("-")
            data_json['labels'][x]['FilesChanged']= [int(i) for i in data_json['labels'][x]['FilesChanged']]
            if ((min(data_json['labels'][x]['FilesChanged'])) <= count_of_files_edited_add <= (max(data_json['labels'][x]['FilesChanged']))):
                
                
                print ("Label:",data_json['labels'][x]['label'])
            
        if (count_of_files_edited_add > (max(Biggestsvalue)) and data_json['labels'][x]['FilesChanged']!= '1' and x== count-1 ):
            print("Label:",data_json['labels'][count-1]['label'])
                
   

    f = open('diff_File.txt', 'w')    
    for lines in diff_lines:
        if (lines.startswith('----') or lines.startswith('+---') or lines.startswith('-+++') or lines.startswith('++++') or lines.startswith('+++ ') ):

            f.write(lines.rsplit(' ', 1)[-1])
            f.write('\n')
            

    f.close()

    

if __name__ == "__main__":
 main()

