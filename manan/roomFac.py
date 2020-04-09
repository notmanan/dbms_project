import random
import csv

class roomFacilities:
    # roomType --> Currently Randomized, decided the rest of the room features
    # Hotel_Name -> inherited
    # Company_ID -> inherited
    # Wifi -> from roomType
    # Breakfast -> from roomType
    # Hot_Water -> from roomType
    # AC -> from roomType
    # Heater -> from roomType
    # Tv -> from roomType
    # Availability -> from roomType

    def __init__(self, hn, cid, roomi):
        # roomTypes = ["1-Star", "2-Star", "3-Star", "4-Star", "5-Star", "6-Star"]
        # roomFeatures = [[1,0,0,0,0,0], 
        #                 [1,1,0,0,0,0], 
        #                 [1,1,0,1,0,0], 
        #                 [1,1,1,1,0,0], 
        #                 [1,1,1,1,1,0], 
        #                 [1,1,1,1,1,1]]
        features = [random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1)]
        while(sum(features)!= roomi):
            features = [random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1)]
        self.roomType = str(sum(features)) + " - Star Room"
        self.Hotel_Name = hn
        self.Company_ID = cid
        self.Wifi = features[0]
        self.Breakfast = features[1]
        self.Hot_Water = features[2]
        self.AC = features[3]
        self.Heater = features[4]
        self.Tv = features[5]
        self.Availability = 1

    def returnList(self):
        return([self.roomType,
                self.Hotel_Name, 
                self.Company_ID,
                self.Wifi,
                self.Breakfast,
                self.Hot_Water,
                self.AC ,
                self.Heater, 
                self.Tv, 
                self.Availability])

def createRoomFacilityDataset():
    print("Creating Database")
    with open('hotel.csv', newline='') as f:
        reader = csv.reader(f)
        hotels = list(reader)
    
    hotels = hotels[1:]

    roomFacilitiesList = []
    for hotel in hotels:
        for rt in range(1,7):
            newRoomFac = roomFacilities(hotel[0], hotel[1], rt)
            roomFacilitiesList.append(newRoomFac.__dict__)

    toCSV = roomFacilitiesList
    keys = toCSV[0].keys()
    with open('roomFacilities.csv', 'w', newline= '') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(toCSV)
    
    print("Room Facility Database Done.")

createRoomFacilityDataset()