import os.path as path
import argparse
import git
import re
import subprocess
from git import Repo



parser = argparse.ArgumentParser(description='a tool to obtain the git diff and use the information to get a label depending on the changed files')
parser.add_argument('-bb','--branch_base',  type=str, default="",
                    help='branch_base.')
parser.add_argument('-ic','--id_commit', type=str,default="",
                    help="Id of the commit")

def main():
    args = parser.parse_args()
    edited_lines(args.branch_base, args.id_commit)

def edited_lines(basebr,idcommit):
    repo = Repo()
    d= repo.git.diff("launo", "e33e3e1") 
    diff_lines= d.split('\n')
    ans = ""
    found_first = False
    # adjust for added lines
    adjust = 0
    # how many lines since the start
    count = 0
    numbsmax = 0
    numbs = 0
    numbsf = 0
    matrix=""
    matrixs=""
    matrixf=""
    countf= 0
    counts= 0
    sw = "sw/"
    fpga = "fpga/"    
    for line in diff_lines:
        if line.startswith('+++'):
            count = count + 1
            
            if fpga in line: 
                if not line.endswith(".md"):
                    matrix= "Requires fpga build"                    
                   
            if sw in line: 
                if not line.endswith(".md"):
                    matrixs= "Requires sw build"
        print (line)                   
   
                
    
    for lines in diff_lines:
        if lines.startswith('+'):
            numbs += 1
        if lines.startswith('-'):
            numbsf+= 1
 
    numbs = numbs - count
    numbf = numbsf -count
    numbsmax = numbs + numbsf
    if count <= 1:
        ans = "FIX"
    if (count >= 1 and count <= 5 and numbsmax > 5) :
        ans = "Tiny"
        
    if count >=5  and count < 30:
        ans = "minor"
    if count >= 30 and count < 50:
        ans = "Feature"
    if count >= 30 and count < 50:
        ans = "Monster"
    if count >= 50:
        ans = "Calamity"
    
    print (ans)
    print (matrix)
    print (matrixs)




if __name__ == "__main__":
 main()
