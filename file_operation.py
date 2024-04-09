 # if you want to read or write on file "with open (fielpath, r/w):"
import os
def update_file (file_path, key, value):
    with open (file_path,"r") as file:
        lines = file.readlines()
        print(lines)
        print(type(lines))
    
    with open (file_path,"w") as file:
        for line in lines:
            #print(type(line))
            if key in line:
                file.write(key + "=" + value + "\n")
            else:
                file.write(line)
    

update_file('S://server.conf', "MAX_CONNECTIONS", "55")
#update_file('server.conf', "MAX_CONNECTIONS", "65")
#S:\python\file_operation.py

