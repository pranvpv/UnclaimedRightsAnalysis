import requests
import base64

client_id = "7f03f7eeb9fd49d382dade584bbb3a98"
client_secret = "96987357ea524cabaffca7ab7885694b"

# Encode credentials
auth_str = f"{client_id}:{client_secret}"
b64_auth_str = base64.b64encode(auth_str.encode()).decode()

# Request access token
token_url = "https://accounts.spotify.com/api/token"
response = requests.post(token_url, 
    data={"grant_type": "client_credentials"},
    headers={"Authorization": f"Basic {b64_auth_str}"}
)

access_token = response.json()["access_token"]
print("Access Token:", access_token)


import pandas as pd
headers = {"Authorization": f"Bearer {access_token}"}
artist_name = "The Weeknd"
url = "https://api.spotify.com/v1/search"
params = {"q": "The Weeknd", "type": "artist", "limit": 1}
res = requests.get(url, headers=headers, params=params)
artist = res.json()["artists"]["items"][0]
artist_id = artist["id"]

url = f"https://api.spotify.com/v1/artists/{artist_id}/albums"

albums = []
params = {
    "include_groups": "album,single,compilation",  # choose what to include
    "limit": 50,   # max allowed per request
    "offset": 0
}

# Handle pagination (Spotify only gives 50 at a time)
while True:
    res = requests.get(url, headers=headers, params=params).json()
    items = res.get("items", [])
    albums.extend(items)

    # Check if there are more pages
    if res.get("next"):
        params["offset"] += params["limit"]
    else:
        break

all_tracks = []

track_ids_seen = set()  # avoid duplicates

for album in albums:
    album_id = album["id"]
    album_name = album["name"]
    release_date = album["release_date"]

    # Get album tracks
    tracks_url = f"https://api.spotify.com/v1/albums/{album_id}/tracks"
    tracks_res = requests.get(tracks_url, headers=headers).json()
    tracks = tracks_res.get("items", [])

    for track in tracks:
        track_id = track["id"]


        # Skip duplicates (some songs appear in multiple albums)
        if track_id in track_ids_seen:
            continue
        track_ids_seen.add(track_id)

        # Get track details (for ISRC)
        track_url = f"https://api.spotify.com/v1/tracks/{track_id}"
        track_data = requests.get(track_url, headers=headers).json()

        isrc = track_data.get("external_ids", {}).get("isrc", "N/A")

        all_tracks.append({
            "Track Name": track["name"],
            "Album": album_name,
            "Release Date": release_date,
            "Artists": ", ".join([a["name"] for a in track["artists"]]),
            "ISRC": isrc,
            "Track ID": track_id
        })
        
df = pd.DataFrame(all_tracks)
csv_filename = r"C:\Users\prana\Downloads\unclaimed.csv"
df.to_csv(csv_filename, index=False, encoding="utf-8")
print(all_tracks)