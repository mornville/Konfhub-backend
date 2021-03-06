import requests
import spacy
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
        combinedData.extend(data['paid'])   
        combinedData.extend(data['free'])       
    
    #To Print individual entries
    def printEntries(self, data):
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

    #TASK 1: Print data in human readable format
    def task1(self, data):
        self.printEntries(data)
            

    #TASK 2: Identify exact duplicates
    def task2(self, data):
        duplicates = []
        for i in range(len(data) - 1):
            if data[i] in data[i + 1 :]:
                duplicates.append(data[i])
            else:
                pass
        print('\nExact Duplicates: \n')
        for entry in duplicates:
            print(str(entry['confName']) + ', ' + entry['confStartDate'] + ', ' + str(entry['city']) + ', ' +str(entry['state']) + ', ' +  str(entry['country']) + ', ' + str(entry['entryType']) + ', ' +str(entry['confUrl'])  + '\n')
      
    
    #TASK 3: Identify semantic duplicates
    def task3(self, data):
        #Loading en_core_web_md(english model)
        nlp = spacy.load("en_core_web_md")
        redundant = []
        for entry in range(len(data)-1):
            entryFirst = nlp(data[entry][0])
            temp = []
            for j in range(entry + 1, len(data)):
                entrySecond = nlp(data[j][0])
                rank = entryFirst.similarity(entrySecond)
                if rank > 0.95:
                    temp.append(data[j])
            #Checking if similarity found
            if len(temp) > 0:
                if data[entry] not in redundant:
                    redundant.append(data[entry])
                    for event in temp:
                        if event not in redundant:
                            redundant.append(event)
                        else:
                            pass
                else:
                    pass



#Declaring instance of class Wrapper
a = Wrapper()
data = a.getData(url)
# print(data)
if(data!= {}):
    a.combinePaidAndFree(data)
    ch = 0
    while(ch!='4'):
      print("1.Task1: Print data in human readable format\n2.Task2: Identify Exact Duplicates\n3.Task3: Identify Semantic Duplicates\n4.Exit")
      ch = input('\nSelect:')
      print(ch)
      if(ch=='1'):
          a.task1(combinedData)
      elif(ch=='2'):
          a.task2(combinedData)
      elif(ch=='3'):
          a.task3(combinedData)
      else:
          pass

        
#     a.task2(combinedData)
else:
    print('Could not fetch data')
