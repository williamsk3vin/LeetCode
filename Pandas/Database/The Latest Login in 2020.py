import pandas as pd

def latest_login(logins: pd.DataFrame) -> pd.DataFrame:
    filtered = logins.query('time_stamp >= "2020-01-01" and time_stamp < "2021-01-01"')
    grouped = filtered.groupby('user_id')['time_stamp'].max().reset_index(name='last_stamp')
    return grouped
