import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    order = orders.value_counts('customer_number').reset_index()
    return order[['customer_number']].iloc[[0]]


