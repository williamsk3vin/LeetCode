import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
  # ^ == 'startswith 
  # * == endswith
  # $ nothing else passed what is written
    return users[(users['mail'].str.match('^[A-Za-z][A-Za-z0-9._-]*@leetcode\.com$'))]
