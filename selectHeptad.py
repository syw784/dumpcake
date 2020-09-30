#what a waste of time. for coiled coil scholar wannabes i dont know how this is not in the world wide of the magnificent web yet.
#run pymol, file -> run script, run this, type selectHeptad XXX where X is the first residuue number wqhen u open display-sequences, becasue people dont like follow rules
#and start with random numbers when possible. this selects heptads for you so you can look at each and individual face's spheres and detemrine contact.

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
        a = 'heptad{}'.format(str(j + 1))
        b = '(' + a + ', {})'
        cmd.select(a, b.format(pymol_select2(i + j)))

cmd.extend('selectHeptad', selectHeptad)
