import pandas as pd

def list_products(products: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    merged = products.merge(orders, how='inner', on='product_id')

    between_dates = merged.query(
        "order_date >= '2020-02-01' & order_date < '2020-03-01'"
    )

    result = (
        between_dates
        .groupby('product_name', as_index=False)['unit']
        .sum()
        .query('unit >= 100')
    )

    return result
