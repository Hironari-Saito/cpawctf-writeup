import subprocess


UNKNOWN_FILE = 'exec_me'

def exec_file(file):
  res = subprocess.call(f'file %s' % file,shell=True)
  subprocess.call(f'chmod +x %s' % file, shell=True)
  print('chmod +x exec_me')
  answer = subprocess.check_output(f'./%s' % file, shell=True)
  return answer


if __name__ == '__main__':
  flag = exec_file(UNKNOWN_FILE)
  print(flag.decode())
