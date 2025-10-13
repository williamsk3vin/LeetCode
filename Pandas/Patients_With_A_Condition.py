import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    mask = patients['conditions'].apply(lambda cond_str: any(code.startswith("DIAB1") for code in cond_str.split(" ")))
    return patients[mask]
