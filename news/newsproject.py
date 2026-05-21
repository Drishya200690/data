import requests
import pandas as pd

# -------------------------
# STEP 1: API KEY
# -------------------------
API_KEY = "fadd3a5a43ec442d88d956837bad1d63"

# -------------------------
# STEP 2: API URL
# -------------------------
url = f"https://newsapi.org/v2/top-headlines?country=us&pageSize=10&apiKey={API_KEY}"

# -------------------------
# STEP 3: GET DATA
# -------------------------
response = requests.get(url)
data = response.json()

# -------------------------
# STEP 4: EXTRACT NEWS
# -------------------------
articles = data["articles"]

# -------------------------
# STEP 5: PRINT TOP 10 NEWS
# -------------------------
print("\nTOP 10 NEWS HEADLINES\n")

for i, article in enumerate(articles, start=1):
    print(f"{i}. {article['title']}")

# -------------------------
# STEP 6: CONVERT TO DATAFRAME
# -------------------------
df = pd.DataFrame([{
    "Title": a["title"],
    "Source": a["source"]["name"],
    "Published": a["publishedAt"]
} for a in articles])

# -------------------------
# STEP 7: SAVE CSV
# -------------------------
df.to_csv("top10_news.csv", index=False)

print("\nCSV file created: top10_news.csv")

# -------------------------
# STEP 8: SIMPLE INSIGHT
# -------------------------
print("\nNews Source Count:")
print(df["Source"].value_counts())
import requests
import pandas as pd
import matplotlib.pyplot as plt

# ------------------------
# STEP 1: API KEY
# ------------------------
API_KEY = "fadd3a5a43ec442d88d956837bad1d63"


# ------------------------
# STEP 2: GET NEWS DATA
# ------------------------
url = f"https://newsapi.org/v2/top-headlines?country=us&pageSize=10&apiKey={API_KEY}"

response = requests.get(url)
data = response.json()

articles = data["articles"]

# ------------------------
# STEP 3: CREATE DATAFRAME
# ------------------------
df = pd.DataFrame([{
    "Title": a["title"],
    "Source": a["source"]["name"]
} for a in articles])

print(df)

# ------------------------
# STEP 4: COUNT SOURCES
# ------------------------
source_counts = df["Source"].value_counts()

# ------------------------
# STEP 5: PLOT GRAPH
# ------------------------
plt.figure(figsize=(8,5))

source_counts.plot(kind="bar", color="skyblue")

plt.title("Top News Sources (Top 10 News)")
plt.xlabel("News Source")
plt.ylabel("Number of Articles")

plt.xticks(rotation=45)

# Show on screen
plt.show()