import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    course = courses['class'].value_counts().reset_index()
    return course.query('count >= 5')[['class']]
