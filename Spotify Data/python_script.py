import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

# 🚨 REPLACE: Your Spotify API credentials
# 🔴 Replace with your Client ID
SPOTIPY_CLIENT_ID = "-----------------"
# 🔴 Replace with your Client Secret
SPOTIPY_CLIENT_SECRET = "------------------"

# Authenticate with Spotify API
client_credentials_manager = SpotifyClientCredentials(
    client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# 🚨 REPLACE: Your CSV file path
# 🔴 Replace with actual file path
file_path = r"D:\Study\Project\Spotify\spotify_data.csv"
df = pd.read_csv(file_path, encoding="ISO-8859-1")

# ✅ Ensure required columns exist
if "Track" not in df.columns or "Artist" not in df.columns:
    raise ValueError("Dataset must have 'Track' and 'Artist' columns.")

# Function to get album cover URL with rate-limit handling


def get_album_cover(track, artist):
    query = f"track:{track} artist:{artist}"

    while True:
        try:
            result = sp.search(q=query, type="track", limit=1)
            if result["tracks"]["items"]:
                return result["tracks"]["items"][0]["album"]["images"][0]["url"]
            return "Not Found"
        except spotipy.exceptions.SpotifyException as e:
            if e.http_status == 429:  # Rate limit error
                retry_after = int(e.headers.get("Retry-After", 5))
                print(
                    f"🔴 Rate limit reached. Retrying after {retry_after} seconds...")
                # Extra buffer time to avoid consecutive limits
                time.sleep(retry_after + 2)
            else:
                print(f"❌ Error fetching {track} by {artist}: {e}")
                return "Error"


# 🚀 Use ThreadPoolExecutor with fewer workers (avoid too many requests)
album_covers = []
# 🔥 Reduce to 3 workers to prevent rate limiting
with ThreadPoolExecutor(max_workers=3) as executor:
    future_to_row = {executor.submit(get_album_cover, row["Track"], row["Artist"]): index
                     for index, row in df.iterrows()}

    for future in as_completed(future_to_row):
        index = future_to_row[future]
        try:
            album_covers.append(future.result())
        except Exception as e:
            print(f"❌ Error at index {index}: {e}")
            album_covers.append("Error")

# Add album cover URLs to DataFrame
df["Album Cover URL"] = album_covers

# 🚨 REPLACE: Your desired output file name
output_file = "updated_spotify_data.csv"  # 🔴 Replace with the output file name
df.to_csv(output_file, index=False)

print(f"✅ Updated dataset saved as {output_file}")
