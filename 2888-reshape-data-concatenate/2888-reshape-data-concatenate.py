import pandas as pd

# data1 = {
#     'student_id': [1,2,3,4],
#     'name':['Mason','Ava','Taylor','Georgia'],
#     'age':[8,6,15,17],
# }

# data2 = {
#     'student_id': [5,6],
#     'name':['Leo','Alex'],
#     'age':[7,7],
# }


def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    df=pd.concat([df1,df2])
    return df