

def bf_modulus(iteration):

  for i in range(iteration):
    x = 32134 + 1584891 * i
    y = x - 193127
    if y % 3438478 == 0:
      print('Flag is Found!')
      return x
  print('Flag is Not Found...')
  return None

if __name__ == '__main__':
  flag = bf_modulus(1000000)
  if flag != None:
    print(f"Flag: cpaw{{{flag}}}")
