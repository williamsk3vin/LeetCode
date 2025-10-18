import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    first = activity.sort_values(by=['player_id','event_date'], ascending=True).drop_duplicates(subset='player_id',keep='first')
    return first[['player_id','event_date']].rename(columns={'event_date': 'first_login'})
