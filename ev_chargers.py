#Setup
import requests
import pandas as pd

#API Code
api = "https://developer.nrel.gov/api/alt-fuel-stations/v1.json"

#Key Value
key_value = "QSck3raybMQr0u5jKeTlyYfmgbvljebG1dTa08eZ"

#Dictionary for Parameters 
payload = {'api_key': key_value,'state': 'NY','fuel_type': 'ELEC'}

#GET Request
response = requests.get(api,payload)

#Checking Response Code
if response.status_code != 200:
    print('\nStatus Code:')
    print(response.status_code)
    print('\nResponse Text:')
    print(response.text)
    assert False
  
#Converting JSON Response to Dictionary
response_dictionary = response.json()

#Value of Stations
stations = response_dictionary["fuel_stations"]

#Stations into Variable
ev_chargers = pd.DataFrame(stations)

#CSV Creation
ev_chargers.to_csv('EV_Chargers.csv',index=False)