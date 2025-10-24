import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    # Step 1: Count how many exams each student attended per subject
    attended = examinations.groupby(['student_id','subject_name'], as_index=False).size().rename(columns={'size':'attended_exams'})
    
    # Step 2: Create all student-subject combinations
    cross = pd.merge(students, subjects, how='cross')
    
    # Step 3: Merge with attended exams, fill missing with 0
    result = pd.merge(cross, attended, on=['student_id','subject_name'], how='left')
    result['attended_exams'] = result['attended_exams'].fillna(0).astype(int)
    
    # Step 4: Optional sort
    result = result.sort_values(['student_id','subject_name']).reset_index(drop=True)
    
    return result
