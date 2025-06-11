import streamlit as st

st.set_page_config(page_title="Defense Dashboard", layout="wide")

st.title("🌐 U.S. Defense & Geopolitics News Feed")
st.sidebar.header("Filters")

st.sidebar.multiselect("Region", ["INDOPACOM", "CENTCOM", "EUCOM"])
st.sidebar.multiselect("Topic", ["Surface Warfare", "AEGIS", "Cyber", "Budget", "Taiwan", "China", "Russia"])
st.sidebar.date_input("Date Range")

st.write("🚧 [Sample Feed] This section will eventually list curated news articles...")
