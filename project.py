from pathlib import Path
from os import listdir
from os.path import isfile, join
import os
import shutil


root_dir = Path(r'D:\temp') ## root dir -> your download/folder 

folder_names = {
"Audio": {'aif','cda','mid','midi','mp3','mpa','ogg','wav','wma'},
"Compressed":{'7z','deb','pkg','rar','rpm', 'tar.gz','z', 'zip'},
'Code':{'js','jsp','html','ipynb','py','java','css','c','cpp','r','C'},
'Documents':{'ppt','pptx','pdf','xls', 'xlsx','doc','docx','txt', 'tex', 'epub','csv'},
'Images':{'bmp','gif','ico','jpeg','jpg','png','jfif','svg','tif','tiff'},
'Softwares':{'apk','bat','bin','jar','msi','py',"exe"},
'Videos':{'3gp','avi','flv','h264','mkv','mov','mp4','mpg','mpeg','wmv'},
'Others': {'NONE'}
}

def find_keys(para):
    for values in folder_names.values():
        if para in values:
            keys = values
            final = [k for k,v in folder_names.items()if v==keys]
            return final[0]

def make_folder(type):

    parent_dir = r'D:\test_folder'
    dirctory = find_keys(type)
    path = os.path.join(parent_dir,dirctory)
    os.mkdir(path)

list_extension = []
def split_text_extension():
    name = []
    for file in root_dir.iterdir():
        file_extension = os.path.splitext(file)[1].replace(".","")
        file_extension_1 = os.path.splitext(file)
        name.append(file_extension)
    return name

for item in split_text_extension():
    list_extension.append(item)

def main():
    
    file_path = []

    for file in root_dir.iterdir():
        file_extension_1 = os.path.splitext(file)
        file_path.append(file_extension_1)

    try:
        if 'aif' or 'cda' or 'mid'or 'midi'or 'mp3' or 'mpa' or 'ogg'or 'wav'or 'wma' in list_extension:
            (make_folder('aif'))

        if '7z'or 'deb' or 'pkg' or 'rar' or 'rpm' or 'tar.gz' or 'z' or 'zip' in list_extension:
            make_folder('zip')

        if 'js' or 'jsp' or 'html' or 'ipynb' or 'py' or 'java' or 'css' or 'C' in list_extension:
            make_folder('py')

        if 'ppt' or 'pptx' or 'pdf' or 'xls' or 'xlsx' or 'doc' or 'docx' or 'txt' or 'tex' or 'epub' in list_extension:
            make_folder('ppt')

        if 'bmp' or 'gif' or 'ico' or 'jpeg' or 'jpg' or 'png' or 'jfif' or 'svg' or 'tif' or 'tiff' in list_extension:
            make_folder('png')

        if 'apk' or 'bat' or 'bin' or 'exe' or 'jar' or 'msi' or 'py' in list_extension:
            make_folder("apk")

        if '3gp' or 'avi' or 'flv' or 'h264' or 'mkv' or 'mov' or 'mp4' or 'mpg' or 'mpeg' or 'wmv' in list_extension:
            make_folder('mp4')

        print("folder is created")
    except FileExistsError:
    
            for f in file_path:
                path = r"D:\temp" ## your folder path ##
                onlyfiles = [f for f in listdir(path) if isfile(join(path,f))]
                for file in onlyfiles:
                    try:
                        if file.endswith(('aif' , 'cda' , 'mid', 'midi', 'mp3' , 'mpa' , 'ogg', 'wav', 'wma')):
                            shutil.move(f"D:\\temp\\{file}",r"D:\test_folder\Audio")
                        if file.endswith(('7z', 'deb' , 'pkg' , 'rar' , 'rpm' , 'tar.gz' , 'z' , 'zip')):
                            shutil.move(f"D:\\temp\\{file}",r"D:\test_folder\Compressed")
                        if file.endswith(('js' , 'jsp' , 'html' , 'ipynb' , 'py' , 'java' , 'css','c','C')):
                            shutil.move(f"D:\\temp\\{file}",r"D:\test_folder\Code")
                        if file.endswith(('ppt' , 'pptx' , 'pdf' , 'xls' , 'xlsx' , 'doc' , 'docx' , 'txt' , 'tex' , 'epub','csv')):
                            shutil.move(f"D:\\temp\\{file}",r"D:\test_folder\Documents")
                        if file.endswith(('bmp','gif','ico','jpeg','jpg','png','jfif','svg','tif','tiff')):
                            shutil.move(f"D:\\temp\\{file}",r"D:\test_folder\Images")
                        if file.endswith(('apk' , 'bat' , 'bin' , 'exe' , 'jar' , 'msi')):
                            shutil.move(f"D:\\temp\\{file}",r"D:\test_folder\Softwares")
                        if file.endswith(('3gp' , 'avi' , 'flv' , 'h264' , 'mkv' , 'mov' , 'mp4' , 'mpg' , 'mpeg' , 'wmv')):
                            shutil.move(f"D:\\temp\\{file}",r"D:\test_folder\Videos")

                    except:
                        pass  
    

if __name__ == "__main__":
    main()