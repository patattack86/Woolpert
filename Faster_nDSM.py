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
projection = "2236"
cellsize = "1"
output_location = ""



laslist = glob.glob(las_folder + "\\*.las")

l = numpy.array_split(numpy.array(laslist), 6)

for index, List in enumerate(l):
    with open(r"C:\Users\reil\Desktop\nDSM_{}.bat".format(index), 'w') as batch_file:
        for path in list(List):
            las_file = path
            batch_file.write("python c:\users\reil\source\repos\PythonApplication19\PythonApplication19\create_ndsm.py {} {} {} {} \n".format(las_file, output_location, projection, cellsize))
