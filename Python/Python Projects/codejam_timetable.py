import datetime

"""


WIP




NA trains
sch1NA = dep=09:00 arr = 12:00
sch2NA = dep=10:00 arr = 13:00
sch3NA  dep= 11:00 arr = 12:30

sch4NB dep=12:02-15:00
sch5NB dep= 09:00-10:30

first of all sort the NA by departure if nec
set train 1 on sch1NA, trainAB numbers = 1
sch2NA - we need to check if there will be a NB service arriving back at A two minutes or more before the dep.
If not, sch2NA = train 2, add 1 to trainABnumbers
sch3NA - we need to check if there will be a NB service arriving back at A two minutes or more before the dep.
If this was the service used for train 2 we can't use it. Maybe put a flag on it?
Then return the value of trainAB numbers

what data types to use????
a service class. Holds dep and arr time, service id and flag. Set up the class and give it get and set methods.
Either make a different class for AN and BN or make it a property of the class.

Create an instance of the class for each of the services.
Put them in arrays for A and B, sorted on dep time for A and arr time for B

Start working through the array:

for the first service, set train A attribute to trainA1 . Add 1 to trainA count.
for the second service, search service B instances for one where the arr time is at least 2 mins less than second service dep time.
If one is found, add 1 to trainA count and set the train A attribute to trainA+count  
For the next service, search service B instances for one where the arr time is at least 2 mins less than second service dep time.
TrainA attribute must be empty.
If one is found, add 1 to trainA count and set the train A attribute to trainA+count set the train A attribute 
"""
#an instance of service is a scheduled train service
class Service:
    def __init__(self, dep, arr, serviceId, depStation, aFlag, bFlag):
        self.dep = dep
        self.arr = arr
        self.serviceId = serviceId
        self.depStation = depStation
        self.aFlag = aFlag
        self.bFlag = bFlag
      
    def getDep(self):
        depTime = datetime.datetime.strptime(self.dep, "%H:%M")
        return depTime.time()
    
    def getArr(self):  
        arrTime = datetime.datetime.strptime(self.arr, "%H:%M")
        return arrTime.time()


#set up services in multidimensional array. Use the data in the array to create a Service instance for each service
serviceA1 = {
  "dep": "09:00",
  "arr": "12:00",
  "serviceId": "1",
  "depStation": "A",
  "aFlag": False,
  "bFlag": False
}

serviceA2 = {
  "dep": "10:00",
  "arr": "13:00",
  "serviceId": "2",
  "depStation": "A",
  "aFlag": False,
  "bFlag": False
}

serviceA3 = {
  "dep": "11:00",
  "arr": "12:30",
  "serviceId": "3",
  "depStation": "A",
  "aFlag": False,
  "bFlag": False
}

serviceB1 = {
  "dep": "12:02",
  "arr": "15:00",
  "serviceId": "4",
  "depStation": "B",
  "aFlag": False,
  "bFlag": False
}

serviceB2 = {
  "dep": "09:00",
  "arr": "10:30",
  "serviceId": "4",
  "depStation": "B",
  "aFlag": False,
  "bFlag": False
}

serviceB1 = {
  "dep": "12:02",
  "arr": "15:00",
  "serviceId": "4",
  "depStation": "B",
  "aFlag": False,
  "bFlag": False
}

serviceB2 = {
  "dep": "12:02",
  "arr": "15:00",
  "serviceId": "5",
  "depStation": "B",
  "aFlag": False,
  "bFlag": False
}

serviceList =[serviceA1, serviceA2, serviceA3, serviceB1, serviceB2]
print(serviceList[0]["dep"])
#function to set up instances of Service objects from array, and save to list according to dep station
def createServices(myList):
    listA = []
    listB = []
    for x in range(len(myList)):
        d = myList[x]["serviceId"]
        d = Service(myList[x]["dep"],myList[x]["arr"],myList[x]["serviceId"],myList[x]["depStation"], myList[x]["aFlag"],myList[x]["bFlag"])
        print("Service", d.serviceId, "has been created")
        if(d.depStation=="A"):
           listA.append(d)
           
        else:
            listB.append(d)
          
    

for x in range(len(myList)):
        d = myList[x]["serviceId"]
        d = Service(myList[x]["dep"],myList[x]["arr"],myList[x]["serviceId"],myList[x]["depStation"], myList[x]["aFlag"],myList[x]["bFlag"])
        
serviceA = Service("09:00", "12:00", 1, "A", False, False)
print("Service", serviceA.serviceId, "departs at", serviceA.getDep(), "and arrives at", serviceA.getArr() )

