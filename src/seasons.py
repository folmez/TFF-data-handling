import src

import datetime
import pandas as pd

# Default years
START, END = 1000, 3000

def get_season_info(filename, league_name, start=START, end=END):
    assert end-start is 1

    df = src.read_csv_into_data_frame(filename, silent=True)

    # Leagues generally are on a break in July
    start_datetime = datetime.datetime(start,7,1,0,0,0)
    end_datetime = datetime.datetime(end,7,1,0,0,0)

    # Remove matches that are not needed
    df = df.drop(df[df['Organizasyon'] != league_name].index)
    df = df.drop(df[df['Tarih'] < start_datetime].index)
    df = df.drop(df[df['Tarih'] > end_datetime].index)

    teams, team_ids = check_whether_ev_and_deplasman_are_identical(df)

    # Print season summary
    print('                    Season:', start, '-', end)
    print('                    League:', league_name)
    print('           Number of teams:', len(team_ids))
    print('         Number of matches:', len(df))
    print(' Number of missing matches:', len(team_ids)*(len(team_ids)-1) - len(df))
    get_missing_matches(df, team_ids)

def check_whether_ev_and_deplasman_are_identical(df):
    home_teams = df['Ev'].unique()
    away_teams = df['Deplasman'].unique()
    assert set(home_teams) == set(away_teams)

    home_team_ids = df['Ev ID'].unique()
    away_team_ids = df['Deplasman ID'].unique()
    assert set(home_team_ids) == set(away_team_ids)

    return home_teams, home_team_ids

def get_missing_matches(df, team_ids):
    for h in team_ids:
        for a in team_ids:
            if h != a:
                if len(df[(df['Ev ID'] == h) & (df['Deplasman ID'] == a)]) is not 1:
                    print('                   Missing:',\
                        team_id_to_name(df, h), '-', team_id_to_name(df, a))

def team_id_to_name(df, team_id):
    df_ev = df.drop(df[df['Ev ID'] != team_id].index)
    ev_name = df_ev['Ev'].unique()
    df_dep = df.drop(df[df['Deplasman ID'] != team_id].index)
    dep_name = df_dep['Deplasman'].unique()
    assert len(ev_name) == 1 and len(dep_name) == 1 and ev_name == dep_name
    return ev_name
