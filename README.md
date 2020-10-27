a collection of failed phd stuff
-------------------------------
# imageJ + Hitachi  HT7700 (emory PPMS TEM)
1. open imageJ -> plugin -> macro -> start up macro

![Chungus](https://github.com/syw784/dumpcake/raw/master/readme/ij1.PNG)

2. paste imageJ_Hitachi_scalebar's code in it

![Chungus](https://github.com/syw784/dumpcake/raw/master/readme/ij2.PNG)

3. config: width = 100 means the scale bar represents 100 nm. bold hide means theres only going to be a bar; bold show i think will also write "100 nm" under it; run(crop) will crop out hitachi HT7700's bottom black portion including image captured time and scale bar to make it looks professionalish.

![Chungus](https://github.com/syw784/dumpcake/raw/master/readme/hj3.PNG)

4. restart imageJ. open a tif file. only tif file has magnification data stored in. choose a command from plugin -> macro.

hitachi scale will only set the scale. useful to make measuremetns

100 nm scale bar will only make the scale bar. 

hitachi 100 nm scale bar will make a bar, save, close to make the whole process faster.

![Chungus](https://github.com/syw784/dumpcake/raw/master/readme/ij4.PNG)


# selectHeptad:

![Chungus](https://github.com/syw784/dumpcake/raw/master/readme/dfpksdfdfs.PNG)

who thought of the great idea to imagine coiled-coil in head? what a crazy lad.
1. open a coiled-coil

![Chungus](https://github.com/syw784/dumpcake/raw/master/readme/hp1.PNG)

2. go pymol-file-run script.

![Chungus](https://github.com/syw784/dumpcake/raw/master/readme/hp2.PNG)

3. find selectHeptad.py and click on run.

![Chungus](https://github.com/syw784/dumpcake/raw/master/readme/hp3.PNG)

4. type selectHeptad 1 (if you got dimer chains u know what to do)

![Chungus](https://github.com/syw784/dumpcake/raw/master/readme/hp4.PNG)

5. a collection of slections from 0 - 6 shows up, click through and determine which one is a.

![Chungus](https://github.com/syw784/dumpcake/raw/master/readme/hp5.PNG)

6. type renameHeptad 2, A if heptad2 is A.

![Chungus](https://github.com/syw784/dumpcake/raw/master/readme/hp6.PNG)

7. all selections are renamed to A-G. I showed AD face in spehere and you can clearly see its AD face.


![Chungus](https://github.com/syw784/dumpcake/raw/master/readme/hp7.PNG)


# Histogram_temp dumdum:
why spend 5 hours automating this crap when you can make histograms in igor with a few clicks? now ur thinking. 

1. use imageJ (in combo with imageJ_Hitachi to auto load mag) to make some measurements

![Chungus](https://github.com/syw784/dumpcake/raw/master/readme/histtemp1.PNG)

2. copy all entries 
3. go to histogram_temp's sheet1's A1 and paste

![Chungus](https://github.com/syw784/dumpcake/raw/master/readme/histtemp12.PNG)

4. make sure the data you want ot craete histogram on is in column H; if not copy it to column H

![Chungus](https://github.com/syw784/dumpcake/raw/master/readme/histtemp3.PNG)

5. run view-macros-hist

![Chungus](https://github.com/syw784/dumpcake/raw/master/readme/histtem555.PNG)

6. type the # of bins - 1 (want 5 bins put 4 cuz icant really do math)

![Chungus](https://github.com/syw784/dumpcake/raw/master/readme/55555.PNG)

7. a "professional" garph is made

![Chungus](https://github.com/syw784/dumpcake/raw/master/readme/4324234234322.PNG)
