import os
import shutil

from_dir = "c:/Users/krima/OneDrive/Desktop/Document_files"
to_dir = "d:/Project 102"

list_of_files=os.listdir(from_dir)
print(list_of_files)


for file_name in list_of_files():
           
    name,extension=os.path.splitext(file_name)
    if extension=="" :
        continue
    if extension==['.txt', '.doc', '.docx', '.pdf','.jpg']:
        path1=from_dir+'/'+file_name
        path2=to_dir+'/'+'Document_files'
        path3=to_dir+'/'+'Document_files'+file_name

    if os.path.exists(path2):
        print("moving"+file_name)
        shutil.move(path1,path3)
    else:
        os.makedirs(path2)
        print("moving"+file_name)
        shutil.move(path1,path3)
