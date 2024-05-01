import pandas as pd

pd.options.mode.copy_on_write=True
ev_vehicles = pd.read_csv("Electric_Vehicles_NY_2024.csv",dtype={"Zip":str})

ev_vehicles = ev_vehicles.rename(columns = {"Zip": "zip"})

ev_chargers = pd.read_csv("EV_Chargers.csv",dtype={"zip":str})



vehicles_per_zip = ev_vehicles.groupby('zip').size().reset_index(name ='num_vehicles')

chargers_per_zip = ev_chargers.groupby('zip').size().reset_index(name ='num_chargers')

ny_data = pd.merge(vehicles_per_zip, chargers_per_zip, 
                       on='zip', how='outer',indicator=True)



ny_data.drop(columns = ["_merge"],inplace=True)
ny_data = ny_data.fillna(0)
is_ny1 = ny_data["zip"] == "06390"
is_ny2 = ny_data["zip"].between("10001","14905")
is_ny = is_ny1 | is_ny2
ny_data["is_ny"] = is_ny.astype(int)


non_ny_zip = ny_data[is_ny==False]
non_ny_vehicles = non_ny_zip["num_vehicles"].sum()
non_ny_chargers = non_ny_zip["num_chargers"].sum()

ny_data.to_pickle("ny_data.pkl")

print(ny_data)
print (non_ny_vehicles)
print (non_ny_chargers)







