import pandas as pd


df = pd.read_csv('data/raw/laliga.csv')

print(df.head())
print(df.columns.tolist())
print(df.shape)


print(df["FTR"].value_counts())
print(df["HomeTeam"].nunique())
print(df[["HomeTeam","AwayTeam","FTHG","FTAG"]].head(10))

print("Goles de HomeTeam: ", df["FTHG"].mean())
print("Goles de AwayTeam: ", df["FTAG"].mean())

print("Goles locales ausentes:", df["FTHG"].isna().sum())
print("Goles visitantes ausentes:", df["FTAG"].isna().sum())


home_avg = df["FTAG"].mean()
away_avg = df["FTHG"].mean()

total_avg = home_avg + away_avg
print("Promedio total de goles por partido: ", total_avg)

team = "Barcelona"

matches = df[df["HomeTeam"] == team]

print(matches[["HomeTeam", "FTHG"]].head())
print("Partidos como local:", len(matches))
print("Promedio de goles:", matches["FTHG"].mean())