import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['total_time'] = employees['out_time'] - employees['in_time']
    employ = employees.groupby(by=['event_day','emp_id'])[['total_time']].sum().sort_values(by='emp_id').reset_index()
    return employ[['event_day','emp_id','total_time']].rename(columns={'event_day': 'day'})
