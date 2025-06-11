import streamlit as st
from datetime import date
import feedparser

# Page config
st.set_page_config(page_title="Defense Dashboard", layout="wide")

# Sidebar UI
st.sidebar.header("Filters")

# Region Filter
regions = sorted([
    "AFRICOM", "CENTCOM", "CYBERCOM", "EUCOM",
    "NORTHCOM", "PACOM", "SOUTHCOM", "SPACECOM"
])
selected_regions = st.sidebar.multiselect("Select Region(s)", regions)

# Topic Filter
topics = ["Surface Warfare", "AEGIS", "Cyber", "Budget", "Taiwan", "China", "Russia"]
selected_topics = st.sidebar.multiselect("Select Topic(s)", topics)

# Date Range Picker
date_range = st.sidebar.date_input(
    "Select Date Range",
    value=(date(2024, 1, 1), date.today())
)

# Source URL Submission Tool (UI only for now)
st.sidebar.markdown("---")
st.sidebar.subheader("Add New Source")
new_source_url = st.sidebar.text_input("Paste Source URL")
new_source_region = st.sidebar.selectbox("Assign Region", regions)

if st.sidebar.button("Submit Source"):
    if new_source_url.strip() == "":
        st.sidebar.warning("Please enter a valid URL.")
    else:
        st.sidebar.success(f"Source '{new_source_url}' submitted for region '{new_source_region}'")
        # Future enhancement: store this in database or feed list

# 🔄 RSS Feed List (Expanded with USNI)
rss_feeds = [
    "https://www.defense.gov/News/News-Stories/RSS/",
    "https://www.defense.gov/News/Feature-Stories/RSS/",
    "https://feeds.feedburner.com/BreakingDefense",
    "https://feeds.feedburner.com/defenseone/all",
    "https://www.navy.mil/RSS/TopStories.xml",
    "https://www.navy.mil/RSS/Press-Releases.xml",
    "https://www.defensenews.com/m/rss/naval/",
    "https://www.realcleardefense.com/rss",
    "https:
