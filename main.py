import requests

#Api url
url = 'https://o136z8hk40.execute-api.us-east-1.amazonaws.com/dev/get-list-of-conferences'
data = {}
class api_wrapper:
    def getData(self, url):
        r = requests.get(url)
        #Loading json data
        data = r.json()
        print(data)

a = api_wrapper()
a.getData(url)