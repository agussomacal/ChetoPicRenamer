import os
import time
import sys
from shutil import copy2

directory = os.getcwd() + '/test_rename_pics'

for f in os.listdir(directory):
    if f.split('.')[-1] in ['png', 'JPG']:
        os.remove('{}/{}'.format(directory, f))
        
if len(sys.argv) > 1:
    if sys.argv[1] == '-create':    
        for i in range(1000):
            with open('{}/img_{}.png'.format(directory, i), 'w'):
                time.sleep(0.01)
                
    elif sys.argv[1] == '-copy':
        src_dir = '{}/original_images/'.format(os.getcwd())
        for f in os.listdir(src_dir):
            copy2('{}/{}'.format(src_dir, f), 
            '{}/{}'.format(directory, f))    
            time.sleep(0.01)
            