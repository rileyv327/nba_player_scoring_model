import pandas as pd
import numpy as np
import requests
from nba_api.stats import endpoints
from nba_api.stats.static import players, teams


data = endpoints.playerestimatedmetrics.PlayerEstimatedMetrics()

df = data.player_estimated_metrics.get_data_frame()

home_team_players = ["Anthony Edwards", "Karl-Anthony Towns",
                     "Jarred Vanderbilt", "Patrick Beverley", "D'Angelo Russell"]  # starting 5
away_team_players = ["Ja Morant", "Desmond Bane",
                     "Jaren Jackson Jr.", "Kyle Anderson", "Dillon Brooks"]  # starting 5

home_stats = pd.DataFrame()
away_stats = pd.DataFrame()

home_team = teams.find_teams_by_city("Memphis")
away_team = teams.find_teams_by_city("Dallas")

for h, a in zip(home_team_players, away_team_players):
    home_stats = pd.concat([home_stats, df.loc[df['PLAYER_NAME'] == h]])
    away_stats = pd.concat([away_stats, df.loc[df['PLAYER_NAME'] == a]])

print(home_stats)
