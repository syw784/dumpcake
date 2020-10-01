from pymol import cmd

# coiled coil pymol toolkit. would have appreciated it if something similar was searchable 2 years ago so i can actually understand coiled-coil design. F.K. my phd.
#features:
#1. make all 7 heptad faces into selections by typing selectHeptad 1 (or whatever the number your sequence starts with. if you have a dimer and start wth diff numbers, run it twice)
#2. rename heptad faces into ABCDEFGs by typing renameHeptad face# face, like renameHeptad 1, A if heptad1 is A face.
#3. color heptad faces so its more distinguishable when shown as spheres. ad is green, e is red, g is blue, cb is yellow, f is cyan.
#4. del_disabled_obj deletes all disabled objects. i have to generate symmetry mates and get a lot of not useful objects, they make selection another level of mess on top of an already messy one; use this to mass delete them.
#5. merge_enabled merges all enabled objects into a new object. I use this to generate a coiled-coil bundle from monomer by generating symmetry mates, then merge into a separate coiled coil object. 

def pymol_select2(i):
    s = ''
    for j in range(6):
        s += 'residue {}, '.format(str(i))
        i += 7
    return s

def selectHeptad(i):   
    i = int(i)
    for j in range(7):
        a = 'heptad{}'.format(str((j + 1) % 7))
        b = '(' + a + ', {})'
        cmd.select(a, b.format(pymol_select2(i + j)))


def renameHeptad(i, face):
    faces = ['G', 'A', 'B', 'C', 'D', 'E', 'F',]
    i = int(i)
    face = faces.index(face)
    for j in range(7):
        try:
            cmd.set_name('heptad{}'.format(i % 7), 'heptad{}'.format(faces[face % 7]))
        except:
            'okay'
        i += 1
        face += 1
    cmd.select('heptadAD', 'heptadA, heptadD')
    cmd.select('heptadEG', 'heptadE, heptadG')
    cmd.select('heptadBCF', 'heptadB, heptadC, heptadF')
    colorHeptad()

def colorHeptad(atomic = None):
    #a-d green
    #e = red
    #g = blue
    #c, b = yellow
    #f = cyan
    cmd.color('green' , 'heptadA')
    cmd.color('green' , 'heptadD')
    cmd.color('red'   , 'heptadE')
    cmd.color('blue'  , 'heptadG')
    cmd.color('yellow', 'heptadC')
    cmd.color('yellow', 'heptadB')
    cmd.color('cyan'  , 'heptadF')
    if atomic:
        cmd.color('atomic', '(not elem C)')

def del_disabled_obj():
    r = cmd.get_object_list('enabled')
    for i in cmd.get_object_list():
        try:
            r.index(i)
        except:
            cmd.delete(i)
    #string += '_'
    #for i in cmd.get_object_list():
     #   if not i.find(string) == -1:
      #      cmd.delete(i)

def merge_enabled(name = 'merged'):
    cmd.select('sele', 'enabled')
    cmd.create(name, 'sele')
    
cmd.extend('selectHeptad', selectHeptad)
cmd.extend('renameHeptad', renameHeptad)
cmd.extend('colorHeptad' , colorHeptad)
cmd.extend('del_disabled_obj', del_disabled_obj)
cmd.extend('merge_enabled', merge_enabled)
