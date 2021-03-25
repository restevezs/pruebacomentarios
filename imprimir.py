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
   print (basebr)



if __name__ == "__main__":
 main()
