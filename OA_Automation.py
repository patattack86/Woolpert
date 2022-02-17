import arcpy

#where do you want the points to go
out = r"G:\GS\Projects\Reil_Delivery\oaanalysis\GDOT_Project\script_test\points\test_Pointsmerge4.shp"

#where are the points
arcpy.env.workspace = r"G:\GS\Projects\Reil_Delivery\oaanalysis\GDOT_Project\Ecog_Shapefiles\points"

###Define projection
spatial_reference = arcpy.SpatialReference("NAD 1983 (2011) StatePlane Georgia West FIPS 1002 (US Feet)")

###get list of features in folder
shplist = arcpy.ListFeatureClasses('*.shp')
print(shplist)

###merge point shapefiles
arcpy.Merge_management(shplist, out)
print(out)

###define projection
arcpy.management.DefineProjection(out, spatial_reference)
print(out + "projection")

###add xy fields to table
arcpy.management.AddXY(out)
print(out + "_xy")


###create raster variable
zMax = r"G:\GS\Projects\Reil_Delivery\oaanalysis\GDOT_Project\script_test\raster\amg_zmax2.tif"
print(zMax)

###where is new shapefile going
points_values = r"G:\GS\Projects\Reil_Delivery\oaanalysis\GDOT_Project\script_test\points\test_values.shp"

###extrat values to points
arcpy.CheckOutExtension("Spatial")
arcpy.sa.ExtractValuesToPoints(out, zMax, points_values)
print(points_values + "_done")

###create lat and long fields
arcpy.management.AddField(points_values, 'Latitude', "TEXT")
arcpy.management.AddField(points_values, 'Longitude', "TEXT")
arcpy.management.AddField(points_values, 'Elevation', "FlOAT", 3)
print(points_values + "_addfield")

###calculate lat and long
arcpy.management.CalculateGeometryAttributes(points_values, [["Latitude", "POINT_Y"], ["Longitude", "POINT_X"]], '', '', None, "DMS_DIR_LAST")
print(points_values + "_LatLong")

###final attribute table alteration to get a nice label for z enabled surface
arcpy.management.CalculateField(points_values, "Elevation", "!RASTERVALU! * 1", "PYTHON3", '', "FLOAT")
print(points_values + "_CalcField")

