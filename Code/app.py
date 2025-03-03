import streamlit as st

# Streamlit App Configuration
st.set_page_config(page_title="E-commerce Sales Forecasting", layout="wide")
st.markdown("""
    <style>
        body {
            background-color: white;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("E-commerce Sales Forecasting")

# Dropdown for report selection
selected_store = st.selectbox("Generate sales report for:", ["Walmart"])

# Display Dashboard Image
st.subheader("Sales Analysis Dashboard")
st.image("dashboard.png", use_column_width=True)

# Download Report Placeholder
if st.button("Download Report"):
    st.warning("Report download functionality is not available yet.")
