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



#The argument that will take from the pipeline will be the name of the base branch and the commit id 


with open("data_file.json", "r") as read_file:
    data = json.load(read_file)
print (data['labels'][1])
print (type(data['labels'][1]))