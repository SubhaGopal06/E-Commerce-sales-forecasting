import streamlit as st

# Streamlit App Configuration
st.set_page_config(page_title="E-commerce Sales Forecasting", layout="wide")

# Main Page
if "page" not in st.session_state:
    st.session_state.page = "main"

if st.session_state.page == "main":
    st.title("E-commerce Sales Forecasting")
    selected_store = st.selectbox("Generate sales report for:", ["Select", "Walmart"])
    
    if selected_store == "Walmart":
        st.session_state.page = "dashboard"
        st.experimental_rerun()

# Dashboard Page
elif st.session_state.page == "dashboard":
    st.subheader("Sales Analysis Dashboard")
    st.image("dashboard.jpg", use_column_width=True)
    
    if st.button("Go Back"):
        st.session_state.page = "main"
        st.experimental_rerun()
