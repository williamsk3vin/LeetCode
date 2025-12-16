import pandas as pd

def swap_salary(salary: pd.DataFrame) -> pd.DataFrame:
    salary['sex'] = salary['sex'].replace(['m','f'], ['f','m'])
    return salary


def swap_salary(salary: pd.DataFrame) -> pd.DataFrame:
    salary['sex'] = salary['sex'].map(lambda x: 'm' if x == 'f' else ('f' if x == 'm' else 'f'))
    return salary
