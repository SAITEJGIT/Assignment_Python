from os.path import exists
from datetime import date
import time
import shutil
import sys


def copyfiles(src,dest):
  try:
    file_exists = exists(dest) 
    if(file_exists == True):
        
        t = time.localtime()
        current_time = time.strftime("%H%M%S", t)
        
        date1=date.today()
        Datebackup=str(date1).replace('-','.')

        dest= src + Datebackup + '-' + current_time + ".txt"
        
        shutil.copy(src,dest)
    else:
        shutil.copy(src,dest)
  except FileNotFoundError:
     print("File not found, Please enter a valid source or destination file")
    
src=sys.argv[2]
dest=sys.argv[1]
copyfiles(dest, src)
