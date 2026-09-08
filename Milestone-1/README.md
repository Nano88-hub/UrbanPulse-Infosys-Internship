# Milestone 1 — Data Acquisition, Cleaning & Dimensional Modelling

**City:** Bangalore

Collected four unconnected datasets (traffic, weather, demographic, mobility), cleaned
them to a consistent standard, solved the missing-join-key problem with a locality→zone
bridge table, and modelled the result as a star schema for Power BI.

📄 **[Read the full report →](report/REPORT.md)**

![Urban Pulse Smart Mobility Intelligence Dashboard](dashboard/Milestone-1-Dashboard.png)

## Contents

| Folder | Files |
|---|---|
| `data/` | 9 CSVs — 4 cleaned source datasets + 5 star-schema tables |
| `code/` | `Step0_Data_Cleaning.ipynb`, `build_area_zone_bridge.py`, `merge_final.py` |
| `dashboard/` | `Milestone-1-Dashboard.pbix` |
| `presentation/` | `Milestone-1-UrbanPulse.pptx` |
| `report/` | `REPORT.md` |

## Key numbers

- **8,936** traffic records enriched with demographic and mobility context
- **4** siloed datasets unified on a shared `Zone` key
- Star schema: 1 main fact table + 2 dimensions + 2 supporting fact tables

### Dashboard KPIs

| Metric | Value |
|---|---|
| Bengaluru population | 8M |
| Average temperature | 24.30 °C |
| Average traffic volume | 29.24K |
| Average trip length | 71.27 km |

## ⚠️ Before re-running the code

Both `.py` scripts hardcode `os.chdir(r"c:\infosys internship task\given data")`.
Change that line to your own path or they will fail.
