#Setup
import pandas as pd

#Reading CSV File
vehicles = pd.read_csv("Vehicle__Snowmobile__and_Boat_Registrations_20240402.csv", dtype={"Zip":str})

#Selecting Corresponding Columns (Vehicles and Electric)
vehicles = vehicles[vehicles['Fuel Type'] == 'ELECTRIC']
vehicles = vehicles[vehicles['Record Type'] == 'VEH']

#Converting to CSV
vehicles.to_csv("Electric_Vehicles_NY_2024.csv",index=False)

