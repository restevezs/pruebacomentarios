import git
import re
import subprocess
from git import Repo

def main():
    edited_lines()

def edited_lines():
    repo = Repo()
    d= repo.git.diff() 
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
