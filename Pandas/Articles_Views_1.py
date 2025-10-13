import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    return views.query('author_id == viewer_id')[['author_id']].rename(columns={'author_id': 'id'}).drop_duplicates().sort_values(by='id', ascending=True)
