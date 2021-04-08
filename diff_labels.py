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
<<<<<<< HEAD
parser.add_argument('-ic','--id_commit', type=str,default="",
                    help="Id of the commit")
#The argument that will take from the pipeline will be the name of the base branch and the commit id 
=======
parser.add_argument('-id','--id_commit', type=str,default="",
                    help="Id of the commit")
#These arguments  will be taken from the pipeline and they are the name of the base branch and the commit id 
>>>>>>> f31e9e7cb66aa2d69e882a24c7bb278164dd6dd6

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
<<<<<<< HEAD
    label= 'label'
    # adjust for added lines
    adjust = 0
    # how many lines since the start
    count_of_files_edited = 0
    number_lines_edited_onSWmax = 0
    number_lines_edited_onSW = 0
    number_lines_edited_onFPGA = 0
    count_of_files_edited_on_fpga= 0
    count_of_files_edited_on_sw= 0
    sw = "sw/"
    fpga = "fpga/" 
    print(d)   
    for line in diff_lines:
        if line.startswith('+++'):
            count_of_files_edited = count_of_files_edited + 1
            
            if fpga in line: 
                if not line.endswith(".md"):
                    print('Requieres:',data_json['labels'][6]['Requires'])
                   
            if sw in line: 
                if not line.endswith(".md"):
                    print('Requieres:',data_json['labels'][7]['Requires'])
                        
    #this is an iteration of every line of the git diff and it will look for all the lines that start with a "+++" this would help to count the files edited 
                
    
    for lines in diff_lines:
        if lines.startswith('+'):
            number_lines_edited_onSW += 1
        if lines.startswith('---'):
            number_lines_edited_onFPGA+= 1
            
    #Here the for would help to count all the lines that were edited, and bellow the lines founded with +++ will rest, to count only the lines changed  
 
    number_lines_edited_onSW = number_lines_edited_onSW - count_of_files_edited
    numbf = number_lines_edited_onFPGA -count_of_files_edited
    number_lines_edited_onSWmax = number_lines_edited_onSW + number_lines_edited_onFPGA   
    data_json['labels'][0]['linesChanged']= data_json['labels'][0]['linesChanged'].split("-")
    LinesChangedFix =data_json['labels'][0]['linesChanged']
    LinesChangedFix = [int(i) for i in LinesChangedFix]
    
    
    #lineas fix

    data_json['labels'][2]['FilesChanged']= data_json['labels'][2]['FilesChanged'].split("-")
    FilesChangedMin =data_json['labels'][2]['FilesChanged']
    FilesChangedMin = [int(i) for i in FilesChangedMin]
    
    
    #files minor
    data_json['labels'][3]['FilesChanged']= data_json['labels'][3]['FilesChanged'].split("-")
    FilesChangedFeat =data_json['labels'][3]['FilesChanged']
    FilesChangedFeat = [int(i) for i in FilesChangedFeat]
    
    
    #files feature
    data_json['labels'][4]['FilesChanged']= data_json['labels'][4]['FilesChanged'].split("-")
    FilesChangedMon =data_json['labels'][4]['FilesChanged']
    FilesChangedMon = [int(i) for i in FilesChangedMon]
    
    #files calamity

    if (count_of_files_edited <= data_json['labels'][0]['FilesChanged'] and number_lines_edited_onSWmax < LinesChangedFix[1]):
        print('label:',data_json['labels'][0]['label'])
        print(data_json['labels'][0]['description'])
#The change is less than five lines and it is on one file.label fix

    if (count_of_files_edited == data_json['labels'][1]['FilesChanged'] and number_lines_edited_onSWmax >= data_json['labels'][1]['linesChanged'] ):
        print('label:',data_json['labels'][1]['label'])
        print(data_json['labels'][1]['description'])

#The change is more than five lines and it is on one file\: label tiny
    if (count_of_files_edited >=FilesChangedMin[0]  and count_of_files_edited < FilesChangedMin[1]):
        print('label:',data_json['labels'][2]['label'])
        print(data_json['labels'][2]['description'])  
#the change is on more than 1 file and less than 5: label minor

    if (count_of_files_edited >= FilesChangedFeat[0] and count_of_files_edited < FilesChangedFeat[1]):
        print('label:',data_json['labels'][3]['label'] )
        print(data_json['labels'][3]['description'])
#the change is on more than 5 file and less than 30: label feature    
    if (count_of_files_edited >= FilesChangedMon[0] and count_of_files_edited < FilesChangedMon[1]):
        print('label:',data_json['labels'][4]['label'])  
        print(data_json['labels'][4]['description'])
#the change is on more than 30 file and less than 50: label monster    
    if count_of_files_edited > data_json['labels'][5]['FilesChanged'] :
        print('label:',data_json['labels'][5]['label'])
        print(data_json['labels'][5]['description'])
#the change is on more than 50 files: label calamity    
    






=======
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

    

>>>>>>> f31e9e7cb66aa2d69e882a24c7bb278164dd6dd6
if __name__ == "__main__":
 main()

