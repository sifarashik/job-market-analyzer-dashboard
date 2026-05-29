import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ---------------- PAGE SETTINGS ----------------
st.set_page_config(
    page_title="Web Scraping Job Dashboard",
    layout="centered"
)

# ---------------- LOAD DATA ----------------
df = pd.read_csv("jobs.csv")

# ---------------- TITLE ----------------
st.title("🌐 Web Scraping Job Dashboard")

st.markdown("Analyze real scraped job market data")

# ---------------- DATASET ----------------
st.subheader("📁 Scraped Job Data")

st.dataframe(df)

# ---------------- METRICS ----------------
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Jobs", len(df))

with col2:
    st.metric("Companies", df["Company"].nunique())

with col3:
    st.metric("Locations", df["Location"].nunique())

st.divider()

# ---------------- TOP LOCATIONS ----------------
st.subheader("📍 Top Hiring Locations")

location_counts = df["Location"].value_counts().head(5)

fig1, ax1 = plt.subplots(figsize=(6,4))

ax1.bar(
    location_counts.index,
    location_counts.values
)

ax1.set_title("Top 5 Hiring Locations")
ax1.set_xlabel("Location")
ax1.set_ylabel("Jobs")

plt.xticks(rotation=15)

st.pyplot(fig1)

st.divider()

# ---------------- TOP COMPANIES ----------------
st.subheader("🏢 Top Hiring Companies")

company_counts = df["Company"].value_counts().head(5)

fig2, ax2 = plt.subplots(figsize=(6,4))

ax2.bar(
    company_counts.index,
    company_counts.values
)

ax2.set_title("Top 5 Companies")
ax2.set_xlabel("Company")
ax2.set_ylabel("Jobs")

plt.xticks(rotation=15)

st.pyplot(fig2)

st.divider()

# ---------------- PIE CHART ----------------
st.subheader("🥧 Job Distribution")

fig3, ax3 = plt.subplots(figsize=(5,5))

ax3.pie(
    location_counts.values,
    labels=location_counts.index,
    autopct="%1.1f%%"
)

ax3.set_title("Location Distribution")

st.pyplot(fig3)

st.divider()

# ---------------- SEARCH ----------------
st.subheader("🔍 Search Jobs")

search = st.text_input("Search by company or location")

filtered_df = df[
    df["Company"].str.contains(search, case=False, na=False) |
    df["Location"].str.contains(search, case=False, na=False)
]

st.dataframe(filtered_df)

# ---------------- FOOTER ----------------
st.success("Dashboard Loaded Successfully 🚀")