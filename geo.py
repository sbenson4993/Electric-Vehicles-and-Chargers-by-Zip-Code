import pandas as pd
import geopandas as gpd

ny_data = pd.read_pickle("ny_data.pkl")

zip_codes_gdf = gpd.read_file("cb_2020_us_zcta520_500k.zip")
states = gpd.read_file ("cb_2020_us_state_500k.zip")
nys = states.query("STATEFP == '36'")
nyszips = zip_codes_gdf.clip(nys,keep_geom_type=True)
nyszips.to_file("nyzips.gpkg")

ny_data = nyszips.merge(ny_data,left_on="ZCTA5CE20",right_on="zip",
                        indicator=True, how="outer")

rightonly = ny_data[ny_data["_merge"]=="right_only"]
grouped = rightonly.groupby("is_ny")
totals = grouped[["num_vehicles","num_chargers"]].sum()
print(ny_data["_merge"].value_counts())
ny_data = ny_data.drop(columns="_merge")
output_gpkg_path = 'ny_data.gpkg'

ny_data.to_file(output_gpkg_path)
