#inputfile = open("D:/tmp/111.txt","r")
#for line in inputfile:
#    linesp = line.split("----")
#    for mem in linesp:
#        print(mem)
#    print(line)
#import urllib.request
#with urllib.request.urlopen('http://python.org/') as response:
#    html = response.read()
import urllib.request

req = urllib.request.Request('https://user.qzone.qq.com/2978983451')
with urllib.request.urlopen(req) as response:
   the_page = response.read()
print(the_page)
#for line in the_page:
#   line = line.strip()
#   print(line)   