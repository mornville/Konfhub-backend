import requests

#Api url
url = 'https://o136z8hk40.execute-api.us-east-1.amazonaws.com/dev/get-list-of-conferences'
data = {}
combinedData = []
class Wrapper:
    #Fetching data from REST Api
    def getData(self, url)->dict:
        r = requests.get(url)
        #Loading json data
        if(r.status_code == 200):
            return r.json()
        else:
            return {}
    #Combining free and paid events
    def combinePaidAndFree(self, data)->dict:
        for i in data['paid']:
            combinedData.append(i)       
        for i in data['free']:
            combinedData.append(i)       
    
    #TASK 1: Print data in human readable format
    def task1(self, data)->list:
        count = 1
        for entry in data:
            #Preprocessing conferenece start date to convert into format like November 6th, 2020
            if(int(entry['confStartDate'].split(' ')[0])<10):
                entry['confStartDate'] = entry['confStartDate'][1:]

            if 4 <= int(entry['confStartDate'].split(' ')[0]) <= 20 or 24 <= int(entry['confStartDate'].split(' ')[0]) <= 30:
                day = entry['confStartDate'].split(' ')[0] + "th"
            else:
                day = entry['confStartDate'].split(' ')[0] + ["st", "nd", "rd"][int(entry['confStartDate'].split(' ')[0]) % 10 - 1]
            #Combining date, month and year after adding suffix to the day
            startDate = str(entry['confStartDate'].split(' ')[1].replace(',', '') + ' ' + day + ', ' + entry['confStartDate'].split(' ')[2])
            #printing single entry
            print(str(count) + '. ' + str(entry['confName']) + ', ' + startDate + ', ' + str(entry['city']) + ', ' +str(entry['state']) + ', ' +  str(entry['country']) + ', ' + str(entry['entryType']) + ', ' +str(entry['confUrl'])  + '\n')
            count+=1
            
#Declaring instance of class Wrapper
a = Wrapper()
data = a.getData(url)
# print(data)
if(data!= {}):
    a.combinePaidAndFree(data)
    a.task1(combinedData)
else:
    print('Could not fetch data')
