#Hacks website header

#Imports the webpage library
import urllib.request
#Creates the header request
req = urllib.request.Request(
    '{URL}', 
    data=None, 
    headers={
        'User-Agent': '',
        'Referer': ''
    }
)
#Sends the URL Request
f = urllib.request.urlopen(req)
#Gives the output of the header
print(f.read().decode('utf-8'))