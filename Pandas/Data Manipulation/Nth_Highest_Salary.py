import pandas as pd
import numpy as np

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    # Step 1 & 2: distinct salaries, sorted descending
    salaries = employee['salary'].drop_duplicates().sort_values(ascending=False).reset_index(drop=True)
    
    # Step 3 & 4: check if N is valid and get the Nth salary
    if N <= 0 or N > len(salaries):
        nth_salary = np.nan

    else:
        nth_salary = salaries.iloc[N - 1]
    
    # Step 5: wrap in DataFrame with correct column name
    return pd.DataFrame({f'getNthHighestSalary({N})': [nth_salary]})

