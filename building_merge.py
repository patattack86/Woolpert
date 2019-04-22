import os, shutil, time, glob, sys
from shutil import copyfile
import arcpy
from arcpy import env

env.workspace = "C:/data"

Building_folder = r"C:\HydroSamples\Intensity"

building_List = glob.glob(Building_folder + "\\*.shp")

for shapefile in building_List:
    (filepath, filename) = os.path.split(shapefile)
    (shortname, extension) = os.path.splitext(filename)

    output_gdb = shortname + ".gdb"
    output_gdb_location = gdb_folder + "\\" + output_gd

    print "Creating geodatabase " + output_gdb_location
    arcpy.CreateFileGDB_management(gdb_folder, output_gdb, "10.0")

    print "Creating " + nonground_feature_dataset + " dataset"
    arcpy.CreateFeatureDataset_management(output_gdb_location, buiding_feature_dataset, projection)

arcpy.Merge_management(building_feature_dataset, building_merge_dataset)
