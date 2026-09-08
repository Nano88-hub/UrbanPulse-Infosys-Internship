# Milestone 4 — Mobility Equity & Executive Intelligence Platform

**Project:** UrbanPulse — Smart City Mobility Intelligence Platform
**City studied:** Visakhapatnam (Vizag) · **Weeks 7–8**
**Deliverables:** three integrated Power BI dashboards

---

## 1. Objective

City transit agencies can see overall ridership, but not **who is being left behind**.
Access to reliable transport is uneven across zones, and planners lack a single,
forecast-aware view to prioritise where to act next.

Milestone 4 brought equity scoring, demand forecasting and executive decision support
into one platform.

## 2. Project flow

| Stage | Deliverable |
|---|---|
| 1 | **Equity Dashboard** — implement the Mobility Access Index, build zone-level equity views |
| 2 | **Executive Dashboard** — roll KPIs up into a leadership-facing intelligence view |
| 3 | **Forecasting & Anomaly Detection** — demand forecasting with automated alerts |
| 4 | **Optimisation & Deployment** — performance tuning and deployment readiness |

## 3. Dataset

`../data/vizag_mobility_equity_updated.xlsx` — 96 trip-level records, May 2024.

| Dimension | Values |
|---|---|
| Zones | Seethammadhara, Dwaraka Nagar, MVP Colony, Kothapeta, Pendurthi, Madurawada, Rushikonda, Gajuwaka |
| Transport modes | Cab, Bike, Bus, Auto |
| Demographic groups | Student, Employee, Senior Citizen, Low Income |
| Weather | Clear, Cloudy, Heavy Rain, Light Rain |
| Core metrics | Mobility Access Score, Mobility Equity Score, Service Availability %, Avg Travel Time, Transit Routes, Trip Count, Population |

A second sheet, **Notes & Assumptions**, documents how the file was extended from the
original 80-row version (16 rows added to fill missing May dates and top up
under-represented zones) — good practice worth preserving.

---

## 4. Dashboard 01 — Mobility Equity

### Zone-level results

| Zone | Access score | Equity score | Service coverage | Avg travel time | Transit routes | Population |
|---|---:|---:|---:|---:|---:|---:|
| Seethammadhara | 0.85 | 0.88 | 81.9% | 27.6 min | 24 | 210,000 |
| Dwaraka Nagar | 0.83 | 0.90 | 76.8% | 32.3 min | 22 | 185,000 |
| MVP Colony | 0.80 | 0.95 | 73.8% | 31.9 min | 18 | 95,000 |
| Pendurthi | 0.36 | 0.61 | 30.4% | 46.5 min | 8 | 140,000 |
| Kothapeta | 0.34 | 0.59 | 31.1% | 43.8 min | 9 | 150,000 |
| Madurawada | 0.32 | 0.59 | 28.6% | 48.8 min | 7 | 175,000 |
| Rushikonda | 0.30 | 0.56 | 29.7% | 51.2 min | 6 | 60,000 |
| **Gajuwaka** | **0.30** | 0.55 | **27.7%** | **54.0 min** | 8 | 320,000 |

**Citywide mean access score: 0.513**

### Q&A

**Which areas have the highest mobility access?**
Seethammadhara (0.85), followed by Dwaraka Nagar (0.83) and MVP Colony (0.80).

**Which areas have the lowest?**
Gajuwaka and Rushikonda (both 0.30), followed by Madurawada (0.32).

**Which areas are underserved?**
Gajuwaka, Rushikonda and Madurawada — all three fall far below the 0.513 citywide mean.

**What drives low accessibility?**
Low service coverage (27.7% in Gajuwaka against 81.9% in Seethammadhara), high travel
time, and weak auto/feeder connectivity in outer zones.

**What can the city do?**
Add transit routes and increase vehicle frequency, starting with Gajuwaka, then
Rushikonda and Madurawada — prioritised by riders gained per added route.

### The central insight

Access tracks route provision almost linearly. Seethammadhara has **24 transit routes**
and an access score of 0.85; Rushikonda has **6** and scores 0.30. Route count is the
strongest lever the city controls.

**Gajuwaka is the clearest priority in the city.** It combines the worst access score
(0.30), the worst service coverage (27.7%), the longest travel time (54.0 min) — and the
**largest population of any zone (320,000)**. It is simultaneously the worst-served and
the most populous area, so a fix there reaches more people than anywhere else.

By contrast, Rushikonda scores equally badly but holds only 60,000 residents, so the
same investment reaches a fifth as many people. **Equity ranking and population ranking
must be read together to allocate budget sensibly.**

---

## 5. Dashboard 02 — Forecasting & Anomaly Detection

### Anomalies detected

| Date | Zone | Observation | Likely cause |
|---|---|---|---|
| 30 May 2024 | Citywide | Demand spike to ~1,900 trips against a 600–700 daily average — the highest point on the chart | Clear weather combined with elevated month-end activity |
| 10 May 2024 | Pendurthi | Access score dropped to 0.18, travel time rose to 62 min | Heavy rain, against a baseline of only 8 transit routes |

### Insight

The two anomalies have opposite causes but a shared lesson: **zones with few routes
have no buffer.** Pendurthi's 8 routes left nothing in reserve when rain disrupted
service, so a weather event became a service failure.

### Recommendations

- Keep extra vehicles on standby for high-activity, clear-weather days such as month-end.
- Prioritise weather-resilient transit — covered stops, backup vehicles — in low-route
  zones like Pendurthi first.

---

## 6. Dashboard 03 — Executive Mobility Intelligence

![Executive Mobility Intelligence Dashboard](../dashboard/Milestone-4-Executive-Dashboard.png)

### Headline KPIs

| Metric | Value |
|---|---|
| Mobility Access Index | 51.32 |
| Total trips | 13K |
| Average travel time | 42.02 min |
| **Underserved population** | **845K** |
| Average service coverage | 47.50% |

### Alerts

| Alert | Zones affected |
|---|---|
| High travel time | Gajuwaka 54.0 min · Madurawada 48.8 min · Pendurthi 46.5 min |
| Low mobility access | Gajuwaka 0.30 · Rushikonda 0.30 · Madurawada 0.32 |
| Low service coverage | Gajuwaka 27.7% · Madurawada 28.6% · Rushikonda 29.7% |

**845,000 residents underserved citywide.**

### Executive recommendations

| Priority | Action | Rationale |
|---|---|---|
| **High** | Deploy additional buses and increase route frequency in **Gajuwaka** | Worst access, worst coverage, longest travel time, largest population |
| **High** | Prioritise traffic management and route optimisation in **Rushikonda & Madurawada** | Congestion and long travel times |
| Medium | Improve auto/feeder connectivity in underserved zones | Weak last-mile access |

---

## 7. Outcome

- Three dashboards delivered, covering equity scoring, forecasting and executive rollup
- Every zone scored against a citywide access index of 0.513
- 845,000 underserved residents identified, with a prioritised action plan for
  Gajuwaka, Rushikonda, Madurawada and Pendurthi

**Milestone status: complete** — all three dashboards deployed and validated.

---

## 8. Limitations

- 96 records across 8 zones, 4 modes and 4 demographic groups means individual
  zone-mode-group cells rest on very few observations.
- Data covers a single month (May 2024) and cannot show seasonal variation.
- The Mobility Access Index formula is implemented inside the `.pbix` file; it is not
  documented as a standalone specification, so it cannot be independently recomputed.
- 16 of the 96 rows were synthesised to fill gaps (see the Notes & Assumptions sheet)
  and are not direct observations.
