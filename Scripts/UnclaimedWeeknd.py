import pandas as pd

filename= r"C:\Users\prana\Downloads\unclaimedmusicalworkrightshares.tsv"
search_value= "THE WEEKND"
code=[]
chunksize = 100000 
for chunk in pd.read_csv(filename, sep='\t',usecols=["DisplayArtistName", "ISRC"], chunksize=chunksize):

    matches=chunk[chunk["DisplayArtistName"]=="THE WEEKND"]
    code.extend(matches["ISRC"].dropna().tolist())


df = pd.DataFrame(code)
csv_filename = r"C:\Users\prana\Downloads\star1.csv"
df.to_csv(csv_filename, index=False, encoding="utf-8")
print(code)
    