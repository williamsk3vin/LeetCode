import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    join_df = pd.merge(employees, employee_uni, how='left', on='id')
    return join_df[['name','unique_id']]
