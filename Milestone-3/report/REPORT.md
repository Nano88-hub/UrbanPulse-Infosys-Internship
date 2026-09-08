# Milestone 3 — Demand Forecasting & Mode Substitution Analysis

**Project:** UrbanPulse — Smart City Mobility Intelligence Platform
**City studied:** Visakhapatnam (Vizag)
**Deliverables:** demand forecast dashboard, mode substitution dashboard

---

## 1. Problem statement

> Transportation demand varies significantly based on transportation mode, weather
> conditions, location and time. These variations influence the choice of transportation
> mode and can lead to a possible shift in user preference from one mode to another.
>
> Understanding these patterns helps in demand forecasting, identifying mode
> substitution behaviour and supporting better mobility planning.

## 2. Objectives

| # | Objective | Description |
|---|---|---|
| 1 | **Compare transportation modes** | Analyse and compare demand across Auto, Bike and Cab |
| 2 | **Analyse weather impact** | Evaluate how Sunny, Rainy, Windy and Cloudy conditions affect demand |
| 3 | **Identify possible substitution** | Compare Bike and Cab demand under different weather to find substitution patterns |
| 4 | **Analyse peak hours** | Identify high-demand hours per mode to support planning and resource allocation |

## 3. Datasets

| File | Rows | Purpose |
|---|---:|---|
| `../data/Vizag_Forecasting_Dataset_80.xlsx` | 80 | Demand forecasting & supply gap |
| `../data/PowerBI_Model_Substitution_80.xlsx` | 80 | Mode choice under different weather |

**Shared dimensions:** 4 zones (Dwaraka Nagar, Gajuwaka, MVP Colony, Seethammadhara),
4 weather states (Sunny, Cloudy, Rainy, Windy), 3 transport modes (Auto, Bike, Cab),
Peak / Off-Peak time slots, weekday / weekend.

The forecasting dataset additionally carries `Ride_Requests`, `Available_Vehicles`,
`Expected_Demand` and a derived `Supply_Demand_Gap`.

---

## 4. Finding 1 — Mode substitution is driven by rain

This is the central result of the milestone.

**Total demand by weather and transport mode:**

| Weather | Auto | Bike | Cab | Total |
|---|---:|---:|---:|---:|
| Sunny | 43 | 35 | 32 | 110 |
| Cloudy | 20 | 6 | 16 | 42 |
| Windy | 26 | 15 | 16 | 57 |
| **Rainy** | **13** | **0** | **50** | **63** |

### What happens to ride-hailing demand during rain

**Cab demand rises to 50 — the highest single value in the entire matrix — while
bike demand falls to exactly zero.**

Compared with sunny conditions:

| Mode | Sunny | Rainy | Change |
|---|---:|---:|---|
| Bike | 35 | 0 | **−100%** (total collapse) |
| Auto | 43 | 13 | −70% |
| Cab | 32 | 50 | **+56%** |

This is **mode substitution**, not demand destruction. Total demand only falls from
110 to 63, but its composition changes completely: riders abandon open-air modes
(bike, auto) and switch to enclosed ones (cab). Rain does not stop people travelling —
it changes *how* they travel.

**Overall totals:** Cab 114, Auto 102, Bike 56. Cab leads largely because of its
rainy-weather surge.

---

## 5. Finding 2 — Demand and supply are broadly matched

`Supply_Demand_Gap` = `Available_Vehicles` − `Expected_Demand`.
A positive value means spare vehicles; negative means shortage.

| Zone | Total gap | Mean gap | Ride requests |
|---|---:|---:|---:|
| Seethammadhara | +27 | +0.96 | 254 |
| Dwaraka Nagar | +14 | +0.93 | 191 |
| MVP Colony | +6 | +0.32 | 146 |
| Gajuwaka | +4 | +0.22 | 212 |

All four zones run a small surplus on average, so there is no systemic vehicle
shortage. But the surplus is unevenly distributed:

**Gajuwaka is the tightest zone in the city.** It generates the second-highest demand
(212 requests) on the thinnest buffer (+0.22 mean gap). Seethammadhara, with only
slightly more demand (254), runs more than four times the buffer (+0.96). Gajuwaka has
almost no slack when demand spikes.

### Peak vs off-peak

| Time slot | Ride requests | Available vehicles | Expected demand |
|---|---:|---:|---:|
| Off-Peak | 478 | 453 | 486 |
| Peak | 325 | 299 | 316 |

Off-peak carries **59% of total requests** — more than peak. Vehicle deployment
weighted towards traditional rush hours would misread this network.

### Demand by weather (forecasting dataset)

| Weather | Ride requests |
|---|---:|
| Sunny | 265 |
| Cloudy | 196 |
| Rainy | 186 |
| Windy | 156 |

---

## 6. Dashboards

| File | Contents |
|---|---|
| [`../dashboard/Demand-Forecast.pbix`](../dashboard/Demand-Forecast.pbix) | Weather analysis, forecast by location, ride demand trend, forecast demand, demand vs supply by hour |
| [`../dashboard/Demand-Forecast.png`](../dashboard/Demand-Forecast.png) | Screenshot |
| [`../dashboard/Model-Substitution.pbix`](../dashboard/Model-Substitution.pbix) | Demand by weather × mode, bike vs cab comparison, total demand by mode, hourly demand by mode |
| [`../dashboard/Model-Substitution.png`](../dashboard/Model-Substitution.png) | Screenshot |

Both dashboards include a zone slicer for filtering to individual areas.

---

## 7. Recommendations

| Priority | Action | Evidence |
|---|---|---|
| **High** | Trigger cab fleet repositioning on rain forecasts | Cab demand +56% in rain while bike demand hits zero |
| **High** | Raise Gajuwaka's vehicle buffer | Second-highest demand on the thinnest margin (+0.22) |
| Medium | Rebalance deployment towards off-peak | Off-peak carries 59% of ride requests |
| Medium | Treat bike/auto capacity as weather-contingent | Both modes collapse in rain; holding fleet idle wastes supply |

---

## 8. Key findings & conclusion

| # | Area | Finding |
|---|---|---|
| 1 | **Mode demand** | Cab shows the highest overall demand among the analysed modes (114 vs Auto 102, Bike 56) |
| 2 | **Weather impact** | Weather conditions measurably affect both total demand and mode preference |
| 3 | **Possible substitution** | Rainy and unfavourable conditions show a clear shift from **Bike toward Cab** |
| 4 | **Peak hours** | Modes have distinct hourly demand patterns and peak periods |
| 5 | **Mobility planning** | Results support demand forecasting, vehicle allocation, peak-hour planning and weather-based planning |

### Conclusion

Transportation demand is influenced by **mode, weather and time**. The Bike vs Cab
comparison indicates a substitution pattern under unfavourable weather, while the hourly
analysis identifies peak-demand periods.

Together these give the city a repeatable chain:

**identify peak hours → forecast demand patterns → allocate and prepare vehicles →
improved service efficiency, reduced wait times and better resource utilisation.**

## 9. Limitations

- **80 rows per dataset is a small sample.** Weather × mode cells contain few
  observations each, so exact figures should be read as directional, not precise.
- Bike demand of exactly **0** in rain is suspiciously clean for real-world data and
  may reflect how the dataset was constructed rather than true rider behaviour.
- The two datasets cover different `Demand` definitions and should not be summed together.
- The datasets were supplied already cleaned, so no cleaning code exists for this
  milestone. Modelling was done inside Power BI, which means the transformation logic
  is not reproducible outside the `.pbix` files.
