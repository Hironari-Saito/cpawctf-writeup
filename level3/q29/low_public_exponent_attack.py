import gmpy2


def cpe_attack(e, c):
  m = gmpy2.iroot(c, e) 
  if m[1] == True:
    return m[0]
  print('Root isnot exact. cannot use common modulus attack.')
  return None
if __name__ == '__main__':
  e = 11
  c = 80265690974140286785447882525076768851800986505783169077080797677035805215248640465159446426193422263912423067392651719120282968933314718780685629466284745121303594495759721471318134122366715904
  flag = cpe_attack(e, c)
  if flag is not None:
    print(f'cpaw{{{flag}}}')
