
#filter out words...

import os

def rename_f(name):
    a = name
    a = a.replace('.pdb', '.chungus')
    return a

def join_path(path, name):
    return '{}\\{}'.format(path, name)

def rename_d(path, subfolder = True):
    os.chdir(path)
    r = []
    for i in os.listdir():
        if (os.path.isfile(i)):
            a = rename_f(i)
            if not a == i:
              r.append([join_path(path, i), join_path(path, a)])
        else:
            if subfolder:
                r += rename_d(join_path(path, i))
                os.chdir(path)
    return r
