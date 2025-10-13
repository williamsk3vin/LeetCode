import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
# Step 1: Start by copying salary into a new 'bonus' column
    employees['bonus'] = employees['salary']

# Step 2: Build the mask for employees who should get 0 bonus
    mask = (employees['employee_id'] % 2 == 0) | (employees['name'].str.startswith('M'))

# Step 3: Assign 0 to the 'bonus' column wherever the mask is True
    employees.loc[mask, 'bonus'] = 0

# Step 4: Return only the columns required, sorted by employee_id if needed
    return employees[['employee_id', 'bonus']].sort_values(by='employee_id', ascending=True)
