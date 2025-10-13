import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    order_ids = orders['customerId'].unique()
    return customers[~customers['id'].isin(order_ids)][['name']].rename(columns={'name': 'Customers'})
