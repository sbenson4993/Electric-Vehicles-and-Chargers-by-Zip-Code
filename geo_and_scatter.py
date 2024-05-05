#Setup
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt


#Reading Pickle File
ny_data = pd.read_pickle("ny_data.pkl")

#Reading Shapefile Containing Zip Code Boundaries
zip_codes_gdf = gpd.read_file("cb_2020_us_zcta520_500k.zip")

#Reading Shapefile Containing State Boundaries
states = gpd.read_file ("cb_2020_us_state_500k.zip")

#Isolating NY State
nys = states.query("STATEFP == '36'")

#Clipping NY State Boundaries
nyszips = zip_codes_gdf.clip(nys,keep_geom_type=True)

#Saving as a GeoPackage
nyszips.to_file("nyzips.gpkg")

#Merging 'nyszips' with 'ny_data'
ny_data = nyszips.merge(ny_data,left_on="ZCTA5CE20",right_on="zip",
                        indicator=True, how="outer")

#Selecting Rows from 'ny_data' that are 'right_only'
rightonly = ny_data[ny_data["_merge"]=="right_only"]

#Grouping 'right_only' and Calculating Sum
grouped = rightonly.groupby("is_ny")
totals = grouped[["num_vehicles","num_chargers"]].sum()
print("Shares and Separate Values Appearing in the DataFrames:\n",ny_data["_merge"].value_counts())
print ("\nVehicles and Chargers with Out of State or Unmappable Zip Codes:\n", totals)

#Drop _merge Column
ny_data = ny_data.drop(columns="_merge")

#Calculating Averages per Zip Code
mean_vehicles = ny_data["num_vehicles"].mean()
mean_chargers = ny_data["num_chargers"].mean()
print ("\nAverage Vehicles per Zip Code:\n", mean_vehicles)
print ("\nAverage Chargers per Zip Code:\n", mean_chargers)

#Above Average Columns (1 = Yes, 0 = No)
ny_data['vehicles_above_average'] = (ny_data['num_vehicles'] > mean_vehicles).astype(int)
ny_data['chargers_above_average'] = (ny_data['num_chargers'] > mean_chargers).astype(int)

#Column Categorizing Zip Code
#(0 = Below Average Chargers and Vehicles, 1 = Above Average Chargers and Below Average Vehicles,
#2 = Below Average Chargers and Above Average Vehicles, 3 = Above Average Vehicles and Chargers) 
ny_data["average_category"] = ny_data['vehicles_above_average']*2 + ny_data['chargers_above_average']

#Saving 'ny_data' as a GeoPackage
output_gpkg_path = 'ny_data.gpkg'
ny_data.to_file(output_gpkg_path)

#Reprojecting
ny_data = ny_data.to_crs(26918)
ny_data["chargers_per_square_kilometer"] = ny_data["num_chargers"] / (ny_data.area/1e6)
ny_data["vehicles_per_square_kilometer"] = ny_data["num_vehicles"] / (ny_data.area/1e6)

#Mean per Square Kilometer
mean_chargers_per_square_km = ny_data["chargers_per_square_kilometer"].mean()
mean_vehicles_per_square_km = ny_data["vehicles_per_square_kilometer"].mean()
print ("\nMean Chargers per Square Kilometer:\n",mean_chargers_per_square_km)
print ("\nMean Vehicles per Square Kilometer:\n",mean_vehicles_per_square_km)


#Scatter Plot Creation
fig1,ax1 = plt.subplots()
ny_data.plot.scatter(x="chargers_per_square_kilometer",y="vehicles_per_square_kilometer", ax=ax1)
plt.axvline(x=mean_chargers_per_square_km, color='red', linestyle='--', label='Mean Chargers per Square Kilometer')
plt.axhline(y=mean_vehicles_per_square_km, color='blue', linestyle='--', label='Mean Vehicles per Square Kilometer')
plt.xlabel('Chargers per Square Kilometer')
plt.ylabel('Vehicles per Square Kilometer')
plt.title('Vehicles and Chargers per Square Kilometer')
plt.legend()
plt.show()
fig1.tight_layout()
fig1.savefig("Vehicles_and_Chargers_per_Square_Kilometer.png",dpi=300)

