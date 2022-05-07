import re
import requests


TGT = 'http://q9.ctf.cpaw.site'

def detect_flag(site_url):
  response = requests.get(site_url)
  answer = re.search('cpaw{.*}', response.text)
  return answer.group()

if __name__ == '__main__':
  flag = detect_flag(TGT)
  print(flag)
