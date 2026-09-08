import pandas as pd
import os

# Set this to wherever you're saving your project files
os.chdir(r"c:\infosys internship task\given data")

locality_to_zone = {
    "Indiranagar":     "Bangalore East",
    "M.G. Road":       "Bangalore East",
    "Koramangala":     "Bommanahalli",
    "Jayanagar":       "Bangalore South",
    "Whitefield":      "Mahadevapura",
    "Electronic City": "Bommanahalli",
    "Hebbal":          "Byatarayanapura",
    "Yeshwanthpur":    "Dasarahalli",
}

bridge = pd.DataFrame([
    {"Area_Name": k, "Zone": v} for k, v in locality_to_zone.items()
])

bridge.to_csv("area_to_zone_bridge.csv", index=False)
print("Saved area_to_zone_bridge.csv")
print(bridge)