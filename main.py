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
            print(pAddress) # prints address only for each key

            myHash.insert(pID, p)  # insert data into hash table

myHash = ChainingHashTable()

loadPackageData('WGUPSPackageData.csv')

print("Package info:") # hash table header

for i in range(len(myHash.table)):
    print("Package: {}".format(myHash.search(i))) #print each line of package data



# import Data table into list of lists. Data is also inverted so all cells are filled
with open('distanceTable.csv', 'r') as distanceData:
    csv_reader = csv.reader(distanceData)
    distanceData = list(csv_reader)
print(distanceData)
distanceDataFloat = [[float(x) for x in e] for e in distanceData]

'''
for element in distances:
    print(element)
'''


# input addressdata as list, include only address itself
with open('addressdata.csv', 'r') as addressData:
    csv_reader = csv.reader(addressData)
    addressData = list(csv_reader)


def distanceBetween(address1, address2):
        return distanceData[addressData.index(address1)][addressData.index(address2)]



def minimumDistance(fromAddress, truck):

    return distanceBetween()




'''use in. Set the value to a row, then use in to search for that row in distanceTable'''



def test(fromAddress, truck):
    i = -1
    x = -1
    for row in addressData: # find row with matching address, iterate i, and return i as key for distancedata
        i += 1
        for field in row:
            if field == fromAddress:
                milesList = distanceDataFloat[i]
                milesList= sorted(milesList, key = lambda x:float(x)) # sort acsending
                milesList.remove(0) # remove 0.0
                minDistance = milesList.pop(0) # set lowest non-zero distance as min
                print(minDistance) # test for accuracy

                minDistanceIndex = distanceDataFloat[i].index(minDistance) # find index of min distance
                print(minDistanceIndex) # test

                nextAddress = addressData[minDistanceIndex][2]
                print(nextAddress)
                # find address of index of min distance. if not found, look at next smallest

                for id in truck:
                    if myHash.search(id) is not None:
                        # print(myHash.search(id))
                        if nextAddress == myHash.search(id).address:
                            return distanceBetween(fromAddress, nextAddress)




            else: # if address not found, continue. may need to include break option....
                continue

'''
def truckTest(truck):
    for id in truck:
        if myHash.search(id) is not None:
            # print(myHash.search(id))
            return (myHash.search(id).address)
'''


# do the above, but loop through all packages on a truck and find min address for ALL packages, just like
# above, but more focused on the truck. Then the new address becomes from address, but that might be in deliver function
# then you can work on deliver class


# minimumDistance(HUB, 1)
# minimum distance from. Iterate through a row to find the least address
# track minimum distance: take from object and look through all truck package addressess and finds minimum distances by calling
# distancebetween you want to find minimum distance address IN THAT TRUCK
# track where you are at





Truck1 = [
"Truck 1 Packages:", 0, 1, 3, 4, 6, 7, 9, 12, 13, 15, 19, 25, 28, 29, 30, 33
]

Truck2 = [
"Truck 2 Packages:", 2, 5, 10, 11, 14, 16, 17, 18, 20, 21, 22, 24, 27, 31, 35, 37
]

Unloaded = [
"Unloaded:", 8, 25, 26, 32, 34, 36, 38
]

test('3365 S 900 W', Truck2)

print("\nCurrent package loading status: \n")
print(Truck1, "\n")
print(Truck2, "\n")
if Unloaded == ["Unloaded:"]:
    print("there are no more packages to load.\n")
else:
    print(Unloaded, "\n")






def packageDelivery(truck):
    DistanceTraveled = 0
    currentAddress = "HUB"
    i = 0
# call minimum distance from packages in the truck
    for id in truck: #loop through package ids, not the amount of packages
        return
        # below just tells you the packages, we need to find the next closest package
        # nextlocation = str(myHash.search(truck.pop(0))) #not pop, do call min distance from, wcich will call distance betwwen, which returns minumum

    else:
        print("No more packages loaded")

print("Delivering via Truck 1")
packageDelivery(Truck1)


# use this to update hash table when delivered, be sure to implement datetime library first

#miles and time will be different functions

print('this is for navigation. beep bop boop')
print(myHash.search(1).address) # just do myHash.search(i).fjdklsajf to find any of the data
# myHash.insert((1).status) = 'Test' #play withl this more, this is the insert ideas
# print(myHash.search(1)) will print the entire hash section

