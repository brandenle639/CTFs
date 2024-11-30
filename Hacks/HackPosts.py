#Used to hack post request login information

#Used for web requests
import requests
#Set the url to hack
url = ''
#Enter login information
values = {'username': '',
          'password': ''}
#Sends the information to the page
r = requests.post(url, data=values)
#Prints out the page information
print(r.content)