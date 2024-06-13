import pandas as pd

data = {
    'name': ['Jack','Piper','Mia', 'Ulysses'],
    'salary': [19666, 74754, 62509, 54866],
}

employees = pd.DataFrame(data)

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['salary']= employees['salary']*2
    return employees