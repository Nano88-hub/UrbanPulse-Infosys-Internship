# Milestone 2 — Route Preference & Transit Performance Analysis

**City:** Visakhapatnam (Vizag)

Measured how the bus network actually performs: which routes carry the load, where
services run late, and how passenger flow distributes across the city.

📄 **[Read the full report →](report/REPORT.md)**

![Route Preference Dashboard](dashboard/Route-Preference-Dashboard.png)

## Contents

| Folder | Files |
|---|---|
| `data/` | `Vizag_Bus_Report_Simple.xlsx` (81 route-stop records) |
| `code/` | `Step2_4_Transit_Cleaning.ipynb`, `Milestone2_Transit_KPIs.ipynb` |
| `dashboard/` | Power BI `.pbix` + PNG, Tableau flow map & heat map `.twbx` |
| `presentation/` | `Milestone-2-UrbanPulse.pptx` |
| `report/` | `REPORT.md` |

## Key findings

- **Only 30.9% of services arrive on time** — average delay 2.72 min
- **16 routes**, 43 stops, 56,106 passenger movements analysed
- Worst performer: **RK Beach → Kothavalasa** (4.88 min avg delay, 4,949 passengers)
- Delay scales with route length — the 2-stop route averages 0.50 min, the 8-stop route 4.88 min
