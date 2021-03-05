'''import git
from unidiff import PatchSet

from io import StringIO

commit_sha1 = '7df6b0e71d8912a6aa4f9f249b7853ceabad3f0d'
commit_sha11 = '7df6b0e71d8912a6aa4f9f249b7853ceabad3f0d'
repo_directory_address = "path"

repository = git.Repo()
commit = repository.commit(commit_sha1)

uni_diff_text = repository.git.diff(commit_sha1+ '~1', commit_sha11,
                                    )
print(uni_diff_text)
'''
import re
import subprocess

def main():
    print(edited_lines())

def edited_lines():
    ans = []
    with open('C:\\Users\\restevez\\Documents\\oculus\\repo.jenkinstest\\checarcomentarios\\pruebacomentarios\\foo.txt') as source:
            template = source.read()
    if template is None:
        print('Error. Template is empty')
        sys.exit(1)
    print (template)
    diff_lines = template.split("\n")
    found_first = False
    # adjust for added lines
    adjust = 0
    # how many lines since the start
    count = 0
    for line in diff_lines:
        print("estoes lo que hace el fot",line)
        
        count += 1
        if line.startswith('-'):
        # minus one because count is 1 when we're looking at the start line
            ans.append(count)
                
            continue

        if line.startswith('+'):
            adjust += 1
            continue

        # get the start line
        match = re.fullmatch(r'@@ \-(\d+),\d+ \+\d+,\d+ @@', line)
        if match:
            start = int(match.group(1))
            count = 0
            adjust = 0
            
    print (ans)
    return ans





if __name__ == "__main__":
 main()
