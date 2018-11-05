# ---------------------------------------------------------------------------
# Create_nDSM.py
# Created on: 2017-01-05
# Chris Stayte
# Description: Create nDSM.
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy, os, sys, shutil, string, time, glob, numpy

# Check out any necessary licenses
arcpy.CheckOutExtension("spatial")
arcpy.CheckOutExtension("3D")

# Local variables:
print 'START ' + time.ctime()
start_time = time.time()
las_folder = r"I:\HydroProject\second_wave_las"
gdb_folder = r"I:\HydroProject\Junk\gdb"
tiff_folder = r"I:\HydroProject\nDSM2"
ground_feature_dataset = "Ground"
nonground_feature_dataset = "NonGround"
projection = "3735"
cell_size = ".1"

laslist = glob.glob(las_folder + "\\*.las")
for lasfile in laslist:
    try:
        print ""
        (filepath, filename) = os.path.split(lasfile)
        (shortname, extension) = os.path.splitext(filename)

        output_gdb = shortname + ".gdb"
        output_gdb_location = gdb_folder + "\\" + output_gdb

        print "Creating geodatabase " + output_gdb_location
        arcpy.CreateFileGDB_management(gdb_folder, output_gdb, "10.0")

        print "Creating " + nonground_feature_dataset + " dataset"
        arcpy.CreateFeatureDataset_management(output_gdb_location, nonground_feature_dataset, projection)

        print "Importing LAS to " + nonground_feature_dataset + " ..."
        out_fclass = output_gdb_location + "\\" + nonground_feature_dataset + "\\n_" + shortname
        arcpy.LASToMultipoint_3d(lasfile, out_fclass, cell_size, "1;2", "ANY_RETURNS", "", "", "las")
        print "Interpolating " + out_fclass + " ..."
        outgrid = output_gdb_location + "\\DSM_"
        if arcpy.Exists(out_fclass):
            arcpy.gp.NaturalNeighbor_sa(out_fclass, "Shape.Z", outgrid, "3")

        print "Creating " + ground_feature_dataset + " dataset"
        arcpy.CreateFeatureDataset_management(output_gdb_location, ground_feature_dataset, projection)

        print "Importing LAS to " + ground_feature_dataset + " ..."
        out_fclass = output_gdb_location + "\\" + ground_feature_dataset + "\\g_" + shortname
        arcpy.LASToMultipoint_3d(lasfile, out_fclass, cell_size, "2", "ANY_RETURNS", "", "", "las")
        print "Interpolating " + out_fclass + " ..."
        outgrid = output_gdb_location + "\\DTM_"
        if arcpy.Exists(out_fclass):
            arcpy.gp.NaturalNeighbor_sa(out_fclass, "Shape.Z", outgrid, cell_size)

        print "Creating a nDSM ....."
        outgrid = output_gdb_location + "\\nDSM_" + shortname
        grid1 = output_gdb_location + "\\DSM_"
        grid2 = output_gdb_location + "\\DTM_"
        if arcpy.Exists(grid1):
            if arcpy.Exists(grid2):
                arcpy.Minus_3d(grid1, grid2, outgrid)

        print "Exporting TIFF ...."
        if arcpy.Exists(outgrid):
            arcpy.RasterToOtherFormat_conversion(outgrid, tiff_folder, "TIFF")
    except Exception as ex:
        print(ex.message)


print 'END ' + time.ctime()
seconds = time.time() - start_time
m, s = divmod(seconds, 60)
h, m = divmod(m, 60)
print "Time elapsed: " + "%d:%02d:%02d" % (h, m, s)
