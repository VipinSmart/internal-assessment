import sqlite3

conn_animals = sqlite3.connect("animals.db")
c_animals    = conn_animals.cursor()

conn_bookings = sqlite3.connect("booking.db")
c_bookings    = conn_bookings.cursor()

conn_customers = sqlite3.connect("customer.db")
c_customers    = conn_customers.cursor()

conn_food = sqlite3.connect("food.db")
c_food    = conn_food.cursor()

#c_animals.execute("""CREATE TABLE animals(
#		name text,
#		species text,
#		breed text,
#		medical_notes text,
#		photo blob
#		)""")

#c_bookings.execute("""CREATE TABLE bookings(
#		name_of_customer text,
#		phone int,
#		email text,
#		adress text,
#		single_or_monthly text,
#		private_horse_or_not text,
#		type_of_event text,
#		date_of_event date
#		)""")

#c_customers.execute("""CREATE TABLE customers(
#		name_of_customer text,
#		phone int,
#		email text,
#		adress text
#		)""")

#c_food.execute("""CREATE TABLE food(
#		type_of_food text,
#		amount_in_storage real,
#		supplier_name text,
#		supplier_number int,
#		supplier_email text
#		)""")


#Run the program once, so it makes the tables, and then comment everything so it doesnt keep making the tables