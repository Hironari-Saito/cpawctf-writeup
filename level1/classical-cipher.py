import sys


TGT = "fsdz{Fdhvdu_flskhu_lv_fodvvlfdo_flskhu}"

def caesar_cipher(ciphered_text):
  answer = ""
  for c in ciphered_text:
    if(c.isalpha()):
      answer += chr(ord(c) - 3)
    else:
      answer += c

  return answer 

if __name__ == '__main__':
  FLAG = caesar_cipher(TGT)
  print(FLAG)
