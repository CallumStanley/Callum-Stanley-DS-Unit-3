import requests
import json

# retrieve data from API
trucks_data = requests.get("https://www.bnefoodtrucks.com.au/api/1/trucks")
trucks_data_book = requests.get("https://www.bnefoodtrucks.com.au/api/1/bookings")
trucks_data_sites = requests.get("https://www.bnefoodtrucks.com.au/api/1/sites")

# check request status
print(trucks_data.status_code)
print(trucks_data_book.status_code)
print(trucks_data_sites.status_code)

#view data
print(trucks_data, trucks_data_book, trucks_data_sites.json())