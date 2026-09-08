import pandas as pd
import os

os.chdir(r"c:\infosys internship task\given data")

traffic = pd.read_csv("traffic_weather_cleaned.csv")
mobility_zone = pd.read_csv("mobility_zone_cleaned.csv")
demo = pd.read_excel("demographic_cleaned_final.xlsx")
bridge = pd.read_csv("area_to_zone_bridge.csv")
stops = pd.read_csv("stops_with_zone.csv")
routes = pd.read_csv("routes_clean.csv")
route_zone = pd.read_csv("route_zone_mapping.csv")

fact_traffic = traffic.merge(bridge, left_on="Area Name", right_on="Area_Name", how="left")
fact_traffic = fact_traffic.drop(columns=["Area_Name"])
print(f"fact_traffic Zone match rate: {fact_traffic['Zone'].notna().mean()*100:.1f}%")

zone_to_subdistrict = {
    "Bangalore East": "Bangalore East", "Bommanahalli": "Bangalore South",
    "Bangalore South": "Bangalore South", "Mahadevapura": "Bangalore East",
    "Byatarayanapura": "Bangalore North", "Dasarahalli": "Bangalore North",
    "Bangalore West": "Bangalore North", "Rajarajeshwari Nagara": "Bangalore South",
    "Bangalore North Taluk (BIAAPA)": "Area not under any Sub-district",
    "Devanahalli Taluk (BIAAPA)": "Area not under any Sub-district",
    "Doddaballapura Taluk (BIAAPA)": "Area not under any Sub-district",
}
mobility_zone["Sub_District"] = mobility_zone["Zone"].map(zone_to_subdistrict)
demo_subdist = demo[(demo["area_level"] == "Sub-District") & (demo["area_type"] == "Total")][
    ["area_name_clean", "num_households", "total_population_persons",
     "total_workers_persons", "literate_population_persons"]]
dim_zone = mobility_zone.merge(demo_subdist, left_on="Sub_District", right_on="area_name_clean", how="left").drop(columns=["area_name_clean"])
print(f"dim_zone demographic match rate: {dim_zone['total_population_persons'].notna().mean()*100:.1f}%")

fact_transit_routes = routes.merge(route_zone, on="route_id", how="left")

fact_traffic["Date"] = pd.to_datetime(fact_traffic["Date"], errors="coerce")
dim_date = pd.DataFrame({"Date": pd.date_range(fact_traffic["Date"].min(), fact_traffic["Date"].max(), freq="D")})
dim_date["Year"] = dim_date["Date"].dt.year
dim_date["Month"] = dim_date["Date"].dt.month_name()
dim_date["Day_of_Week"] = dim_date["Date"].dt.day_name()
dim_date["Is_Weekend"] = dim_date["Day_of_Week"].isin(["Saturday", "Sunday"])

fact_traffic.to_csv("fact_traffic.csv", index=False)
dim_zone.to_csv("dim_zone.csv", index=False)
dim_date.to_csv("dim_date.csv", index=False)
stops.to_csv("fact_transit_stops.csv", index=False)
fact_transit_routes.to_csv("fact_transit_routes.csv", index=False)

print("\nDONE. Saved: fact_traffic.csv, dim_zone.csv, dim_date.csv, fact_transit_stops.csv, fact_transit_routes.csv")