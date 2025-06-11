import streamlit as st
from datetime import date
import feedparser

# --- CONFIG ---
st.set_page_config(page_title="Defense Dashboard", layout="wide")

# Define Region & Topic Filters
regions = sorted(["AFRICOM", "CENTCOM", "CYBERCOM", "EUCOM", "INDOPACOM", "NORTHCOM", "SOUTHCOM", "SPACECOM"])
topics = ["Surface Warfare", "AEGIS", "Cyber", "Budget", "Taiwan", "China", "Russia"]

# Define RSS Feeds with Region Mapping (PACOM changed to INDOPACOM)
rss_feeds = {
    "https://www.defense.gov/News/News-Stories/RSS/": "Unassigned",
    "https://www.defense.gov/News/Feature-Stories/RSS/": "Unassigned",
    "https://feeds.feedburner.com/BreakingDefense": "Unassigned",
    "https://feeds.feedburner.com/defenseone/all": "Unassigned",
    "https://www.navy.mil/RSS/TopStories.xml": "Unassigned",
    "https://www.navy.mil/RSS/Press-Releases.xml": "Unassigned",
    "https://www.defensenews.com/m/rss/naval/": "Unassigned",
    "https://www.realcleardefense.com/rss": "Unassigned",
    "https://military.com/defensetech/feed": "Unassigned",
    "https://thediplomat.com/category/asia-defense/feed/": "INDOPACOM",
    "https://globalsecurityreview.com/feed/": "Unassigned",
    "https://www.state.gov/rss-feeds/foreign-policy/": "Unassigned",
    "https://www.darpa.mil/news/rss": "Unassigned",
    "https://www.defencetalk.com/category/navy-news/feed/": "Unassigned",
    "https://www.doncio.navy.mil/RSSFeeds.aspx": "Unassigned",
    "https://news.usni.org/top-stories-feed": "INDOPACOM",
    "https://blog.usni.org/?feed=rss2": "Unassigned"
}

# --- SIDEBAR ---
st.sidebar.title("Filters")

# Page switcher
page = st.sidebar.radio("Go to", ["Main Feed", "Active Sources"])

if page == "Main Feed":
    selected_regions = st.sidebar.multiselect("Select Region(s)", regions)
    selected_topics = st.sidebar.multiselect("Select Topic(s)", topics)
    date_range = st.sidebar.date_input("Select Date Range", value=(date(2024, 1, 1), date.today()))

    st.sidebar.markdown("---")
    st.sidebar.subheader("Add New Source (UI Only)")
    new_source_url = st.sidebar.text_input("Paste Source URL")
    new_source_region = st.sidebar.selectbox("Assign Region", regions)

    if st.sidebar.button("Submit Source"):
        if new_source_url.strip() == "":
            st.sidebar.warning("Please enter a valid URL.")
        else:
            st.sidebar.success(f"Source '{new_source_url}' submitted for region '{new_source_region}'")
            # Future: Append source to storage or list

    # --- DATA INGESTION & TAGGING ---
    def tag_article(entry):
        entry_tags = {"regions": set(), "topics": set()}
        content = f"{entry.get('title', '')} {entry.get('summary', '')}".lower()
        for region in regions:
            if region.lower() in content:
                entry_tags["regions"].add(region)
        for topic in topics:
            if topic.lower() in content:
                entry_tags["topics"].add(topic)
        return entry_tags

    # Fetch & tag artic
