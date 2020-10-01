#what a waste of time. for coiled coil scholar wannabes i dont know how this is not in the world wide of the magnificent web yet.
#run pymol, file -> run script, run this, type selectHeptad XXX where X is the first residuue number wqhen u open display-sequences, becasue people dont like follow rules
#and start with random numbers when possible. this selects heptads for you so you can look at each and individual face's spheres and detemrine contact.
#example: selectHeptad 1
#if nothing is selected, try display->sequences->does it start with 1? weird numbers typically happen with dimers. do selectHeptad whatever number.
#look for A-D face which should be the hydrophobic core part. lets say face #1 is A. do renameHeptad 1, A

from pymol import cmd

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
        cmd.set_name('heptad{}'.format(i % 7), 'heptad{}'.format(faces[face % 7]))
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

cmd.extend('selectHeptad', selectHeptad)
cmd.extend('renameHeptad', renameHeptad)
cmd.extend('colorHeptad' , colorHeptad)
