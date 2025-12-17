import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    result = person['email'].value_counts().reset_index().query('count > 1')[['email']]
    return result
