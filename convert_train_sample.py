from glob import glob
import os

paths = ['test', 'train']
cwd = os.getcwd()

for path in paths:
    fnames = glob(path+'/**jpg')
    with open(cwd + '/'+ path+'.txt', 'w') as outfile:
        outfile.write("\n".join(fnames))

