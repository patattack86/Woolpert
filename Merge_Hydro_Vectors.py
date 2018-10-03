import os, shutil, time, glob, sys
from shutil import copyfile
import arcpy

#Parent folder which contains the child folders. Child folders contain vector data of interest
Vec_Folder = r"B:\Florida-Hydro\Final-Vector"

#Empty lists which the vector data will stored in until merged
Raw_Vect = []
Smooth_Vect = []

#Path where the merged vectors will be stored
Raw_merge = r"B:\Florida-Hydro\Final_Merged_Vectors\Raw_Merged.shp"
Smooth_merge = r"B:\Florida-Hydro\Final_Merged_Vectors\Smooth_Merged.shp"

for subdir, dirs, files in os.walk(Vec_Folder):
    for file in files:
        (filepath, filename) = os.path.split(file)
        (shortname, extension) = os.path.splitext(filename)

        if (extension != ".shp"):
            continue

        if shortname == "hydro":
            Raw_Vect.append(os.path.join(subdir,file))
        elif shortname == "Hydro_smoothed":
            Smooth_Vect.append(os.path.join(subdir,file))

arcpy.Merge_management(Raw_Vect, Raw_merge)
arcpy.Merge_management(Smooth_Vect, Smooth_merge)

