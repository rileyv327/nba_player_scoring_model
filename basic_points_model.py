import pandas as pd
import numpy as np
import requests
from nba_api.stats import endpoints
from nba_api.stats.static import players, teams


home_team_players = ["Anthony Edwards", "Karl-Anthony Towns",
                     "Jarred Vanderbilt", "Patrick Beverley", "D'Angelo Russell"]  # starting 5
away_team_players = ["Ja Morant", "Desmond Bane",
                     "Jaren Jackson Jr.", "Kyle Anderson", "Dillon Brooks"]  # starting 5


# get the most recent stats for all players in the game
def get_player_stats(home_team_players, away_team_players):
    home_stats = pd.DataFrame()
    away_stats = pd.DataFrame()
    for h, a in zip(home_team_players, away_team_players):

        h_player = players.find_players_by_full_name(h)[0]
        a_player = players.find_players_by_full_name(a)[0]

        h_data = endpoints.playerdashboardbylastngames.PlayerDashboardByLastNGames(
            h_player["id"])
        h_df = h_data.last10_player_dashboard.get_data_frame()

        a_data = endpoints.playerdashboardbylastngames.PlayerDashboardByLastNGames(
            a_player["id"])
        a_df = a_data.last10_player_dashboard.get_data_frame()

        home_stats = pd.concat([home_stats, h_df])
        away_stats = pd.concat([away_stats, a_df])

    home_stats = home_stats[['GP', 'W', 'L', 'W_PCT', 'MIN', 'FGM',
                            'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT',
                             'OREB', 'DREB', 'REB', 'AST', 'TOV', 'STL', 'BLK', 'BLKA', 'PF', 'PFD',
                             'PTS', 'PLUS_MINUS', 'NBA_FANTASY_PTS', 'DD2', 'TD3']]
    away_stats = away_stats[['GP', 'W', 'L', 'W_PCT', 'MIN', 'FGM',
                            'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT',
                             'OREB', 'DREB', 'REB', 'AST', 'TOV', 'STL', 'BLK', 'BLKA', 'PF', 'PFD',
                             'PTS', 'PLUS_MINUS', 'NBA_FANTASY_PTS', 'DD2', 'TD3']]

    return home_stats, away_stats

# PER MINUTE (multiple by avg minutes to get expected)
# player = last n games / league avg
# opp defense allowed = defense avg last N games/ league avg

# expected points for player = player * opp defense


home, away = get_player_stats(home_team_players, away_team_players)
