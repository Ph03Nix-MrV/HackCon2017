import base64
import math
import hashlib
from PIL import Image

img=Image.open('digest.png')
arr = list(img.getdata())
checksum=0
encrypted_flag =''
i=0
done = False
while done == False:
  if arr[i] != (0,0,0):
    for c in range(0,256):
      m = hashlib.md5()
      m.update(chr(c))
      m = m.hexdigest()
      m = int(m, 16)
      m_hex = str(hex(m))
      count = 0
      tmp=[]
      for j in range(0, len(m_hex)-3, 3):
        tmp.append((128 + ord(m_hex[j])^ord(m_hex[j+1]), 128 + ord(m_hex[j+1])^ord(m_hex[j+2]), 128 + ord(m_hex[j+2])^ord(m_hex[j+3])))
        count+=1
      if tmp == arr[i:i+count]:
        encrypted_flag+=chr(c)
        c=255
        i+=count
        checksum += m
        tmp = (int(checksum%256), int((checksum/256)%256), int((checksum/(256*256))%256) )
        if tmp == arr[i]:
          print '[*] Checksum: '+str(checksum)
          print '-------------------------------------------------------------'
          print '[*] encrypted_flag: \n'+encrypted_flag
          print '-------------------------------------------------------------'
          done = True
          break

def decode(s):
  return ''.join([ chr(ord(c)-4) for c in s] )[::-1]

len_flag=1
s=0
while True:
  s+=len_flag
  if s == len(encrypted_flag):
    break
  len_flag+=1
print '[*] Length Flag: '+str(len_flag)
print '[*] Flag: '+decode(encrypted_flag[len(encrypted_flag)-len_flag:]).decode('base64')

