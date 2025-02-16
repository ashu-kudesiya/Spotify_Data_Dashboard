

# 🎵 Spotify Data Dashboard 📊  

This project provides insights into **Spotify's 2024 dataset** using **Power BI**, focusing on track performance, artist trends, streaming statistics, and playlist reach. The dataset was enriched by retrieving **album cover URLs** via the **Spotify API** using a Python script.  

## 📌 Table of Contents  
- [🔍 Overview](#overview)  
- [⚙️ Requirements](#requirements)  
- [📊 Steps for Analysis](#steps-for-analysis)  
- [📈 Visualizations](#visualizations)  
- [📸 Screenshots](#screenshots)  
- [🚀 Getting Started](#getting-started)  
- [📩 Contact Information](#contact-information)  

---

## 🔍 Overview  

- **🛠 Data Cleaning & Processing**: The dataset was cleaned, missing values were handled, and non-essential columns were removed.  
- **🎨 Album Cover Retrieval**: A Python script used the **Spotify API** to fetch album cover URLs.  
- **📊 Power BI Dashboard**: Created **interactive visualizations** for analyzing track performance, artist popularity, and playlist impact.  

---

## ⚙️ Requirements  

- 🐍 **Python 3.x** (for data processing & album cover retrieval)  
- 🖥 **Power BI Desktop** (for viewing the dashboard)  
- 🎧 **Spotipy Library** (for interacting with the Spotify API)  
- 📑 **Pandas Library** (for data manipulation)  
- 🔑 **Spotify Developer Account** (for API access)  

### 📂 Files  
- **📌 `Dashboard.pbix`** → Power BI file containing the dashboard  
- **📁 `updated_spotify_data.csv`** → Processed dataset with album cover URLs  
- **📜 `python_script.py`** → Script for retrieving album cover URLs from Spotify API  

---

## 📊 Steps for Analysis  

### 🎯 Part 1: Data Preparation & Enrichment  

1️⃣ **Data Import and Cleaning**  
   - Loaded the original Spotify dataset.  
   - Handled missing values and standardized columns.  

2️⃣ **Album Cover Retrieval**  
   - Used a **Python script** to fetch album cover URLs from the **Spotify API**.  
   - Implemented **rate-limiting handling** to avoid API restrictions.  
   - Used **multi-threading** to speed up requests.  

3️⃣ **Final Output**  
   - Created `updated_spotify_data.csv` containing the album cover URLs.  

---

### 🎵 Part 2: Power BI Dashboard Analysis  

1️⃣ **Data Import and Transformation**  
   - Loaded `updated_spotify_data.csv` into Power BI.  
   - Transformed the dataset for better visualization.  

2️⃣ **Data Visualization**  
   - 🎤 **Track Performance**: Analysis based on Spotify streams, YouTube views, and TikTok trends.  
   - 🌟 **Artist Popularity**: Identifying top artists based on streaming numbers.  
   - 📢 **Playlist & Streaming Reach**: Insights into track placements across different platforms.  
   - 🖼 **Album Cover Display**: Enhanced visuals with fetched album covers.  

3️⃣ **Insights**  
   - 📌 Identified the most streamed and popular tracks.  
   - 🔍 Determined the platforms contributing the most to track success.  
   - 📊 Analyzed trends in playlist reach and track engagement.  

4️⃣ **Final Output**  
   - 🎯 Interactive **Power BI dashboard** with actionable insights.  

---

## 📈 Visualizations  

This dashboard includes the following visualizations:  

- 🏆 **Top Artists & Track Performance**  
- 🎚 **Streaming Statistics (Spotify, YouTube, TikTok, Pandora)**  
- 🎼 **Playlist Reach & Engagement**  
- 🎨 **Album Cover Integration for Better Insights**  

---

## 📸 Screenshots  

![🎵 Dashboard Screenshot](https://your-image-link.com/dashboard.png)  
---  
![📊 Track Performance Screenshot](https://your-image-link.com/track_performance.png)  
---  
![🔥 Artist Popularity Screenshot](https://your-image-link.com/artist_popularity.png)  
---  

---

## 🚀 Getting Started  

### 🛠 Running the Python Script  
1️⃣ Replace `SPOTIPY_CLIENT_ID` and `SPOTIPY_CLIENT_SECRET` with your **Spotify API credentials** in `python_script.py`.  
2️⃣ Run the script:  
   ```bash
   python python_script.py
