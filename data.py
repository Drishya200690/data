import pandas as pd 

table = pd.read_csv("archive/imdb_top_1000.csv")
print(table)
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load IMDb dataset
df = pd.read_csv("imdb_top_1000.csv")

# Display first 5 rows
print("First 5 Rows:")
print(df.head())

# ---------------------------------------------------
# 1. Highest Rated Movies
# ---------------------------------------------------

top_movies = df.sort_values(by="IMDB_Rating", ascending=False)

print("\nTop 10 Highest Rated Movies:")
print(top_movies[["Series_Title", "IMDB_Rating"]].head(10))

# Bar chart
plt.figure(figsize=(10,5))
sns.barplot(
    x=top_movies["IMDB_Rating"].head(10),
    y=top_movies["Series_Title"].head(10),
    palette="viridis"
)

plt.title("Top 10 Highest Rated Movies")
plt.xlabel("IMDb Rating")
plt.ylabel("Movie")
plt.show()

# ---------------------------------------------------
# 2. Most Common Genres
# ---------------------------------------------------

genre_count = df["Genre"].value_counts()

print("\nMost Common Genres:")
print(genre_count.head(10))

# Pie chart
plt.figure(figsize=(8,8))
genre_count.head(5).plot(
    kind="pie",
    autopct='%1.1f%%'
)

plt.title("Top 5 Movie Genres")
plt.ylabel("")
plt.show()

# ---------------------------------------------------
# 3. Longest Runtime Movies
# ---------------------------------------------------

# Convert Runtime into numeric minutes
df["Runtime_Minutes"] = df["Runtime"].str.replace(" min", "").astype(int)

longest_movies = df.sort_values(
    by="Runtime_Minutes",
    ascending=False
)

print("\nTop 10 Longest Movies:")
print(longest_movies[
    ["Series_Title", "Runtime"]
].head(10))

# ---------------------------------------------------
# 4. Top Directors by Number of Movies
# ---------------------------------------------------

director_count = df["Director"].value_counts()

print("\nTop Directors:")
print(director_count.head(10))

# Bar chart
plt.figure(figsize=(10,5))
sns.barplot(
    x=director_count.head(10).values,
    y=director_count.head(10).index,
    palette="magma"
)

plt.title("Top Directors by Movie Count")
plt.xlabel("Number of Movies")
plt.ylabel("Director")
plt.show()

# ---------------------------------------------------
# 5. Average IMDb Rating by Certificate
# ---------------------------------------------------

certificate_rating = df.groupby(
    "Certificate"
)["IMDB_Rating"].mean()

print("\nAverage IMDb Rating by Certificate:")
print(certificate_rating)

# Bar chart
plt.figure(figsize=(8,5))
certificate_rating.sort_values().plot(
    kind="bar",
    color="skyblue"
)

plt.title("Average IMDb Rating by Certificate")
plt.xlabel("Certificate")
plt.ylabel("Average Rating")
plt.show()

# ---------------------------------------------------
# Correlation Heatmap
# ---------------------------------------------------

plt.figure(figsize=(8,5))

sns.heatmap(
    df.corr(numeric_only=True),
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Heatmap")
plt.show()

