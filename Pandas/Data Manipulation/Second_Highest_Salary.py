import pandas as pd
import numpy as np

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    #Drop duplicates and sort values in Employee['salary']
    salary = employee['salary'].drop_duplicates().sort_values(ascending=False).reset_index(drop=True)
    #Selecting the second highest salary or making the value null
    if len(salary) < 2:
        salary_2nd = np.nan

    else:
        salary_2nd = salary.iloc[1]
    
    #returning a new renamed dataframe with the salary value
    return pd.DataFrame({f'SecondHighestSalary': [salary_2nd]})
