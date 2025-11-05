import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(employee, department, left_on='departmentId', right_on='id', how='inner')
    max_salary = merged.groupby('name_y')['salary'].max().reset_index()
    result = pd.merge(merged, max_salary, on=['name_y', 'salary'])
    result = result[['name_y', 'name_x', 'salary']].rename(
        columns={'name_y': 'Department', 'name_x': 'Employee', 'salary': 'Salary'}
    )
    return result
