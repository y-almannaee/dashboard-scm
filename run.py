# Project Plan: Supply Chain Dashboard
# 1. Overview page
# Total demand
# Total material requirement
# Total material cost
# Total transportation cost

# 2. Demand analysisff
# Demand by product over time
# Peak periods (we can graph the demand, draw trendlines, etc.)

#    3.Cost breakdown
# Material cost per product
# Transportation cost per product
# Landed cost per product
# Cost share by material

# 5. Inventory / service metrics
# Safety stock
# Reorder point
# Estimated order quantity
# Stockout risk
# Service level / fill rate
#  - - - All these can be calculated with formulas we learnt in the course, assumptions can be made and we will clearly list them out

# 6. Scenario analysis
# Material cost increase   (we can describe effects of geopolitical events)
# Transportation cost increase  (we can make an assumption that costs are linked to oil prices, make sensitivity analysis based on cost of oil)
# Demand spike/drop
# Supplier or lead-time disruption
# Impact on total cost and material requirements

# What should the LLM do:
# 1. summarize the dashboard. Use the data as an MCP to LM Studio?
# 2. explain specific scenarios (transportation cost increases/decreases, material price increase/decrease)
# 3. suggest actions from management (stock up on certain materials, increase prices to compensate for rising material cost, etc)

# Architecture (prototypical only)
# [Raw Data CSVs]
#     ↓
# [Data Layer] — unified schema: SKU, Grade, Origin, Lead Time, Demand (mean/var), Unit Cost, BOM ratios
#     ↓
# [BOM Engine] — finished goods demand × BOM coefficients → material-level demand (MRP logic)
#     ↓
# [Model Layer — Python modules]
#     ├── eoq.py          → Q*, order frequency, annual cost
#     ├── safety_stock.py → CSL, SS, ROP, fill rate
#     ├── newsvendor.py   → critical ratio, optimal Q, Co/Cu
#     └── contracts.py    → wholesale / buyback / revenue sharing comparison
#     ↓
# [Streamlit Dashboard]
#     ├── Overview (total demand, material cost, transportation cost)
#     ├── Per-material inventory metrics (SS, ROP, EOQ)
#     ├── Newsvendor panel (finished goods seasonal SKUs)
#     ├── Contract comparison panel
#     └── Scenario Analysis (lead time shock, cost %, demand spike)
#     ↓
# [LLM Layer] — receives computed outputs, generates executive plain-text summary

import streamlit as st
import pandas as pd
import numpy as np


