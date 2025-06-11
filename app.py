import streamlit as st
from datetime import date

# Page config
st.set_page_config(page_title="Defense Dashboard", layout="wide")

# Sidebar UI
st.sidebar.header("Filters")

# ✅ Region Filter (Alphabetized & Updated List)
regions = sorted(["AFRICOM", "CENTCOM", "EUCOM", "NORTHCOM", "SOUTHCOM", "SPACECOM", "CYBERCOM"])
selected_regions = st.sidebar.multiselect("Select Region(s)", regions)

# ✅ Topic Filter (You can update this list later)
topics = ["Surface Warfare", "AEGIS", "Cyber", "Budget", "Taiwan", "China", "Russia"]
selected_topics = st.sidebar.multiselect("Select Topic(s)", topics)

# ✅ Date Range Picker (From - To)
date_range = st.sidebar.date_input(
    "Select Date Range",
    value=(date(2024, 1, 1), date.today()),
    help="Choose a start and end date",
)

if len(date_range) != 2:
    st.sidebar.warning("Please select both a start and end date.")

# ✅ Source URL Submission Panel
st.sidebar.markdown("---")
st.sidebar.subheader("Add New Source")

new_source_url = st.sidebar.text_input("Paste Source URL")
new_source_region = st.sidebar.selectbox("Assign Region", regions)

if st.sidebar.button("Submit Source"):
    if new_source_url.strip() == "":
        st.sidebar.warning("Please enter a valid URL.")
    else:
        st.sidebar.success(f"Source '{new_source_url}' submitted for region '{new_source_region}'")
        # Future: Append to a database or trigger a webhook here

# Main area
st.title("🌐 U.S. Defense & Geopolitics News Feed")

st.write("🚧 This section will eventually list filtered news articles based on selected inputs.")
st.write(f"**Regions:** {', '.join(selected_regions) if selected_regions else 'All'}")
st.write(f"**Topics:** {', '.join(selected_topics) if selected_topics else 'All'}")
st.write(f"**Date Range:** {date_range[0]} to {date_range[1]}" if len(date_range) == 2 else "")
