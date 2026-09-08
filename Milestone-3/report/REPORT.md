# Milestone 3 — Demand Forecasting & Mode Substitution Analysis

**Project:** UrbanPulse — Smart City Mobility Intelligence Platform
**City studied:** Visakhapatnam (Vizag)
**Deliverables:** demand forecast dashboard, mode substitution dashboard

---

## 1. Objective

Milestones 1 and 2 described the network as it *is*. Milestone 3 turned to prediction
and behaviour, asking two questions:

1. **Can ride demand be forecast**, and does vehicle supply match it?
2. **What happens to demand when the weather changes** — specifically, what happens to
   ride-hailing demand during rainy periods?

## 2. Datasets

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

## 3. Finding 1 — Mode substitution is driven by rain

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

## 4. Finding 2 — Demand and supply are broadly matched

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

## 5. Dashboards

| File | Contents |
|---|---|
| [`../dashboard/Demand-Forecast.pbix`](../dashboard/Demand-Forecast.pbix) | Weather analysis, forecast by location, ride demand trend, forecast demand, demand vs supply by hour |
| [`../dashboard/Demand-Forecast.png`](../dashboard/Demand-Forecast.png) | Screenshot |
| [`../dashboard/Model-Substitution.pbix`](../dashboard/Model-Substitution.pbix) | Demand by weather × mode, bike vs cab comparison, total demand by mode, hourly demand by mode |
| [`../dashboard/Model-Substitution.png`](../dashboard/Model-Substitution.png) | Screenshot |

Both dashboards include a zone slicer for filtering to individual areas.

---

## 6. Recommendations

| Priority | Action | Evidence |
|---|---|---|
| **High** | Trigger cab fleet repositioning on rain forecasts | Cab demand +56% in rain while bike demand hits zero |
| **High** | Raise Gajuwaka's vehicle buffer | Second-highest demand on the thinnest margin (+0.22) |
| Medium | Rebalance deployment towards off-peak | Off-peak carries 59% of ride requests |
| Medium | Treat bike/auto capacity as weather-contingent | Both modes collapse in rain; holding fleet idle wastes supply |

---

## 7. Limitations

- **80 rows per dataset is a small sample.** Weather × mode cells contain few
  observations each, so exact figures should be read as directional, not precise.
- Bike demand of exactly **0** in rain is suspiciously clean for real-world data and
  may reflect how the dataset was constructed rather than true rider behaviour.
- The two datasets cover different `Demand` definitions and should not be summed together.
- The datasets were supplied already cleaned, so no cleaning code exists for this
  milestone. Modelling was done inside Power BI, which means the transformation logic
  is not reproducible outside the `.pbix` files.
