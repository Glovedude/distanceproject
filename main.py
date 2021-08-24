import csv
import datetime

class ChainingHashTable:

    def __init__(self, initial_capacity=39):
        # Constructor with initial capacity parameter
        # Assign all bucket with empty list
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # insert new item into hash table
    def insert(self, key, item):  # insert and update
        # get the bucket list where item will go
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]


        # update key if it is in bucket
        for kv in bucket_list:
            # print key_value()
            if kv[0] == key:
                kv[1] = item
                return True

        # if not, insert the item to the end of the bucket
        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    # searches for an item with matching key in the hash table
    # return the item if found, none if not
    def search(self, key):
        # get the bucket list where key would be
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        # print(bucket_list)

        # search for the key in the bucket
        for kv in bucket_list:
            # print (key_value)
            if kv[0] == key:
                return kv[1]  # value
        return None

    # remove an item with matching key from table
    def remove(self, key):
        # get the bucket list where this item will be removed
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # remove the item from the list if present
        for kv in bucket_list:
            # print (key_value)
            if kv[0] == key:
                bucket_list.remove([kv[0], kv[1]])


class Package:
    def __init__(self, id, address, city, state, zip, deadline, mass, notes, status):
        self.ID = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.mass = mass
        self.notes = notes
        self.status = status

    def __str__(self):  # overwrite print
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.ID, self.address, self.city, self.state, self.zip,
                                                   self.deadline, self.mass, self.notes, self.status)


def printAddress(property):
    print(property)

def loadPackageData(fileName):
    with open(fileName) as WGUPSPackageData:
        packageData = csv.reader(WGUPSPackageData, delimiter=',')
        for package in packageData:
            pID = int(package[0])
            pAddress = package[1]
            pCity = package[2]
            pState = package[3]
            pZip = int(package[4])
            pDeadline = package[5]
            pMass = int(package[6])
            pNotes = package[7]
            pStatus = 'At Hub'
            p = Package(pID, pAddress, pCity, pState, pZip, pDeadline, pMass, pNotes, pStatus)
            print(pAddress)  # prints address only for each key

            myHash.insert(pID, p)  # insert data into hash table


myHash = ChainingHashTable()

loadPackageData('WGUPSPackageData.csv')

print("Package info:")  # hash table header

for i in range(len(myHash.table)):
    print("Package: {}".format(myHash.search(i)))  # print each line of package data



# import Data table into list of lists. Data is also inverted so all cells are filled
with open('distanceTable.csv', 'r') as distanceData:
    csv_reader = csv.reader(distanceData)
    distanceData = list(csv_reader)
print(distanceData)
distanceDataFloat = [[float(x) for x in e] for e in distanceData]  # put data as float


# input addressdata as list, include only address itself
addressData=[]
with open('addressdata.csv', 'r') as addressList:
    csv_reader = csv.reader(addressList)
    for data in csv_reader:
        addressData.append(data[2])  # sets address in it's own table for below function to find


def distanceBetween(address1, address2):
    return distanceDataFloat[addressData.index(address1)][addressData.index(address2)]

print(distanceBetween('4001 South 700 East', '1060 Dalton Ave S'))

def minimumDistanceFrom(fromAddress, truckPackages):
    # loop through packages
    nextPackageID = 0
    nextPackageAddress = ''
    minDistance = 1000
    for packageid in truckPackages:
        packageAddress = myHash.search(packageid).address
        distance = distanceBetween(fromAddress, packageAddress)
        if distance < minDistance:
            minDistance = distance
            nextPackageID = packageid
            nextPackageAddress = packageAddress
    return nextPackageID, nextPackageAddress, minDistance




Truck1 = [
0, 1, 3, 4, 6, 7, 12, 13, 15, 19, 25, 28, 29, 30, 33, 39
]
for id in Truck1:
    myHash.search(id).status = "Loaded on Truck"

Truck2 = [
2, 5, 9, 10, 11, 14, 16, 17, 18, 20, 21, 22, 24, 27, 31, 35, 37
]

for id in Truck2:
    myHash.search(id).status = "Loaded on Truck"

Truck3 = [
8, 23, 25, 26, 32, 34, 36, 38
]

for id in Truck3:
    myHash.search(id).status = "Loaded on Truck"


print("\nCurrent package loading status: \n")
print("Truck One: ", Truck1, "\n")
print("Truck Two: ", Truck2, "\n")
print("Truck Three: ", Truck3, "\n")



DistanceTraveled = 0.0
currentAddress = "4001 South 700 East"
DistanceTraveledTime = 0.0
'''
time_stamp = datetime.timedelta(hours=8, minutes=0, seconds=0)
time_stamp2 = datetime.timedelta(hours=0, minutes=0, seconds=0)
# time_stamp = time_stamp + time_stamp2
print(time_stamp)
'''
time = 8.0
t = datetime.time(8, 0, 0)

def packageDelivery(truck):
    global DistanceTraveled
    global currentAddress
    global time

    nextDistance = 0
    i = 0




    for id in truck:
        if id == minimumDistanceFrom(currentAddress, truck)[0]:
            DistanceTraveled += minimumDistanceFrom(currentAddress, truck)[2]
            nextDistance = minimumDistanceFrom(currentAddress, truck)[2]
            currentAddress = minimumDistanceFrom(currentAddress, truck)[1]

            # calculate speed and update time

            time += nextDistance/18
            # print(round(time, 2))
            timeFinal = ('{0:02.0f}:{1:02.0f}'.format(*divmod(float(time) * 60, 60)))
            myHash.search(id).status = (timeFinal)


            # remove id and print what's left as well as current location
            truck.remove(id)
            # print(truck)
            print('Delivering package: ', id, ' Current address: ', currentAddress,
                  ' Total distance traveled: ', round(DistanceTraveled, 2), ' Delivered at: ', timeFinal)


            # repeat until truck is empty
            packageDelivery(truck)

    else:

        return ("Truck is empty, returning to HUB\n\n")



print("Delivering via Truck 1")
# print(packageDelivery(Truck0))

print(packageDelivery(Truck1))
DistanceTraveled += distanceBetween(currentAddress, "4001 South 700 East") # return to hub and add return mileage

print("Delivering via Truck 2")
print(packageDelivery(Truck2))
DistanceTraveled += distanceBetween(currentAddress, "4001 South 700 East")

print("Delivering via Truck 3")
print(packageDelivery(Truck3))
DistanceTraveled += distanceBetween(currentAddress, "4001 South 700 East")


print("Total distance traveled: ",round(DistanceTraveled, 2))


fakeTimes = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,
             31,32,33,34,35,36,37,38,39]


test = []

for id in fakeTimes:
    test.append((myHash.search(id).status).replace(':', ''))
    # print(test)

userinput = input("Enter a time to check package status (Must be in 24hr format. e.g. 0930): ")
def condition(x): return x < userinput
testoutput = [idx for idx, element in enumerate(test) if condition(element)]

for id in testoutput:
    print(myHash.search(id))



