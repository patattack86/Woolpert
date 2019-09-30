import arcpy
import numpy
import os, shutil, time, glob, sys
from shutil import copyfile

#where the files are located
polygon_folder = r""
feature_classes = []

#change this from Line to Polygon as necessary
shape_type = "Polygon"

#path to the output merged file
merge_output_file = r""

#Path to dissolved file
Diss_file_output = r""

#PAth to smoothed features


#Walking workspace recursively checking type, and appending filepath to list  
for dirpath, dirnames, filenames in arcpy.da.Walk(polygon_folder, datatype="FeatureClass", type= shape_type):  
    for filename in filenames:  
        desc = arcpy.Describe(os.path.join(dirpath, filename))
        if desc.shapeType == shape_type:
            feature_classes.append(os.path.join(dirpath, filename))  
            
#merging my list of feature classes to a new dataset  
arcpy.Merge_management(feature_classes, merge_output_file) 

#dissolving merged boundaries
arcpy.Dissolve_management(merge_output_file, Diss_file_output)

arcpy.SmoothPolygon_cartography(Diss_file_output, )
