import olefile
import subprocess


FILE = 'open_me'

def open_file(file):
  subprocess.call(f'file %s' % file, shell=True) 

  # python-docx cannot handle this file because of too old version.
  if(olefile.isOleFile(file)):
    subprocess.call(f'mv %s %s.doc' % (file, file), shell=True)
      
  else:
    return 'CANT FIND FLAG'

if __name__ == '__main__':
  flag = open_file(FILE)
  print(flag)
