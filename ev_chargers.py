import requests
import pandas as pd

#API Code
api = "https://developer.nrel.gov/api/alt-fuel-stations/v1.json"

#Key Value
key_value = "QSck3raybMQr0u5jKeTlyYfmgbvljebG1dTa08eZ"

#Dictionary
payload = {'api_key': key_value,'state': 'NY','fuel_type': 'ELEC'}

response = requests.get(api,payload)
if response.status_code != 200:
    print('\nStatus Code:')
    print(response.status_code)
    print('\nResponse Text:')
    print(response.text)
    assert False
  

response_dictionary = response.json()
stations = response_dictionary["fuel_stations"]

#Stations into Variable
ev_chargers = pd.DataFrame(stations)

#CSV Creation
ev_chargers.to_csv('EV_Chargers.csv',index=False)