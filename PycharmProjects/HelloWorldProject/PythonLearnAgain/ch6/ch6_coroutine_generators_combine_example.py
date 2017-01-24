import os
import fnmatch

def find_files(topdir,pattern):
    for path, dirname, filelist in os.walk(topdir):
        #print('walking ', path, dirname, filelist)
        for name in filelist:
            #print('File matching: ', name)
            if fnmatch.fnmatch(name,pattern):
                yield os.path.join(path,name)



import gzip,bz2
def opener(name):
    if name.endswith('.gz'):
        f = gzip.open(name)
    elif name.endswith('.bz2'):
        f = bz2.open(name)
    else:
        f = open(name)
    yield f




def cat(filelist):
    for line in f:
        #print(line)
        yield line

def grep(pattern,lines):
    if pattern in lines:
        yield lines




if __name__ == '__main__':
    for filepath in find_files(r'C:\Users\vburaga\Desktop\Testing\Email\Load_files\logs', 'www.log*'):
        print("Execution Start : ", filepath)
        for f in opener(filepath):
            print(f)
            for lines in cat(f):
                for exc in grep("optimizelyEndUserId", lines):
                    print(filepath, exc)
                    #pass


    # or you can call this way

    #file_path = find_files(r'C:\Users\vburaga\Desktop\Testing\Email\Load_files\logs','www.log*')
