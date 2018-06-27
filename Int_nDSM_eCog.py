 import os, shutil, time, glob, sys
from shutil import copyfile


INT_folder = r"C:\HydroSamples\Intensity"
nDSM_folder = r"C:\HydroSamples\nDSM"
eCOG_folder = r"C:\HydroSamples\eCOG"


intensityList = glob.glob(INT_folder + "\\*.tif")
intensityTFWList = glob.glob(INT_folder + "\\*.tfw")

nDSMList = glob.glob(nDSM_folder + "\\*.tif")
nDSMTFWList = glob.glob(nDSM_folder + "\\*.tfw")


### Create the folders
for intensity in intensityList:
    (filepath, filename) = os.path.split(intensity)
    (shortname, extension) = os.path.splitext(filename)

    directory = eCOG_folder + "\\{}".format(shortname)

    if not os.path.exists(directory):
        os.makedirs(directory)

# Copy the files
for intensity in intensityList:
    (filepath, filename) = os.path.split(intensity)
    (shortname, extension) = os.path.splitext(filename)

    src = intensity
    dst = eCOG_folder + "\\{}\\intensity.tif".format(shortname)
    shutil.copy(src, dst)

for TFW in intensityTFWList:
    (filepath, filename) = os.path.split(TFW)
    (shortname, extension) = os.path.splitext(filename)

    src = TFW 
    dst = eCOG_folder + "\\{}\\intensityTFW .tif".format(shortname)
    shutil.copy(src, dst)

for nDSM in nDSMList:
    (filepath, filename) = os.path.split(nDSM)
    (shortname, extension) = os.path.splitext(filename)

    src = nDSM
    dst = eCOG_folder + "\\{}\\nDSM.tif".format(shortname)
    shutil.copy(src, dst)

for nDSMTFW in nDSMTFWList:
    (filepath, filename) = os.path.split(nDSMTFW)
    (shortname, extension) = os.path.splitext(filename)

    src = nDSMTFW
    dst = eCOG_folder + "\\{}\\nDSMTFW.tif".format(shortname)
    shutil.copy(src, dst)
