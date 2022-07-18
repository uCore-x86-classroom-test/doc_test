import os
import re

if __name__ == '__main__':

    path = os.listdir(".")
    mdfiles = []
    tmp = []
    for i in path:
        if i.endswith('.md'):
            mdfiles.append(i)
        else:
            if os.path.isdir(i):
                tmp_path = []
                tmp_path = [i + '/' + j for j in os.listdir(i)]
                for j in tmp_path:
                    if j.endswith('.md'):
                        mdfiles.append(j)

    for i in mdfiles:
        o = re.sub('.md', '.rst', i) 
        cmd = 'pandoc ' + i + ' --from markdown --to rst -s -o '+ o
        os.popen(cmd)