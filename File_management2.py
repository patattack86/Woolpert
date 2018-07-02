## we need a file fot generated intensities, generated ndsm, lidar intensity, generated shapefiles, smoothed shapefiles
## remember to us os.walk to move files from one location to another if necessary
import os
import shutil
import sys


#setting the location of the master file, poopshit assfart
master = r"C:\finish the path later"

#setting file path to what will  become the folders for the lidar derivatives and shapefiles and derr fucking lidar team derrrrivitives
INT_folder = r"C:\HydroSamples\Intensity"
nDSM_folder = r"C:\HydroSamples\nDSM"
gen_hydro = r"C:\HydroSamples\gen_hydrofiles"
gen_hydro_smoothed = r"C:\HydroSamples\gen_hydrofiles_smoothed"

lidar_hydro = r"C:\HydroSamples\lidar_hydro"
lidar_intensity = r"C:\HydroSamples\lidar_intensity"

ruleset = r"C:\HydroSamples\Ruleset"

#defining the function which will place each folder in its place, the element is like each intensity which is in the path(INT_folder) 
def createfolders(element, path):
    for folder in path:
        (filepath, filename) = os.path.split(intensity)
        (shortname, extension) = os.path.splitext(filename)

        master = r""

        ##Make sure to rename master to the folder where you will be placing things
        directory = master + "\\{}.shortname"

        if not os.path.exists(directory):
            os.makedirs(directory)

#using os.walk to move files from one location to another
def movefiles(dir, newdir):
    dir = "write the main directory where this shit is"
    newdir = "write whereever it is going"

    for dirpath, dirnames, filenames in os.walk(dir):
        ##os.walk will yield a tuple when using, for each file that it see's, you'll see the directory path, the directories within that path, and then the files in that path. 
        print('path:', dirpath)
        print('directories:', dirnames)
        print('files:', filenames)

        #this does not copy files, only moves from one location to the newdir
        for file in filenames:
            path = os.path.join(path, file)
            shutil.move(path, newdir)



