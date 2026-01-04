import pandas as pd

def find_employees(employees: pd.DataFrame, salaries: pd.DataFrame) -> pd.DataFrame:
    merged = employees.merge(salaries, how = 'outer', on = 'employee_id').drop_duplicates()
    return merged[merged['name'].isna() | merged['salary'].isna()][['employee_id']]
