#subset shapefile based on area of the 

import arcpy
from arcpy import env
import arcpy.cartography as CA
import arcpy.management as DM

#set parameters poopy fart butt
Shapefile = ""
Where_Clause = ""
Field_description = ""
Save_location = ""

#set workspace
arcpy.env.workspace = ""

#create necessary field in table
arcpy.management.AddField(Shapefile, Field_description)

#Calculate filed bas on area

arcpy.MakeFeatureLayer_management(Shapefile, "lyr")

Vector_selection = arcpy.SelectLayerByAttribute_management("lyr", "SUBSET_SELECTION", Where_Clause) 

#extract features based on attribute

arcpy.CopyFeatures_management(Vector_selection, "Suitable_hydro")

#merge data based on attribute

arcpy.merge("Suitable_hydro", Save_location)
