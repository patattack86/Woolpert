import os, shutil, time, glob, sys
from os import listdir, rmdir
from shutil import move

src = r"M:\GS\Users\Reil\deliverable"
dst = r"M:\GS\Users\Reil\dummmy"
#shutil.move(src, dst)

rootdir = r"M:\GS\Users\Reil\dummmy\deliverable"
#rootdir = r"C:\Users\reil\Downloads\deliverable"



# Used to delete unessary 'info' folder
# ------------------------------------------------
info_folders = []
for subdir, dirs, files in os.walk(rootdir):
    if (subdir[-4:] == "info"):
        info_folders.append(subdir)

for info_folder in info_folders:
    shutil.rmtree(info_folder)
# ------------------------------------------------

# Used to move all generated hydro files into 'Generated_Hydro' folder
# ------------------------------------------------

# Get all tile folders in a "LIST"
tile_folders = [] ## Folders where each tile is processed and outputed to
for dir in os.listdir(rootdir):
    directory = "{}\\{}".format(rootdir, dir)

    if os.path.isdir(directory):
        tile_folders.append(directory)

# Create a "Generated_Hyrdo" Folder for each sub folder
for tile_folder in tile_folders:
    generated_hydro_directory = "{}\\{}".format(tile_folder, "Generated_Hydro")
    if not os.path.isdir(generated_hydro_directory):
        os.makedirs(generated_hydro_directory)


# Get All Files in each folder in a "DICT"
file_lists = {}

for tile_folder in tile_folders:
    file_lists[tile_folder] = os.listdir(tile_folder)

# Copy all files into "Generated_Hyrdo" Folder
for file_list in file_lists:
    for file in file_lists[file_list]:
        orginal_file_location = "{}\\{}".format(file_list, file)
        new_file_location = "{}\\{}".format(file_list, "Generated_Hydro")
        shutil.move(orginal_file_location, new_file_location)
