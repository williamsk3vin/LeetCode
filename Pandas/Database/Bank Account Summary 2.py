import pandas as pd

def account_summary(users: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    trans1 = transactions.groupby('account')['amount'].sum().reset_index(name='balance')
    merged = users.merge(trans1, how='left', on='account')
    return merged.query('balance > 10000')[['name','balance']]
