import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    counts = employee['managerId'].value_counts()
    result = employee[employee['id'].isin(counts[counts >= 5].index)][['name']]
    return result
