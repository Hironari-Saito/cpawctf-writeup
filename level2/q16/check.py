import pyshark
import re


FILE = 'http_traffic.pcap'

def search_word(file):
  caps = pyshark.FileCapture(file, include_raw=True, use_json=True, display_filter='http')
  for cap in caps:
    hex_packet = cap.frame_raw.value
    binary_packet = bytearray.fromhex(hex_packet)
    print(binary_packet.decode('ascii', 'ignore'))

    answer = re.search('cpaw{.*}',binary_packet.decode('ascii', 'ignore'))
    if answer: 
      return answer.group()    


if __name__ == '__main__':
  flag = search_word(FILE)
  print(flag)
