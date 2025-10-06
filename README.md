# Unclaimed Musical Work Rights — The Weeknd Dataset Analysis

## Overview
This project explores unclaimed musical work right shares associated with The Weeknd’s catalog.  
It analyzes a large real-world dataset (`unclaimedmusicalworkrightshares.tsv`, size ≈ 6 GB) containing royalty ownership and publishing metadata for various recordings.  
The goal is to identify ISRCs (International Standard Recording Codes) that remain unclaimed due to metadata gaps, publishing mismatches, or registration delays.

Because of the file’s large size, it was processed in chunks of 100,000 rows using Python loops to efficiently handle the data and extract meaningful subsets.  
The project demonstrates a complete data workflow — from large-scale data handling to database querying and insight generation.

---

## Objectives
- Extract and analyze ISRCs belonging to The Weeknd from the unclaimed rights dataset.  
- Investigate why certain recordings remain unclaimed.  
- Identify duplicates, remixes, live versions, and collaborative tracks.  
- Generate insights into metadata mismatches and rights linkage issues.

---

## Tech Stack
| Tool | Purpose |
|------|----------|
| Python (pandas) | Data cleaning, filtering, and chunk processing |
| PostgreSQL | Database storage and SQL querying |
| Spotify API | Metadata verification for ISRCs |
| Jupyter Notebook | Exploratory analysis and visualization |
| CSV / TSV | Input dataset format |

---

## Dataset Details
- Source file: `unclaimedmusicalworkrightshares.tsv`  
- File size: ~6 GB (too large to load fully into memory)  
- Processed using: Python `for` loop with `chunksize=100000` for efficient reading  
- Filtered artist: The Weeknd  
- Distinct ISRCs obtained: 374  
- Example columns: ISRC, WorkTitle, Artist, RightsOwner, ISWC, ClaimStatus  

---

## Step-by-Step Workflow

### 1. Initial Filtering
- The task began by locating all ISRCs of songs by The Weeknd in the given `unclaimedmusicalworkrightshares.tsv` file.  
- Upon loading, the file (≈6 GB) was found to be too large to process at once, so it was read in chunks of 100,000 rows using pandas.  
- This loop-based chunk processing allowed smooth and memory-efficient filtering of data.

### 2. Data Cleaning and Deduplication
- After filtering, more than 10,000 ISRCs associated with The Weeknd were found.  
- After removing duplicates, the list was reduced to 374 distinct ISRCs, representing unique recordings or versions.

### 3. Spotify API Integration
- To retrieve detailed metadata (albums, tracks, labels), a new Spotify Developer account was created.  
- Using the client credentials, an access token was generated and used to access the Spotify Web API.  
- The API was used to retrieve relevant information such as song names, album titles, and release dates.

### 4. Cross-Matching
- Using Python, ISRCs obtained from Spotify were compared with those filtered from the unclaimed dataset.  
- Common ISRCs were extracted to find which Spotify-verified recordings also appeared unclaimed in the given TSV file.  
- This revealed patterns in metadata mismatches and missing ownership claims.

---

## Findings
1. a) From the given `unclaimedmusicalworkrightshares.tsv` file, 375 ISRCs belonging to The Weeknd were obtained.  
   b) The number of songs retrieved through Spotify API web scraping was 355, which is slightly lower compared to the unclaimed rights dataset.  
   c) This difference is assumed to be caused by the presence of remixes, alternate versions, live performances, and collaborative tracks in the unclaimed rights data that do not appear as individual releases on Spotify.  
   d) During manual verification, a few ISRCs could not be found in any public databases (Spotify, Discogs, or MusicBrainz), possibly indicating internal label versions or unreleased works.  

2. Out of the 355 songs of The Weeknd obtained through Spotify web scraping, 144 songs matched with entries from the `unclaimedmusicalworkrightshares.tsv` dataset.  

3. The majority of the matched songs consist of live performances, remixes, or collaborative works, suggesting that these categories are more prone to metadata mismatches and unclaimed rights.

---

## Insights
- Many unclaimed works are alternate versions (remix/live/cover) not properly linked to their main composition.  
- Metadata mismatches between ISRC and ISWC codes cause rights to remain unclaimed.  
- Even major label releases (USUG/USUM prefixes) can appear unclaimed, revealing data synchronization issues.  
- Regional releases (FR3Z, ITQ, CAHQJ prefixes) indicate international catalog fragmentation.  
- Some entries might be false positives due to automated tagging or duplicate data.

---

## Assumptions
1. The dataset represents recording-level (ISRC) data rather than composition rights (ISWC).  
2. “Unclaimed” indicates missing publisher or songwriter linkage.  
3. Multiple ISRCs may refer to the same song released in different territories.  
4. Some entries may already be claimed after dataset publication due to time lag in updates.  


