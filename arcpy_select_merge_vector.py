#subset shapefile based on area of the 

import arcpy
from arcpy import env
import arcpy.cartography as CA
import arcpy.management as DM

#set parameters poopy fart butt
Shapefile_folder = ""
Vector_location = ""
Where_Clause = ""
Field_name = ""
Save_location = ""

#set workspace
arcpy.env.workspace = ""

#merge individual vectors into one vector
vector_list = []

for subdir, dirs, files in os.walk(Shapefile_folder):
    for file in files:
        vector_list.append(os.path.join(subdir, file))

merged_raw = arcpy.Merge_management(vector_list, Save_location)

#create necessary field in table
arcpy.management.AddField(merged_raw, Field_name, "SHORT")

#Calculate filed bas on area

arcpy.MakeFeatureLayer_management(merged_raw, "lyr")

Vector_selection = arcpy.SelectLayerByAttribute_management("lyr", "SUBSET_SELECTION", Where_Clause) 

#extract features based on attribute

arcpy.CopyFeatures_management(Vector_selection, "Suitable_hydro")

#merge data based on attribute

arcpy.merge("Suitable_hydro", Save_location)

