# Milestone 2 — Route Preference & Transit Performance Analysis

**Project:** UrbanPulse — Smart City Mobility Intelligence Platform
**City studied:** Visakhapatnam (Vizag)
**Deliverables:** transit KPI model, Power BI route dashboard, Tableau flow map & heat map

---

## 1. Objective

Milestone 1 established *what the network looks like*. Milestone 2 asked
*how well it actually performs*: which routes carry the load, where buses run late,
and how passenger flow is distributed across the city.

The city of study moved from Bangalore to **Visakhapatnam**, using GTFS-style route,
stop and timing data.

## 2. Dataset

`../data/Vizag_Bus_Report_Simple.xlsx` — 81 route-stop records covering:

- **16 bus routes**
- **43 unique stops**
- Fields: `route_id`, `route_name`, `stop_id`, `stop_name`, `arrival_time`,
  `latitude`, `longitude`, `Passenger_Count`, `Travel_Time`, `Distance`,
  `Scheduled_Time`, `Actual_Time`

The `Scheduled_Time` / `Actual_Time` pair is what makes punctuality measurable.

## 3. Data preparation

- [`../code/Step2_4_Transit_Cleaning.ipynb`](../code/Step2_4_Transit_Cleaning.ipynb) —
  cleans the raw GTFS feed (`routes.txt`, `stops.txt`, `trips.txt`, `stop_times.txt`)
  into tabular form and assigns each stop to a zone.
- [`../code/Milestone2_Transit_KPIs.ipynb`](../code/Milestone2_Transit_KPIs.ipynb) —
  derives the performance metrics below.

## 4. Key metrics

**Delay** is defined as `Actual_Time − Scheduled_Time`, in minutes.

| Metric | Value |
|---|---|
| Routes analysed | 16 |
| Stops analysed | 43 |
| **On-time performance** (≤ 0 min late) | **30.9%** |
| Average delay across all services | 2.72 min |
| Total passenger movements recorded | 56,106 |

**Only 3 services in 10 arrive on time.** That is the headline finding of this
milestone.

## 5. Route-level results

### Busiest routes by passenger volume

| Route | Stops | Passengers | Avg delay (min) |
|---|---:|---:|---:|
| RTC Complex → Kailasagiri | 6 | 5,306 | 2.17 |
| RTC Complex → Duvvada Railway Station | 5 | 5,017 | 2.60 |
| RK Beach → Kothavalasa | 8 | 4,949 | **4.88** |
| Bheemili → Railway Station | 7 | 4,604 | 3.86 |
| Railway Station → Thagarapuvalasa | 6 | 4,215 | 2.67 |

### Least punctual routes

| Route | Avg delay (min) | Passengers |
|---|---:|---:|
| RK Beach → Kothavalasa | 4.88 | 4,949 |
| RTC Complex → Rajeev Nagar | 4.50 | 3,178 |
| Ratnagiri HB Colony → Old Post Office | 4.00 | 2,629 |
| Bheemili → Railway Station | 3.86 | 4,604 |

### Most punctual routes

| Route | Avg delay (min) |
|---|---:|
| Old Post Office → Venkojipalem | 0.50 |
| Kothavalasa → RK Beach | 1.00 |
| Vizianagaram → Anakapalli | 1.00 |

## 6. Insights

1. **Delay scales with route length.** The two worst performers — RK Beach →
   Kothavalasa (8 stops) and Bheemili → Railway Station (7 stops) — are the longest
   routes in the network. Every additional stop adds a boarding-time opportunity for
   delay to accumulate.

2. **The worst delay sits on a high-volume route.** RK Beach → Kothavalasa is both the
   3rd busiest route *and* the least punctual, so the delay is felt by ~4,949 passengers
   rather than a handful. This is the single highest-impact fix available.

3. **Short routes are reliable.** Old Post Office → Venkojipalem (2 stops) averages
   0.50 min delay, confirming that the punctuality problem is structural to long routes,
   not a system-wide scheduling fault.

4. **The RTC Complex hub dominates flow.** Three of the top-five busiest routes
   originate there, making it the network's critical node.

## 7. Recommendations

| Priority | Action | Rationale |
|---|---|---|
| **High** | Add buffer time to the schedules of RK Beach → Kothavalasa and RTC Complex → Rajeev Nagar | Highest delay on high passenger volume |
| **High** | Increase frequency on the three RTC Complex corridors | Hub carries the largest share of demand |
| Medium | Review dwell time at intermediate stops on 7–8 stop routes | Delay accumulates per stop |
| Medium | Re-baseline the timetable — 30.9% on-time suggests the schedule itself is optimistic | Padding schedules may fix more than adding vehicles |

## 8. Visualisations

| File | What it shows |
|---|---|
| [`../dashboard/Route-Preference-Dashboard.pbix`](../dashboard/Route-Preference-Dashboard.pbix) | Power BI: route preference and passenger volume |
| [`../dashboard/Route-Preference-Dashboard.png`](../dashboard/Route-Preference-Dashboard.png) | Screenshot of the above |
| [`../dashboard/vizag-flowmap.twbx`](../dashboard/vizag-flowmap.twbx) | Tableau: passenger flow between stops |
| [`../dashboard/vizag-heatmap.twbx`](../dashboard/vizag-heatmap.twbx) | Tableau: geographic density of demand |

## 9. Limitations

- 81 records across 16 routes is a small sample — roughly 5 stops per route, so
  route-level averages rest on few observations.
- Data captures a single time window; it cannot separate peak from off-peak behaviour.
- Delay is measured at stop level only, so mid-route recovery is invisible.
