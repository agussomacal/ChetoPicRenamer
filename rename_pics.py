import os
import sys
import time


allowed_formats = ['png', 'jpeg', 'svg', 'eps', 'bmp']

def rename_one_file(name, prefix, item):
    img_format = name.split('.')[1]
    if img_format in allowed_formats:
        new_name = '{}_{}.{}'.format(prefix,item,img_format)
        os.rename(name, new_name)
        print(name+' -> '+new_name)


def sort_func(name1, name2):
    return os.path.getmtime(name1) < os.path.getmtime(name2)
    
    

def rename_many_files_from_directory(directory, prefix=None):
    for i, f in enumerate(sorted(os.listdir(directory), key=lambda x: os.path.getmtime(x))):
        print(os.path.getmtime(f))
        rename_one_file(f, 
                        directory.split('/')[-1] if prefix is None else prefix, 
                        i)
        #time.sleep(0.01)
    

if len(sys.argv) == 1:
    print('Asumo que estas en la carpeta de las imagenes a modificar.')
    directory = os.getcwd()
    print(sys.argv)
else:
    directory = sys.argv[1]

    
rename_many_files_from_directory(directory)
