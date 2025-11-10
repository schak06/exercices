import mysql.connector

# Connect to the database
connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="said2006",
    database="flight_game"
)
#Task 1:
cursor = connection.cursor()

icao = input("Enter ICAO code: ").upper()

query = "SELECT name, municipality FROM airport WHERE ident = %s"
cursor.execute(query, (icao,))
result = cursor.fetchone()

if result:
    print(f"Airport name: {result[0]}, Location: {result[1]}")
else:
    print("No airport found with that ICAO code.")

cursor.close()
connection.close()

#Task 2:
import mysql.connector

connection = mysql.connector.connect(
         host="localhost",
         port= 3306,
         database="flight_game",
         user="root",
         password="said2006",
         autocommit=True
         )

cursor = connection.cursor()

country_code = input("Enter area code (e.g., FI): ").upper()

cursor.execute(f"select type, count(*) from airport where iso_country = '{country_code}' group by type")

airports_sorted_by_type = cursor.fetchall()
for airport_type, number in airports_sorted_by_type:
    print(f'The country has a total of: {number} {airport_type} ')

#Task 3:
import mysql.connector
from geopy.distance import geodesic

connection = mysql.connector.connect(
    host="localhost",
    port= 3306,
    user="root",
    password="said2006",
    database="flight_game"
)

cursor = connection.cursor()

icao1 = input("Enter first ICAO code: ").upper()
icao2 = input("Enter second ICAO code: ").upper()

query = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s"


cursor.execute(query, (icao1,))
coords1 = cursor.fetchone()


cursor.execute(query, (icao2,))
coords2 = cursor.fetchone()

if coords1 and coords2:
    distance = geodesic(coords1, coords2).kilometers
    print(f"Distance between {icao1} and {icao2}: {distance:.2f} km")
else:
    print("One or both ICAO codes not found.")

cursor.close()
connection.close()
