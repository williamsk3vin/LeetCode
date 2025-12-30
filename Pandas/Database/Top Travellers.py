import pandas as pd

def top_travellers(users: pd.DataFrame, rides: pd.DataFrame) -> pd.DataFrame:
    rides1 = rides.groupby('user_id')['distance'].sum().reset_index(name='travelled_distance')
    merged = users.merge(rides1, left_on='id', right_on='user_id', how='left').fillna(0)
    return merged[['name','travelled_distance']].sort_values(['travelled_distance','name'], ascending=[False, True])
