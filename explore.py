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

away_matches = df[df["AwayTeam"] == team]

print("Partidos como visitante:", len(away_matches))

away_avg = away_matches["FTAG"].mean()

print("Promedio de goles como visitante:", away_avg)


homeTeam = df.groupby("HomeTeam")["FTHG"].mean()

print(homeTeam.sort_values(ascending=False))


home_conceded = df.groupby("HomeTeam")["FTAG"].mean()

print(home_conceded.sort_values())


awayTeam = df.groupby("AwayTeam")["FTAG"].mean()

print("Goles marcados como visitante:")
print(awayTeam.sort_values(ascending=False))


away_conceded = df.groupby("AwayTeam")["FTHG"].mean()

print("Goles recibidos como visitante:")
print(away_conceded.sort_values())


# Home wins = H, Draw D, away = A


Home_wins = df[df["FTR"] == "H"]
Draws = df[df["FTR"] == "D"]
Away_wins = df[df["FTR"] == "A"]

print("Partidos ganados por el equipo local:", len(Home_wins))
print("Partidos empatados:", len(Draws))
print("Partidos ganados por el equipo visitante:", len(Away_wins))
