import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    result = employee.merge(employee, 
    left_on='managerId', 
    right_on='id',
    suffixes=('_employee', '_manager'),
    how='inner')
    return result.query('salary_employee > salary_manager')[['name_employee']].rename(columns={'name_employee':'Employee'})
