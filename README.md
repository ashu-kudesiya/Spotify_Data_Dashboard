<img src="https://upload.wikimedia.org/wikipedia/commons/1/19/Spotify_logo_without_text.svg" width="222">

# Spotify Data Dashboard 🎵📊

This project provides insights into **Spotify's 2024 dataset** using **Power BI**, focusing on **track popularity, artist performance, and audio feature analysis**. Additionally, a Python script was used to enrich the dataset by retrieving **album cover URLs** via the **Spotify API**.

## 📌 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Dataset](#dataset)
- [Requirements](#requirements)
- [Data Processing Steps](#data-processing-steps)
- [Power BI Dashboard](#power-bi-dashboard)
- [Screenshots](#screenshots)
- [Getting Started](#getting-started)
- [Contact Information](#contact-information)

---

## 🎯 Overview

- **Data Cleaning & Processing**: The dataset was cleaned, missing values were handled, and non-essential columns were removed.
- **Album Cover Retrieval**: Using the **Spotify API**, album cover URLs were fetched and added to the dataset.
- **Power BI Dashboard**: Created **interactive visualizations** for in-depth analysis of Spotify track data.

---

## 🚀 Features

- Extracted **album cover URLs** using a Python script that interacts with the **Spotify API**.
- Created a **Power BI dashboard** for insights into **track popularity, artist trends, and genre analysis**.
- **Advanced data cleaning & transformation** using Python and Pandas.

---

## 📂 Dataset

The dataset contains the following key columns:

| Column Name       | Description |
|------------------|-------------|
| Track | Song title |
| Artist | Name of the artist/band |
| Album | Name of the album |
| Release Date | Date of release |
| Popularity | Track popularity score (0-100) |
| Danceability | Measure of a track’s dance-friendliness |
| Energy | Energy level of the track |
| Tempo | BPM (Beats Per Minute) |
| **Album Cover URL** | URL of the album cover image (retrieved using Spotify API) |

---

## 📌 Requirements

- **Python 3.x** (for data processing & album cover retrieval)
- **Power BI Desktop** (for viewing the dashboard)
- **Spotipy Library** (for interacting with the Spotify API)
- **Pandas Library** (for data manipulation)
- **Spotify Developer Account** (for API access)

---

## 🔄 Data Processing Steps

### 1️⃣ Fetching Album Cover URLs

A Python script (`python_script.py`) was used to retrieve **album cover URLs** using the **Spotify Web API**.

- **Authentication**: Utilized `SpotifyClientCredentials` for API authentication.
- **Track Querying**: Matched **Track** and **Artist** to fetch the album cover.
- **Rate Limiting Handling**: Implemented **retry logic** to avoid exceeding API limits.
- **Multi-threading**: Used `ThreadPoolExecutor` for parallel API requests.

✅ The final dataset with album cover URLs was saved as `updated_spotify_data.csv`.

---

## 📊 Power BI Dashboard

The Power BI dashboard provides:

- **Track Popularity Analysis**: Distribution of tracks based on popularity scores.
- **Artist Performance Trends**: Top-performing artists based on track count & popularity.
- **Genre & Feature Analysis**: Insights into **danceability, energy, and tempo** of songs.
- **Album Cover Integration**: Displaying album covers for enhanced visualization.

---

## 📸 Screenshots

### 🎵 Dashboard Overview
![Spotify Dashboard Screenshot](https://your-image-link.com/dashboard.png)

---

### 📊 Popularity Analysis
![Popularity Analysis Screenshot](https://your-image-link.com/popularity.png)

---

### 🔥 Artist Performance
![Artist Performance Screenshot](https://your-image-link.com/artist.png)

---

## 🛠 Getting Started

### 1️⃣ Run the Python Script
1. Replace `SPOTIPY_CLIENT_ID` and `SPOTIPY_CLIENT_SECRET` with your **Spotify API credentials** in `python_script.py`.
2. Run the script:
   ```bash
   python python_script.py
