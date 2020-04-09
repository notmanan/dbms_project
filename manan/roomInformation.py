import random
import csv

class roomInformation:
    # roomType
    # capacity
    # fare
    # hotel_name
    # room_id
    # company_id
    # facilities
    def __init__(self, rt, hn, cid, roomid):
        self.roomType = rt
        self.capacity = random.randint(1, 4)
        self.fare = random.randint(1,5)*1000
        self.hotel_name = hn
        self.room_id = f'{roomid:03}'
        self.company_id = cid
        # self.facilities = 
        
def createRoomInformation():
    print("Creating Database")
    with open('hotel.csv', newline='') as f:
        reader = csv.reader(f)
        hotels = list(reader)
    
    hotels = hotels[1:]

    with open('roomFacilities.csv', newline='') as f:
        reader = csv.reader(f)
        roomFac = list(reader)
    
    roomFac = roomFac[1:]
    roomInfoList = []
    tempRoomCount = 1
    for hotel in hotels:
        hotelName   = hotel[0]
        hotelId     = hotel[1]
        noOfRoomsInHotel = int(hotel[5])
        for num in range(0, noOfRoomsInHotel):
            hotelFacility = random.randint(1, 6)
            for facility in roomFac:
                hcheck = (hotelName, hotelId, hotelFacility)
                hcheckt = (facility[1], facility[2], int(facility[0][0]))
                if(hcheck == hcheckt):
                    roomInfoList.append(roomInformation(facility[0], hotelName, hotelId, tempRoomCount))
                    tempRoomCount +=1

    toCSV = []
    for c in roomInfoList:
        toCSV.append(c.__dict__)
    keys = toCSV[0].keys()
    with open('roomInformation.csv', 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(toCSV)
    
    # for i in roomInfoList[0:5]:
    #     print(i.__dict__)


createRoomInformation()