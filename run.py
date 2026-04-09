import streamlit as st
import pandas as pd
import numpy as np

# Import the SCM modules
from data.schema import UDM
from scm.eoq import *
from scm.safetystock import *
from scm.newsboy import *
from scm.contracts import *

# Dummy data for demonstration
dummy_data = {
    'SKU': ['A001', 'A002', 'A003'],
    'Grade': ['High', 'Medium', 'Low'],
    'Origin': ['USA', 'China', 'India'],
    'LeadTime': [5, 7, 3],
    'BOM': [{'Part1': 2, 'Part2': 1}, {'Part1': 1, 'Part2': 2}, {'Part1': 3, 'Part2': 1}]
}

# Create a sample UDM instance
sample_udm = UDM(**dummy_data)

# Initialize the app
st.title('SCM Dashboard')

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Overview", "Per-Material Metrics", "Newsvendor", "Contract Comparison", "Scenario Analysis"])

if page == "Overview":
    st.header("Overview")
    # Total demand, material cost, transportation cost
    total_demand = 1000  # dummy value
    material_cost = 50000  # dummy value
    transportation_cost = 10000  # dummy value
    
    st.metric("Total Demand", total_demand)
    st.metric("Material Cost", f"${material_cost:,}")
    st.metric("Transportation Cost", f"${transportation_cost:,}")

elif page == "Per-Material Metrics":
    st.header("Per-Material Inventory Metrics")
    # SS, ROP, EOQ
    material_data = pd.DataFrame({
        'SKU': ['A001', 'A002', 'A003'],
        'Safety Stock': [100, 150, 80],
        'Reorder Point': [200, 250, 150],
        'EOQ': [300, 400, 200]
    })
    st.dataframe(material_data)
    st.write("This panel displays safety stock, reorder point, and EOQ metrics for each material.")
    
elif page == "Newsvendor":
    st.header("Newsvendor Analysis")
    # Finished goods seasonal SKUs
    seasonal_sku_data = pd.DataFrame({
        'SKU': ['S001', 'S002', 'S003'],
        'Critical Ratio': [0.7, 0.6, 0.8],
        'Optimal Q': [1000, 1200, 900],
        'Co/Cu': [0.5, 0.4, 0.6]
    })
    st.dataframe(seasonal_sku_data)
    st.write("This panel analyzes seasonal SKUs using newsvendor model.")
    
elif page == "Contract Comparison":
    st.header("Contract Comparison")
    # Wholesale, buyback, revenue sharing
    contract_data = pd.DataFrame({
        'Contract Type': ['Wholesale', 'Buyback', 'Revenue Sharing'],
        'Profit': [10000, 12000, 11000],
        'Risk': [7, 5, 6]
    })
    st.dataframe(contract_data)
    st.write("This panel compares different contract types.")
    
elif page == "Scenario Analysis":
    st.header("Scenario Analysis")
    # Lead time shock, cost %, demand spike
    st.write("Scenario Analysis: Adjust parameters to see impacts on supply chain metrics.")
    
    # Inputs
    lead_time_shock = st.slider('Lead Time Shock (%)', 0, 50, 10)
    cost_percentage = st.slider('Cost Increase (%)', 0, 30, 5)
    demand_spike = st.slider('Demand Spike (%)', 0, 100, 20)
    
    # Display scenario impact
    st.write(f"Scenario with lead time shock: {lead_time_shock}%, cost increase: {cost_percentage}%, demand spike: {demand_spike}%")
    
    # Placeholder for actual impact calculation
    impact_data = pd.DataFrame({
        'Metric': ['Inventory Cost', 'Shortage Cost', 'Total Cost'],
        'Impact': ['+10%', '+5%', '+15%']
    })
    st.dataframe(impact_data)


