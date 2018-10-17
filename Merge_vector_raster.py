import os, shutil, time, glob, sys
from shutil import copyfile
import arcpy

#Parent folder which contains the child folders. Child folders contain vector data of interest
Vec_Folder = r"B:\Florida-Hydro\Final-Vector"

#Parent folder containing child folders. Each child folder contains an nDSM and Intensity File
eCog_Folder = r"B:\Florida-Hydro\Florida-Ecog"

#Empty lists which the vector data will stored in until merged
Raw_Vect = []
Smooth_Vect = []
River = []
Stream = []
SubStream = []
Marshes = []

#Path where the merged vectors will be stored
Raw_merge = r"B:\Florida-Hydro\Final_Merged_Vectors\Raw_Merged.shp"
Smooth_merge = r"B:\Florida-Hydro\Final_Merged_Vectors\Smooth_Merged.shp"

#Path to merged rasters
nDSM_path = r"B:\Florida-Hydro\Merged_raster"
Intensity_path = r"B:\Florida-Hydro\Merged_raster"

#designating files for mosaic command
nDSM_file = r"nDSM_mosaic.tif"
Intensity_file = r"Intesnity.tif"

#This first section is constructed to merge final vector files
for subdir, dirs, files in os.walk(Vec_Folder):
    for file in files:
        (filepath, filename) = os.path.split(file)
        (shortname, extension) = os.path.splitext(filename)

        if (extension != ".shp"):
            continue

        if shortname == "hydro":
            Raw_Vect.append(os.path.join(subdir,file))
        if shortname == "Marsh":
            River.append(os.path.join(subdir,file))
        if shortname == "River":
            Marshes.append(os.path.join(subdir,file))
        if shortname == "Stream":
            Stream.append(os.path.join(subdir,file))
        if shortname == "Sub-Streams":
            SubStream.append(os.path.join(subdir,file))
        elif shortname == "Hydro_smoothed":
            Smooth_Vect.append(os.path.join(subdir,file))

arcpy.Merge_management(Raw_Vect, Raw_merge)
arcpy.Merge_management(Smooth_Vect, Smooth_merge)


#This second section is constructed to merge the raster files (Intensity & nDSM) if they exist in the
# vector files. Honestly, this should be turned into classes with inheritence but fuckit
folder_names = []
for subdir, dirs, files in os.walk(Vec_Folder):
    for file in files:
        (filepath, filename) = os.path.split(file)
        (shortname, extension) = os.path.splitext(filename)
        (path, foldername) = os.path.split(subdir)
        folder_names.append(foldername)

#Empy list containing individual nDSM and Intensity files 
nDSM = []
Intensity = []
projection = "102658"

for subdir, dirs, files in os.walk(eCog_Folder):
    for dir in dirs:
        if dir in folder_names:
            ndsm_file = "{}\\{}\\nDSM.tif".format(eCog_Folder, dir)
            intensity_file = "{}\\{}\\Intensity.tif".format(eCog_Folder, dir)
            if ndsm_file not in nDSM:
                nDSM.append(ndsm_file)
            if intensity_file not in Intensity:
                Intensity.append(intensity_file)


arcpy.MosaicToNewRaster_management(Intensity, Intensity_path, Intensity_file, projection,"32_BIT_UNSIGNED", "1", "1", "First")
arcpy.MosaicToNewRaster_management(nDSM, nDSM_path, nDSM_file, projection, "32_BIT_UNSIGNED", "1", "1", "First")
