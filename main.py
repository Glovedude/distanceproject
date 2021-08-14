import csv




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
0, 1, 3, 4, 6, 7, 9, 12, 13, 15, 19, 25, 28, 29, 30, 33
]

Truck2 = [
2, 5, 10, 11, 14, 16, 17, 18, 20, 21, 22, 24, 27, 31, 35, 37
]

Unloaded = [
8, 25, 26, 32, 34, 36, 38
]



print("\nCurrent package loading status: \n")
print(Truck1, "\n")
print(Truck2, "\n")
if Unloaded == ["Unloaded:"]:
    print("there are no more packages to load.\n")
else:
    print(Unloaded, "\n")




def packageDelivery(truck):
    DistanceTraveled = 0
    currentAddress = "4001 South 700 East"
    i = 0

    for id in truck:
        print(minimumDistanceFrom(currentAddress, truck))
        currentAddress = nextPackageAddress

        # below just tells you the packages, we need to find the next closest package
        # nextlocation = str(myHash.search(truck.pop(0))) #not pop, do call min distance from, wcich will call distance betwwen, which returns minumum

    else:
        print("No more packages loaded")

print("Delivering via Truck 1")
print(packageDelivery(Truck1))
# call mindistance from with this, then miles and time, may need to call min distance again until truck is empty

# use this to update hash table when delivered, be sure to implement datetime library first

#miles and time will be different functions

print('this is for navigation. beep bop boop')
print(myHash.search(1).address) # just do myHash.search(i).fjdklsajf to find any of the data
# myHash.insert((1).status) = 'Test' #play withl this more, this is the insert ideas
# print(myHash.search(1)) will print the entire hash section