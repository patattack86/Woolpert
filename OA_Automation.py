import arcpy


#where do you want the points to go
out = r"G:\GS\Projects\Reil_Delivery\oaanalysis\GDOT_Project\4J2\shapefiles\points\4J2_Pointsmerge2"

#where are the points
arcpy.env.workspace = r"G:\GS\Projects\Reil_Delivery\oaanalysis\GDOT_Project\4J2\shapefiles\points"

#get list of features in folder
shplist = arcpy.ListFeatureClasses('*.shp')
print(shplist)

#merge point shapefiles
arcpy.Merge_management(shplist, out)

#define projection
spatial_reference = arcpy.SpatialReference("NAD 1983 (2011) StatePlane Georgia West FIPS 1002 (US Feet)")
arcpy.management.DefineProjection(out, spatial_reference)

#add xy fields to table
arcpy.management.AddXY(out)

#create raster variable
zMax = r"G:\GS\Projects\Reil_Delivery\oaanalysis\GDOT_Project\4J2\Rasters\4J2_zMax.tif"

#where is new shapefile going
points_values = r"G:\GS\Projects\Reil_Delivery\oaanalysis\GDOT_Project\4J2\shapefiles\points\4j2_values.shp"

#extrat values to points
arcpy.sa.ExtractValuesToPoints(out, zMax, points_values, "NONE", "VALUE_ONLY")

#create lat and long fields
arcpy.management.AddField(out, 'Latitude', TEXT)
arcpy.management.AddField(out, 'Longitude', TEXT)
arcpy.management.AddField(out, 'Elevation', FlOAT, 3)

#calculate lat and long
arcpy.management.CalculateGeometryAttributes(points_values, [["Latitude", "Latitude POINT_Y"], ["Longitude", "Longitude POINT_X"]], '', '', None, "DMS_DIR_LAST")

#final attribute table alteration to get a nice label for z enabled surface
arcpy.management.CalculateField(points_values, "Elevation", "!RASTERVALU! * 1", "PYTHON3", '', "TEXT", "NO_ENFORCE_DOMAINS")
