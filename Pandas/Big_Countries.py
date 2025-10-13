import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    return world.query('area >= 3_000_000 or population >= 25_000_000')[['name','area','population']]
