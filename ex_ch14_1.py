import urllib.parse, urllib.request, urllib.error
import json

url =('http://py4e-data.dr-chuck.net/comments_109846.json')


uh = urllib.request.urlopen(url)
data = uh.read().decode()
#print(data)

info = json.loads(data)
#print (info)
n = 0
sumcount = 0

for comment in info['comments']:
    sumcount = sumcount + comment['count']
    n += 1
    #print(comment)
print(sumcount)
print(n)

#    Sumcount = Sumcount + count
#    n +=1
#print (n)
#print (Sumcount)
