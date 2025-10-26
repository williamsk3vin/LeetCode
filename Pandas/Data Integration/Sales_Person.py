import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:

    merged = pd.merge(orders, company, on='com_id', how='left')
    red_sales = merged.loc[merged['name'] == 'RED', 'sales_id'].unique()
    result = sales_person[~sales_person['sales_id'].isin(red_sales)][['name']]
    
    return red_sales
