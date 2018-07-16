poopy = []

for subdir, dirs, files in os.walk(eCOG_folder):
    for file in files:
        if len(file) == 4:
            poopy.append(os.path.join(subdir, file))

for poop in poopy:
    os.remove(poop)
    
