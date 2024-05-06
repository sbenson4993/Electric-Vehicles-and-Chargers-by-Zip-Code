#Setup
import pandas as pd
pd.options.mode.copy_on_write=True

#Reading CSV File
ev_vehicles = pd.read_csv("Electric_Vehicles_NY_2024.csv",dtype={"Zip":str})

#Standardizing Zip Code Column
ev_vehicles = ev_vehicles.rename(columns = {"Zip": "zip"})

#Reading CSV File
ev_chargers = pd.read_csv("EV_Chargers.csv",dtype={"zip":str})

#Counting Number of Entries per Group
vehicles_per_zip = ev_vehicles.groupby('zip').size().reset_index(name ='num_vehicles')
chargers_per_zip = ev_chargers.groupby('zip').size().reset_index(name ='num_chargers')

#Merging Data
ny_data = pd.merge(vehicles_per_zip, chargers_per_zip, 
                       on='zip', how='outer',indicator=True)

#Dropping '_merge' Column
ny_data.drop(columns = ["_merge"],inplace=True)

#Missing Values Equal Zero
ny_data = ny_data.fillna(0)

#Creating Variables That Corresponds with NY Zip Codes
is_ny1 = ny_data["zip"] == "06390"
is_ny2 = ny_data["zip"].between("10001","14905")
is_ny = is_ny1 | is_ny2

#New Column Categorizing Zip Codes
ny_data["is_ny"] = is_ny.astype(int)

#Calculating Total Number of Vehicles and Chargers Not in NY
non_ny_zip = ny_data[is_ny==False]
non_ny_vehicles = non_ny_zip["num_vehicles"].sum()
non_ny_chargers = non_ny_zip["num_chargers"].sum()

#Saving as a Pickle File
ny_data.to_pickle("ny_data.pkl")

#Printing Information
print("\n'ny_data' File:\n\n", ny_data)
print ("\nNon-NY Vehicles:\n", non_ny_vehicles)
print ("\nNon-NY Chargers:\n", non_ny_chargers)