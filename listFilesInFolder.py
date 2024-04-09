import os
folders = input("please enter all the folder with space for which you want all the files: ").split()
#print(folders)

for folder in folders:
    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print("Please provide correct folder with proper path. Your folder " + folder + "is incorerct/")
        continue
    except PermissionError:
        print("You don't have permission on the folder ", folder)
        continue
    print("--------Listing files for folder: " + folder)
    #print("type of files is " ,type(files))
    for file in files:
        print(file)
        #print("type of each file is ", type(file))