# File       : diff_labels.py
# Author     : Rafael Estevez
# Company    : A2e technologies
# Created    : 16/03/2021
# -----------------------------------------------------------------------------
# Description: a script that analyzes the te output of git-diff and returns based on a files.md_FPGA of labels the corresponding label
# --------------------------------------------------------------

import os
import os.path as path
import argparse
import git
import re
import subprocess
from git import Repo
import json


parser = argparse.ArgumentParser(description='a tool to obtain the git diff and use the information to get a label depending on the changed files')
parser.add_argument('-id', '--id_commit', type=str, default="", help="Id of the commit")
parser.add_argument('-cv', '--Compiled_variant', type=str, default="", help="logfile_wrap where the variants compiled are printed")
parser.add_argument('-vc', '--Variant_to_compile', type=str, nargs='?', const='', help="Variant_to_compile")
# The argument  will be taken from the pipeline and it is the name  commit id


def main():

    args = parser.parse_args()
    if (args.id_commit):
        edited_lines(args.id_commit)
    if (args.Variant_to_compile):
        variants_collected(args.Variant_to_compile)
    if (args.Compiled_variant):
        compiled_variants(args.Compiled_variant)


def compiled_variants(Compiled_variant):

    f = open("logfile_wrap", 'rt')
    for line in f:
        if (line.startswith("Variants built: ")):
            print(line)
    f.close()


def variants_collected(Variant_to_compile):

    if "," in Variant_to_compile:
        Variant_to_compile = Variant_to_compile.replace(",", " ")
        Variant_to_compile = Variant_to_compile.replace("\n", "")
        print(Variant_to_compile)
    else:
        print(Variant_to_compile)


def edited_lines(idcommit):

    label_fromsjson = []
    Openjson = open("labels.json", "r")
    data_json = json.loads(Openjson.read())
    for i in data_json['labels']:
        label_fromsjson.append(i)
    repo = Repo()
    d = repo.git.merge(idcommit)
    print(d)
    merges_lines = "1 file changed, 0 insertions(+), 0 deletions(-)"
    print("\n")
    print("hola")
    found_first = False
    count_of_files_edited = 0
    count_of_files_edited_add = 0
    count_of_lines_edited_del = 0
    count_of_lines_edited_add = 0
    number_directory_changed = 0
    count = len(data_json['labels'])
    value_for_linesChanged_shared = data_json['labels'][count - 1]['linesChanged']
    Biggestsvalue = data_json['labels'][count - 2]['FilesChanged'].split("-")
    Biggestsvalue = [int(i) for i in Biggestsvalue]
    Minorvalue = data_json['labels'][0]['linesChanged'].split("-")
    Minorvalue = [int(i) for i in Minorvalue]
    for lines in merges_lines:

        if ("files changed" in lines):
            lines.rsplit(',')
            count_of_files_edited_add = re.findall(r'\d+ (?=files changed)', lines)
            if count_of_files_edited_add:
                count_of_files_edited_add = count_of_files_edited_add[0]
                count_of_files_edited_add = int(count_of_files_edited_add)
            else:
                count_of_files_edited_add = 0

            count_of_lines_edited_del = re.findall(r'\d+ (?=deletion)', lines)
            if count_of_lines_edited_del:
                count_of_lines_edited_del = count_of_lines_edited_del[0]
                count_of_lines_edited_del = int(count_of_lines_edited_del)
            else:
                count_of_lines_edited_del = 0
            count_of_lines_edited_add = re.findall(r'\d+ (?=insertion)', lines)
            if count_of_lines_edited_add:
                count_of_lines_edited_add = count_of_lines_edited_add[0]
                count_of_lines_edited_add = int(count_of_lines_edited_add)
            else:
                count_of_lines_edited_add = 0

    # Here the for  would help to count all the lines that were edited, and all the files that were edited
    count_of_lines_edited_addmax = count_of_lines_edited_add + count_of_lines_edited_del

    for x in range(count):

        if ((data_json['labels'][x]['linesChanged']) != value_for_linesChanged_shared and count_of_files_edited_add == (min(Minorvalue))):
            data_json['labels'][x]['linesChanged'] = data_json['labels'][x]['linesChanged'].split("-")
            data_json['labels'][x]['linesChanged'] = [int(i) for i in data_json['labels'][x]['linesChanged']]
            if ((min(data_json['labels'][x]['linesChanged'])) <= count_of_lines_edited_addmax <= (max(data_json['labels'][x]['linesChanged']))):
                print(data_json['labels'][x]['label'])

        if (int((max(data_json['labels'][x]['linesChanged']))) < count_of_lines_edited_add and count_of_files_edited_add == (min(Minorvalue))):
            if (x == (min(Minorvalue))):
                print(data_json['labels'][x]['label'])

        if (data_json['labels'][x]['FilesChanged'] != '1' and data_json['labels'][x]['FilesChanged'] != data_json['labels'][count - 1]['FilesChanged']):
            data_json['labels'][x]['FilesChanged'] = data_json['labels'][x]['FilesChanged'].split("-")
            data_json['labels'][x]['FilesChanged'] = [int(i) for i in data_json['labels'][x]['FilesChanged']]
            if ((min(data_json['labels'][x]['FilesChanged'])) <= count_of_files_edited_add <= (max(data_json['labels'][x]['FilesChanged']))):

                print(data_json['labels'][x]['label'])
        if (count_of_files_edited_add > (max(Biggestsvalue)) and data_json['labels'][x]['FilesChanged'] != '1' and x == count - 1):
            print(data_json['labels'][count - 1]['label'])

    f = open('diff_File.txt', 'w+')
    for lines in merges_lines:
        if (lines.endswith('-') or lines.endswith('+')):
            f.write(lines.rsplit('|')[0])
            f.write('\n')
    f.close()

    with open('diff_File.txt', 'r') as f:
        lines_for_write = []
        lines = f.readlines()
        lines = [line.replace(' ', '') for line in lines]
        for line in lines:

            if line.startswith("..."):
                line = line.replace("...", "*")

            if line.startswith("*"):
                line = os.popen(f"find . -wholename {line}").read()

            if line.startswith("./"):
                line = line[2:]

            lines_for_write.append(line)

            with open('diff_File.txt', 'w') as f:

                f.writelines(lines_for_write)

    f.close()


if __name__ == "__main__":
    main()
