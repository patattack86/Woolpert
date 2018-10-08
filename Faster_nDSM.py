#Working to make our nDSM be created faster from original las files, theory is to break file containing the las files
#down into a list of lists, then save each smaller list to a batch file, then execute original script on 
#the smaller list...or sum chit idk

# Import arcpy module
import arcpy, os, sys, shutil, string, time, glob, numpy
import numpy
import pprint

# Check out any necessary licenses
arcpy.CheckOutExtension("spatial")
arcpy.CheckOutExtension("3D")

# Local variables:
print 'START ' + time.ctime()
start_time = time.time()

las_folder = r"P:\GS\Restore\Shuler_76001_MartinCo_FL\1_block_ground"
gdb_folder = r"B:\Florida-Hydro\nDSM-Junk"
tiff_folder = r"B:\Florida-Hydro\nDSM-Destination"
ground_feature_dataset = "Ground"
nonground_feature_dataset = "NonGround"
projection = "2236"
cellsize = "1"
path = ""


laslist = glob.glob(las_folder + "\\*.las")

l = numpy.array_split(numpy.array(laslist), 6)

for index, List in enumerate(l):
    with open(r"C:\Users\reil\Desktop\nDSM_{}.bat".format(index), 'w') as batch_file:
        for path in list(List):
            batch_file.write("python c:\users\reil\source\repos\PythonApplication19\PythonApplication19\create_ndsm.py {} {} {} \n".format(path, projection, cellsize))
