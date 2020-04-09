# import random
# from faker import Faker
# from faker.providers import geo
# import reverse_geocoder as rg
# import requests
# import time

# # def isEnglish(ss):
# #     for s in ss:
# #         try:
# #             s.encode(encoding='utf-8').decode('ascii')
# #         except UnicodeDecodeError:
# #             return False
# #     return True
    
# fake =  Faker()
# # fake.add_provider(geo)
# # key = 'fa23d8a876704d'
# # locations = []
# # for i in range(0,1000):
# #     print(i)
# #     loc = fake.local_latlng(country_code='IN')
# #     lat = float(loc[0])
# #     lng = float(loc[1])
# #     URL = "https://us1.locationiq.com/v1/reverse.php?key=" + str(key)+ "&lat=" + str(lat) + "&lon=" + str(lng) + "&format=json"
# #     time.sleep(0.7)
# #     r = requests.get(url = URL)
# #     data = r.json()
# #     # print(data)
# #     try:
# #         err = data['error']
# #         if(err == "Rate Limited Second"):
# #             print("Sleeping 1")
# #             time.sleep(1)
# #         elif(err == "Rate Limited Minute"):
# #             print("Sleeping 60")
# #             time.sleep(60)
# #         data = requests.get(url = URL).json()
# #     except:
# #         lol = 1
# #     addr = data['address']
# #     appenders = [data['place_id'],
# #     addr['state'],
# #     data['lat'],
# #     data['lon'],
# #     data['display_name']
# #     ]
# #     if(isEnglish(appenders)):
# #         locations.append(appenders)
# #     else:
# #         print("Not Appended: " + str(appenders))



# # # for i in range(len(locations)):
# # #     loc = locations[i]
# # #     print(loc)
# # #     for info in loc:
# # #         if(not isEnglish(info)):
# # #             locations.remove(loc)
# # #             i-=1
# # #             print("Removed")
# # #             break

# # # print("\n\n\n\n")
# # # print(locations)

# # for l in locations:
# #     print(l)

# # import csv
# # with open('people.csv', 'w', newline='') as file:
# #     writer = csv.writer(file)
# #     writer.writerow(["PlaceID", "State", "Latitude", "Longitude",  "Address"])
# #     for l in locations:
# #         writer.writerow(l)










# # # # def returnRandomPassword(password_length = 8):
# # # #     possible_characters = "abcdefghijklmnopqrstuvwxyz1234567890"
# # # #     random_character_list = [random.choice(possible_characters) for i in range(password_length)]
# # # #     random_password = "".join(random_character_list)
# # # #     return random_password

# # # # def returnEmailID(beginStr):
# # # #     return beginStr + "-admin@gmail.com"

# # # # hotelNames = ['Hilton', 'Hyatt', 'Marriott', 'IHG', 'Wyndham']
# # # # hotelIDs = {}
# # # # count = 1

# # # # for hotel in hotelNames:
# # # #     hotelIDs[hotel] = "HOT" + f'{count:03}'
# # # #     count +=1
# # # # print(hotelIDs)


# import csv

# with open('location1.csv', newline='') as f:
#     reader = csv.reader(f)
#     data = list(reader)

# locations = data
# print(len(locations))
# newLoc = {}
# for location in locations:
#     newLoc[location[0]] = location[1:]
#     # print(newLoc)
#     # break

# print(len(newLoc.keys()))
# del newLoc["PlaceID"]
# finalLocations = []
# for id in newLoc.keys():
#     finalLocations.append([id, newLoc[id][0], newLoc[id][1], newLoc[id][2], newLoc[id][3]])

# print(len(finalLocations))
# print(finalLocations[0])

# with open('location.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(["PlaceID", "State", "Latitude", "Longitude",  "Address"])
#     for l in finalLocations:
#         writer.writerow(l)