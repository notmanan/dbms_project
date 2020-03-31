import sqlite3 , csv , sys
connection = sqlite3.connect("Travel_Site2.db")
cur = connection.cursor()
sys.path.append("./database")

# Creating the Tables

connection.execute('''CREATE TABLE Airline
			(airline_name varchar(20) not null unique,
    company_id varchar(20) Primary key,
    airline_password varchar(20) not null,
    airline_email varchar(20) not null unique,
    no_of_flights int,
    head_office varchar(20));''')

connection.execute('''CREATE TABLE Bus
			(bus_name varchar(20) not null unique,
    company_id varchar(20) primary key,
    bus_password varchar(20) not null,
    bus_email varchar(20) not null unique,
    no_of_buses int,
    head_office varchar(20));''')


connection.execute('''CREATE TABLE Hotel
			(hotel_name varchar(20), 
    company_id varchar(20),
    hotel_password varchar(20) not null,
    hotel_email varchar(20) not null unique,
    hotel_address varchar(20) not null,
    no_of_rooms int,
    parking_available bit(1) not null,
    primary key(hotel_name,company_id));''')


connection.execute('''CREATE TABLE Customer
			(customer_name varchar(20) not null,
    customer_id varchar(20) primary key,
    customer_password varchar(20) not null,
    customer_email varchar(20) not null unique,
    customer_address varchar(50) not null,
    referal_code varchar(20));''')


connection.execute('''CREATE TABLE Flight_Information
			(flight_id varchar(20) primary key,
	company_id varchar(20),
	start_point varchar(20) not null,
	destination varchar(20) not null,
	capacity int not null,
	no_of_haults int default 0,
	fare float(10) not null,
	arrival_time time not null,
	departure_time time not null,
	foreign key (company_id) references Airline);''')

connection.execute('''CREATE TABLE Bus_Information
			(bus_id varchar(20) primary key,
	company_id varchar(20),
	start_point varchar(20) not null,
	destination varchar(20) not null,
	capacity int not null,
	no_of_haults int default 0,
	arrival_time time not null,
	departure_time time not null,
	foreign key (company_id) references Bus);''')

connection.execute('''CREATE TABLE Room_Information
			(room_type varchar(20) not null,
    capacity int default 2,
    fare float(10) not null,
    company_id varchar(20),
    room_id varchar(20) primary key,
    hotel_name varchar(20),
    facilities varchar(50),
    foreign key (company_id,hotel_name) references Hotel);''')

connection.execute('''CREATE TABLE Room_Facilities
			(room_type varchar(20),
    hotel_name varchar(20),
    company_id varchar(20),
    wifi bit(1) not null,
    breakfast bit(1) not null,
    hot_water bit(1) not null,
    ac bit(1) not null,
    heater bit(1) not null,
    tv bit(1) not null,
    availability int not null,
    primary key(room_type,hotel_name,company_id),
    foreign key (company_id,hotel_name) references Hotel);''')

connection.execute('''CREATE TABLE Flight_Booking
			(flight_id varchar(20),
    start_point varchar(20) not null,
    destination varchar(20) not null,
    booking_id varchar(20) primary key,
    customer_id varchar(20),
    fare float(10) not null,
    date_of_journey date not null,
    foreign key (flight_id) references Flight_Information,
    foreign key (customer_id) references Customer);''')

connection.execute('''CREATE TABLE Bus_Booking
			(bus_id varchar(20),
    start_point varchar(20) not null,
    destination varchar (20) not null,
    booking_id varchar(20) primary key,
    customer_id varchar(20),
    date_of_journey date not null,
    fare float(10) not null,
    foreign key (bus_id) references Bus_Information,
    foreign key(customer_id) references Customer);''')

connection.execute('''CREATE TABLE Room_Booking
			(company_id varchar(20),
    hotel_name varchar(20),
    address varchar(50) not null,
    booking_id varchar(20) primary key,
    customer_id varchar(20),
    room_type varchar(20) not null,
    check_in date not null,
    check_out date not null,
    no_of_guest int default 2,
    room_id varchar(20),
	  fare float(10),
    foreign key (company_id,hotel_name) references Hotel
    foreign key(customer_id) references Customer
    foreign key(room_id) references Room_Information);''')


# Populating the Tables

# Populating the Airlines Table

with open ("Flights_DBMS  - Airline.csv" , "rt") as Airline:
	data = csv.DictReader(Airline)
	to_db = [(i["Name "],i["Company_ID"],i["Password"],i["Email"],i["No_of_flights"],i["Head_office"]) for i in data]

connection.executemany("insert into Airline(airline_name,company_id,airline_password,airline_email,no_of_flights,head_office) values(?,?,?,?,?,?);",to_db)

#Populating the Flight_Information table

with open ("Flights_DBMS  - Flight_information .csv" , "rt") as Flight_info:
	data = csv.DictReader(Flight_info)
	to_db = [(i["Flight_ID"],i["Company_ID"],i["Start_point"],i["Destination"],i["Capacity"],i["No_of_haults"],i["Fare"],i["Arrival_time "],i["Depart_time"]) for i in data]

connection.executemany("insert into Flight_information(flight_id,company_id,start_point,destination,capacity,no_of_haults,fare,arrival_time,departure_time) values(?,?,?,?,?,?,?,?,?);",to_db)
		
#Popolating the Bus Table

with open ("Bus_DBMS - Bus.csv" , "rt") as Bus:
	data = csv.DictReader(Bus)
	to_db = [(i["Name "],i["Company_ID"],i["Password"],i["Email"],i["No_of_buses"],i["Head_office"]) for i in data]

connection.executemany("insert into Bus(bus_name,company_id,bus_password,bus_email,no_of_buses,head_office) values(?,?,?,?,?,?);",to_db)


# # Populating the Bus_Information Table

with open ("Bus_DBMS - Bus_Information.csv" , "rt") as Bus:
	data = csv.DictReader(Bus)
	# for i in data:
	# 	print(i)
	to_db = [(i["Bus_ID"],i["Company_ID"],i["Start_point"],i["Destination"],i["Capacity"],i["No_of_haults"],i["Arrival_time "],i["Depart_time"]) for i in data]

connection.executemany("insert into Bus_Information(bus_id,company_id,start_point,destination,capacity,no_of_haults,arrival_time,departure_time) values(?,?,?,?,?,?,?,?);",to_db)


# Populating the Hotel Table

with open ("Hotel_DBMS - Hotel.csv" , "rt") as Hotel:
	data = csv.DictReader(Hotel)
	to_db = [(i["Hotel_Name"],i["Company_id"],i["Password"],i["Email"],i["Address"],i["No_of_Rooms"],i["Parking_Available"]) for i in data]

connection.executemany("insert into Hotel(hotel_name,company_id,hotel_password,hotel_email,hotel_address,no_of_rooms,parking_available) values(?,?,?,?,?,?,?);",to_db)


# #Populating the Room_Information Table

with open ("Hotel_DBMS - Room Information.csv" , "rt") as Hotel:
	data = csv.DictReader(Hotel)
	to_db = [(i["Room_Type"],i["Capacity"],i["Fare"],i["Company_Id"],i["Room_id"],i["Hotel_Name"],i["Facilities"]) for i in data]

connection.executemany("insert into Room_Information(room_type,capacity,fare,company_id,room_id,hotel_name,facilities) values(?,?,?,?,?,?,?);",to_db)

# Populating the Room_Facilities Table

with open ("Hotel_DBMS - Room Facilities.csv" , "rt") as Hotel:
	data = csv.DictReader(Hotel)
	to_db = [(i["Room_Type"],i["Hotel_Name"],i["Company_Id"],i["Wifi"],i["Breakfast"],i["Hot_Water"],i["AC"],i["Heater"],i["TV"],i["Availability"]) for i in data]

connection.executemany("insert into Room_Facilities(room_type,hotel_name,company_id,wifi,breakfast,hot_water,ac,heater,tv,availability) values(?,?,?,?,?,?,?,?,?,?);",to_db)


#Populating the Customer Table

with open ("Hotel_DBMS - Customer Information.csv" , "rt") as Customer:
	data = csv.DictReader(Customer)
	to_db = [(i["Name"],i["Customer_Id"],i["Password"],i["Email"],i["Address"],i["Referal Code"]) for i in data]

connection.executemany("insert into Customer(customer_name,customer_id,customer_password,customer_email,customer_address,referal_code) values(?,?,?,?,?,?);",to_db)


# Populating the Flight_Booking Table


with open ("Bookings_DBMS - Flight_Booking.csv" , "rt") as booking:
	data = csv.DictReader(booking)
	to_db = [(i["Flight_id"],i["Start_Point"],i["Destination"],i["Booking_id"],i["Customer_id"],i["Fare"],i["Date_of_journey"]) for i in data]

connection.executemany("insert into Flight_Booking(flight_id,start_point,destination,booking_id,customer_id,fare,date_of_journey) values(?,?,?,?,?,?,?);",to_db)

#Populating the Bus_Booking Table

with open ("Bookings_DBMS - Bus_Booking.csv" , "rt") as booking:
	data = csv.DictReader(booking)
	to_db = [(i["Bus_id"],i["Start_Point"],i["Destination"],i["Booking_id"],i["Customer_id"],i["Date_of_journey"],i["Fare"]) for i in data]

connection.executemany("insert into Bus_Booking(bus_id,start_point,destination,booking_id,customer_id,date_of_journey,fare) values(?,?,?,?,?,?,?);",to_db)

#Populating the Room_Booking Table

with open ("Bookings_DBMS - Room_Booking.csv" , "rt") as booking:
	data = csv.DictReader(booking)
	to_db = [(i["Company_id"],i["Hotel_name"],i["Address"],i["Booking_id"],i["Customer_id"],i["Fare"],i["Room_type"],i["Check_in"],i["Check_out"],i["No_of_guests"],i["Room_id"]) for i in data]

connection.executemany("insert into Room_Booking(company_id,hotel_name,address,booking_id,customer_id,fare,room_type,check_in,check_out,no_of_guest,room_id) values(?,?,?,?,?,?,?,?,?,?,?);",to_db)
# cur.execute("select * from Airline")
# airlines = cur.fetchall()
# for row in airlines:
# 	print(row)

connection.commit()

