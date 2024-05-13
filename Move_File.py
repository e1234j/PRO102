import os
import shutil
source="C:/Users/emmaj/Downloads/abc"
destination="C:/Users/emmaj/OneDrive/Desktop"
list_of_files= os.listdir(source)
##print(list_of_files)
for i in list_of_files:
    name,ext=os.path.splitext(i)
    print(name)
    print(ext)
    if ext=="":
        continue
    if ext in  [".txt", ".doc", ".docx", ".pdf"]:
        path1 = source + '/' + i
        path2 = destination + '/' + "Document_Files"
        path3 = destination + '/' + "Document_Files" + '/' + i
        if os.path.exists(path2):
            print("this path already exists and moving the file")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("creating the path and moving the files")
            shutil.move(path1,path3)
        




