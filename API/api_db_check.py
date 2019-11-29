import requests
import json
import sqlite3

DB_FILE = "food_trucks.db"
def jprint(obj):
    # Display formatted data only if retrieval is successful
    if obj.status_code == 200:
        print(json.dumps(obj.json(), indent=4))
    # If retrieval not successful, display error number
    else:
        print(obj.status_code, "error in retrieving API")

def create_table(filename, tablename, sqlcommand):
    #connect to database file (will create it if not existing)
    with sqlite3.connect(filename) as database:
        cursor = database.cursor()

        # remove previous table and data
        cursor.execute(f"DROP TABLE IF EXISTS {tablename};")

        #create empty table
        cursor.execute(sqlcommand)

# ---- Main Program ----
# retrieve data from API
trucks_data = requests.get("https://www.bnefoodtrucks.com.au/api/1/trucks")
book_data = requests.get("https://www.bnefoodtrucks.com.au/api/1/bookings")
sites_data = requests.get("https://www.bnefoodtrucks.com.au/api/1/sites")

# display formatted data 
jprint(trucks_data)
jprint(book_data)
jprint(sites_data)

#--- create database tables ---
#trucks table
create_trucks = """
                CREATE TABLE Trucks(
                    truck_id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    category TEXT NOT NULL,
                    website TEXT);
                    """

# BOOKINGS table 
create_bookings = """
	            CREATE TABLE Bookings (
                    Bookings_id INTEGER PRIMARY KEY,
	                Site_id INTEGER NOT NULL,
	                Truck_id INTEGER NOT NULL,
	                Start STRING NOT NULL,
	                Finish STRING NOT NULL);
                    """

# SITES TABLE
create_sites = """
                CREATE TABLE Sites (
	                site_id INTEGER PRIMARY KEY,
	                Street TEXT NOT NULL,
	                suburb TEXT NOT NULL,
	                postcode TEXT NOT NULL,
	                Latitude TEXT NOT NULL,
	                Longitude TEXT NOT NULL);
                    """


create_table(DB_FILE, "Trucks", create_trucks)
create_table(DB_FILE, "Sites", create_sites)
create_table(DB_FILE, "Bookings", create_bookings)