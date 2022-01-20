
# Chase Christensen, Student ID: #001528190
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
    def __init__(self, id, address, city, state, zip, deadline, mass, notes, status, time):
        self.ID = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.mass = mass
        self.notes = notes
        self.status = status
        self.time = time  # Added time for use in the delivery time search

    def __str__(self):  # overwrite print
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.ID, self.address, self.city, self.state, self.zip,
                                                        self.deadline, self.mass, self.notes, self.status, self.time)


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
            pTime = ""
            p = Package(pID, pAddress, pCity, pState, pZip, pDeadline, pMass, pNotes, pStatus, pTime)
            myHash.insert(pID, p)  # insert data into hash table


myHash = ChainingHashTable()

loadPackageData('WGUPSPackageData.csv')


# import Data table into list of lists. Data is also inverted so all cells are filled
with open('distanceTable.csv', 'r') as distanceData:
    csv_reader = csv.reader(distanceData)
    distanceData = list(csv_reader)
distanceDataFloat = [[float(x) for x in e] for e in distanceData]  # put data as float


# input addressdata as list, include only address itself
addressData = []
with open('addressdata.csv', 'r') as addressList:
    csv_reader = csv.reader(addressList)
    for data in csv_reader:
        addressData.append(data[2])  # sets address in it's own table for below function to find


def distanceBetween(address1, address2):  # function to return distance from distanceTable
    return distanceDataFloat[addressData.index(address1)][addressData.index(address2)]


def minimumDistanceFrom(fromAddress, truckPackages):
    # loop through packages, starting at 0
    nextPackageID = 0
    nextPackageAddress = ''
    minDistance = 1000
    for packageid in truckPackages:
        packageAddress = myHash.search(packageid).address  # pull address from Hash
        distance = distanceBetween(fromAddress, packageAddress)  # previous function called here
        if distance < minDistance:
            minDistance = distance
            nextPackageID = packageid
            nextPackageAddress = packageAddress
    return nextPackageID, nextPackageAddress, minDistance


# global variables and starting info declared
DistanceTraveled = 0.0
currentAddress = "4001 South 700 East"
time = datetime.timedelta(hours=8)  # need time in HH:MM format


def packageDelivery(truck):
    global DistanceTraveled
    global currentAddress
    global time

    for id in truck:
        if id == minimumDistanceFrom(currentAddress, truck)[0]:
            DistanceTraveled += minimumDistanceFrom(currentAddress, truck)[2]
            nextDistance = minimumDistanceFrom(currentAddress, truck)[2]
            currentAddress = minimumDistanceFrom(currentAddress, truck)[1]

            # calculate speed and update time
            deliveryTime = datetime.timedelta(hours=nextDistance/18)
            time += deliveryTime
            myHash.search(id).time = time
            myHash.search(id).status = "Delivered"
            # remove id and print what's left as well as current location
            truck.remove(id)
            print('Delivering package: ', id, ' Arrived at address: ', currentAddress,
                  ' Total distance traveled: ', round(DistanceTraveled, 2), ' Delivered at: ', time)

            # repeat until truck is empty
            packageDelivery(truck)

    else:

        return "Truck is empty, returning to HUB\n\n"


# Loading trucks
Truck1 = [
0, 3, 6, 13, 14, 15, 19, 20, 28, 29, 33, 39
]
for id in Truck1:
    myHash.search(id).status = "Loaded on Truck"

Truck2 = [
2, 4, 5, 12, 17, 21, 24, 25, 30, 31, 35, 36, 37
]

for id in Truck2:
    myHash.search(id).status = "Loaded on Truck"

Truck3 = [
1, 7, 8, 9, 10, 11, 16, 18, 22, 23, 26, 27, 32, 34, 38
]

for id in Truck3:
    myHash.search(id).status = "Loaded on Truck"


print("\nCurrent package loading status: \n")
print("Truck One: ", Truck1, "\n")
print("Truck Two: ", Truck2, "\n")
print("Truck Three: ", Truck3, "\n")

# Truck delivery
print("Delivering via Truck 1")

print(packageDelivery(Truck1))
DistanceTraveled += distanceBetween(currentAddress, "4001 South 700 East")  # return to hub and add return mileage


print("Delivering via Truck 2")
print(packageDelivery(Truck2))
DistanceTraveled += distanceBetween(currentAddress, "4001 South 700 East")


print("Delivering via Truck 3")
print(packageDelivery(Truck3))
DistanceTraveled += distanceBetween(currentAddress, "4001 South 700 East")

userTime = input("Enter time to check package status (HH:MM:SS 24hr format): ")


def getTime(userTime):  # take input time, convert to time format for comparison and output
    for id in range(40):
        myTime = myHash.search(id).time
        deliveryStatus = myHash.search(id).status
        h, m, s = list(userTime.split(":"))
        hms = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
        if myTime < hms:
            print('Package ID:', id, ' Status:', deliveryStatus, ' Delivery Time:', myTime)
        else:
            print('Package ID:', id, ' Status: Loaded and waiting for delivery')


getTime(userTime)

print("Total distance traveled at end of day: ", round(DistanceTraveled, 2))
