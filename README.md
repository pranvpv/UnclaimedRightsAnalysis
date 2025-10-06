#  Unclaimed Musical Work Rights — The Weeknd Dataset Analysis

## 📘 Overview
This project explores **unclaimed musical work right shares** associated with **The Weeknd’s** catalog.  
It analyzes a real-world dataset (`unclaimedmusicalworkrightshares.tsv`) to identify **ISRCs** (International Standard Recording Codes) that remain unclaimed due to metadata gaps, publishing mismatches, or registration delays.

The project demonstrates a complete **data workflow** — from large-scale data handling to database querying and insight generation.

---

## 🎯 Objectives
- Extract and analyze ISRCs belonging to **The Weeknd** from a large unclaimed rights dataset.  
- Investigate why certain recordings remain unclaimed.  
- Identify patterns such as duplicates, regional releases, and remix versions.  
- Generate insights into music rights management and metadata synchronization.

---

## 🧰 Tech Stack
| Tool | Purpose |
|------|----------|
| **Python (pandas)** | Data cleaning, filtering, and chunk processing |
| **PostgreSQL** | Database storage and SQL querying |
| **Spotify API** | Metadata verification for ISRCs |
| **Jupyter Notebook** | Exploratory analysis and visualization |
| **CSV / TSV** | Input dataset format |

---

## 🧩 Dataset Details
- **Source file:** `unclaimedmusicalworkrightshares.tsv`  
- **Filtered artist:** *The Weeknd*  
- **Extracted ISRCs:** 375  
- **Example columns:** ISRC, WorkTitle, Artist, RightsOwner, ISWC, ClaimStatus  

---

## 🧮 Workflow Summary
1. **Data Loading:**  
   Used chunked reading (`pandas.read_csv(..., chunksize=...)`) to handle multi-million-row TSV efficiently.  
2. **Filtering:**  
   Filtered records where `ArtistName == "The Weeknd"`.  
3. **ISRC Extraction:**  
   Stored 375 unclaimed ISRCs in a separate CSV file for deeper analysis.  
4. **Verification:**  
   Queried selected ISRCs via the **Spotify API** and **Discogs** to confirm song metadata.  
5. **Database Integration:**  
   Imported cleaned data into **PostgreSQL** for structured queries and further validation.  
6. **Insights Generation:**  
   Identified root causes of unclaimed works such as metadata mismatches, remixes, and regional duplicates.

---

## 🔍 Findings
1. a) From the given `unclaimedmusicalworkrightshares.tsv` file, **375 ISRCs** belonging to *The Weeknd* were obtained.  
   b) The number of songs retrieved through **Spotify API web scraping** was **355**, which is slightly lower compared to the unclaimed rights dataset.  
   c) This difference is assumed to be caused by the **presence of remixes, alternate versions, live performances, and collaborative tracks** in the unclaimed rights data that do not appear as individual releases on Spotify.  
   d) During manual verification, **a few ISRCs could not be found in any public databases** (Spotify, Discogs, or MusicBrainz), possibly indicating internal label versions or unreleased works.  

2. Out of the **355 songs** of *The Weeknd* obtained through Spotify web scraping, **144 songs matched** with entries from the `unclaimedmusicalworkrightshares.tsv` dataset.  

3. The **majority of the matched songs** consist of **live performances, remixes, or collaborative works**, suggesting that these categories are more prone to metadata mismatches and unclaimed rights.

---

## 💡 Insights
- Many unclaimed works are **alternate versions** (remix/live/cover) not properly linked to their main composition.  
- **Metadata mismatches** between ISRC and ISWC codes cause rights to remain unclaimed.  
- Even **major label releases (USUG/USUM prefixes)** can appear unclaimed, revealing data synchronization issues.  
- **Regional releases** (FR3Z, ITQ, CAHQJ prefixes) indicate international catalog fragmentation.  
- Some entries might be **false positives** due to automated tagging or duplicate data.

---

## 🧠 Assumptions
1. The dataset represents **recording-level (ISRC)** data rather than composition rights (ISWC).  
2. “Unclaimed” indicates missing publisher or songwriter linkage.  
3. Multiple ISRCs may refer to the **same song** released in different territories.  
4. Some entries may already be claimed after dataset publication due to time lag in updates.  

---

## 📊 Sample Query (PostgreSQL)
```sql
SELECT isrc, song_title, artist
FROM unclaimed_rights
WHERE artist = 'The Weeknd';

