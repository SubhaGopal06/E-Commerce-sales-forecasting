import streamlit as st
import base64

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

# Display Power BI Dashboard
st.subheader("Sales Analysis Dashboard")

# Embed Power BI Report (Replace with actual embed URL)
powerbi_embed_url = "https://app.powerbi.com/view?r=YOUR_EMBED_URL"
st.components.v1.iframe(powerbi_embed_url, height=800, width=1200)

# Download Power BI Report
if st.button("Download Report"):
    file_link = "https://app.powerbi.com/export?r=YOUR_EXPORT_URL"
    b64 = base64.b64encode(file_link.encode()).decode()
    href = f'<a href="data:file/txt;base64,{b64}" download="sales_report.txt">Download Report</a>'
    st.markdown(href, unsafe_allow_html=True)
