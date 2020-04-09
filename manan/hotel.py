import random
import csv

def returnRandomPassword(password_length = 8):
    possible_characters = "abcdefghijklmnopqrstuvwxyz1234567890"
    random_character_list = [random.choice(possible_characters) for i in range(password_length)]
    random_password = "".join(random_character_list)
    return random_password

class Hotel:
    # hotel_name --> input  
    # company_id --> serialized, input
    # password --> randomize
    # email --> combination of hotel name & location
    # address --> full address
    # No_of_rooms --> randomize, accordingly create room information
    # Parking_Available --> randomize
    def __init__(self, hname, hseries, location):
        state = location[0]
        addr = location[1]
        
        self.hotel_name = hname + ": " + state
        self.company_id = "HOT" + f'{hseries:03}'
        self.password = returnRandomPassword(8)
        self.email = hname + "-" + state.replace(" ", "_") + "@gmail.com"
        self.address = addr
        self.No_of_Rooms = random.randint(5, 15)
        self.parkingBool = random.randint(0,1)

    def printInfo(self):
        print("===================")
        print(self.hotel_name)
        print(self.company_id)
        print(self.password)
        print(self.email)
        print(self.address)
        print(self.No_of_Rooms)
        print(self.parkingBool)
        print("===================")
    
    def returnList(self):
        return [self.hotel_name, self.company_id, self.password, self.email, self.address, self.No_of_Rooms, self.parkingBool]

def createHotelDatabase():
    print("Creating Database")
    hotelNames = ['Hilton', 'Hyatt', 'Marriott', 'IHG', 'Wyndham']
    with open('location.csv', newline='') as f:
        reader = csv.reader(f)
        locations = list(reader)

    def returnStates(locations):
        states = {"a"}
        for location in locations:
            state = location[1]
            states.add(state)
        states.remove("a")
        return states

    # Get all Unique States
    states = returnStates(locations)

    hotels = []
    hotelCount = 1
    for hn in hotelNames:
        for st in states:
            randi = random.randint(0, len(locations)-1)
            while(st !=  locations[randi][1]):
                randi = random.randint(0, len(locations)-1)
            newHotel = Hotel(hn, hotelCount, (st, locations[randi][4]))
            hotels.append(newHotel)
        hotelCount+=1
    # print("Hotel Count: "+ str(hotelCount))

    hotelDetails = []
    for hotel in hotels:
        hotelDetails.append(hotel.__dict__)

    toCSV = hotelDetails
    keys = toCSV[0].keys()
    with open('hotel.csv', 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(toCSV)

    print("Hotel Database Done.")

createHotelDatabase()