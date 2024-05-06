# Electric Vehicles and Chargers by Zip Code

## Purpose:
With the growing accessibility and demand for electric vehicles, there is a need to understand the strengths of the charging network to address both inefficiencies as well as any inequities. As more people rely on these  stations to charge their vehicles, they may be required to travel to areas they would not normally go or are inconvenient for them to reach. While charging from home is an option, the reliance of residents on these stations should not be discounted and understanding why traveling to these stations are inefficient is important. Knowing where these potential inefficiencies lie and finding a way to address them is important when addressing the development of future charging stations. Locations of charging stations can also result in not just inefficiencies but also inequities, preventing people from having easy access to these stations and inhibiting their ability to use their electric vehicles. Analyzing the current network in New York State is the purpose of this repository; serving as a way to highlight potential issues now while also being able to serve as a firm foundation for future analysis going forward. 

## Script Descriptions:

1. **ev_chargers.py:** The purpose of this script is to retrieve data from the National Renewable Energy Laboratory regarding locations for charging stations. By using a key value for the api, the data for New York is retrieved and a CSV file is created titled "EV_Chargers.csv" that contains all the necessary information regarding charging stations.
2. **vehicles.py:** Opposed to the "ev_chargers.py" script, this script simply reads a CSV file titled "Vehicle, Snowmobile, and Boat Registrations" obtained from Data.NY.Gov which contains all vehicle regristations in New York State. This script also pulls out information from the file and creates a new CSV file titled "Electric_Vehicles_NY_2024.csv" that contains information on every electric vehicle in the state. 
3. **vehicles_and_chargers.py:** This script merges the two CSV files that were created in the previous two scripts into a new DataFrame titled "ny_data." Zip codes not belonging to New York State are also categorized as non-NY in this script; this ensures that the data remains unchanged while also giving an indicator of what in this DataFrame is not from New York State. A new DataFrame is created to handle these zip codes from out of state, that DataFrame is titled "non_ny_zip" and is used to sum up the number of vehicles as well as chargers not from New York provided by the original data sources. With everything categorized, the "ny_data" DataFrame is converted to a pickle file for conversion to a GeoPackage. 
4. **geo_and_scatter.py:** With "ny_data" now as a pickle file, this script merges it with a new DataFrame called "nyszips" which was created using two zip files called "cb_2020_us_state_500k.zip" and "cb_2020_us_zcta520_500k.zip" both of which are from the census bureau. "nyszips" isolates the zip codes of New York along with the state boundaries so they can be used to generate a map of the state. With these DataFrames merged together, new columns can be created calculating the average number of vehicles and chargers as well as columns used to categorize these zip codes based off of their position in comparison to the averages. After categorizing the individiual zip codes, "ny_data" is converted into a GeoPackage so the information within the DataFrame can be used to create heatmaps. Besides the creation of heatmaps, the number of vehicles and chargers per square kilometer for every zip code is calculated and displayed in a scatter plot to show the where many zip codes fall when it comes to the number of vehicles and the number of chargers. While the other scripts primarily served to filter data and create DataFrames, this script serves primarily as a way to display the data for policy analysis purposes. 

## Maps and Scatter Plot: 
![num_vehicles]
(num_vehicles.png)
