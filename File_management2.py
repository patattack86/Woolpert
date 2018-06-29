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

        directory = master + "\\{}.shortname"

        if not os.path.exists(directory):
            os.makedirs(directory)

def movefiles(filelocation, dir):
    main = "write the main directory where this shit is"
    directory = "write whereever it is going"

    for filelocation in os.walk(dir):
        ##when using os walk, we'll get a root file, subdirectoriesm and the the files within the subdirectories
        print('root', root)
        print('subdirs', subdirs)
        print('files', files)
