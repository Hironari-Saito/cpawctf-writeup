from PIL import Image
import PIL.ExifTags as ExifTags
import reverse_geocoder as rg


FILE = 'river.jpg'

def get_exif(file):
  with Image.open(FILE) as img:
    exif = {
      ExifTags.TAGS[k]: v
      for k, v in img._getexif().items()
      if k in ExifTags.TAGS
    }

  return exif

def get_gpsinfo(exif):
  gps = {
    ExifTags.GPSTAGS.get(t, t): exif["GPSInfo"][t]
    for t in exif["GPSInfo"]
  }
  return gps

def convert2deg(degree, minite, second, ref):
  print(degree)
  print(minite)
  print(second)
  print(ref)
  result = degree + (minite / 60) + (second / (60 * 60))
  if ref == 'N' or ref == 'E':
    return result
  else:
    return result * -1

if __name__ == '__main__':
  exif = get_exif(FILE)
  gps = get_gpsinfo(exif)
  latitude = convert2deg(*gps["GPSLatitude"], gps["GPSLatitudeRef"])
  longitude = convert2deg(*gps["GPSLongitude"], gps["GPSLongitudeRef"])
  results = rg.search([(latitude, longitude)])
  for k, v in results[0].items():
    print(k, ": ", v)


