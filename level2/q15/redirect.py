import re
import requests



TGT = 'http://q15.ctf.cpaw.site'


def find_flag(site):
  res = requests.get(TGT)
  print(res.text)

  for history in res.history:
    for key in history.__dict__.keys():
      attr = getattr(history, key)
      print(key, ':' , attr)
    print('-' * 30)

  print("heaers info")
  answer = ""
  for k, v in res.history[0].headers.items():
    print(k, ':', v)
    result = re.search('cpaw{.*}', v)
    if result:
      answer = result.group()
  return answer

if __name__ == '__main__':
  flag = find_flag(TGT)
  print('-' * 30)
  print(flag)
