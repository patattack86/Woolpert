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

laslist = glob.glob(las_folder + "\\*.las")

l = numpy.array_split(numpy.array(laslist), 10)

pprint.pprint(list(l[1]))

#Not using anything below this line just yet, probably wont end up using it at all
#splitting list into 10 smaller list
#def list_chunks(l, n):
#    "Use xrange for python2 use range for python 3"
#    for i in xrange(0, len(l), n):
#        yield l[i:i + n]
#
#pprint.pprint(list(list_chunks(laslist, 50)))
