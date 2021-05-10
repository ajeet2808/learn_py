import pandas as pd
from datetime import datetime
from demo_lib import dummy_data
def get_df():
    df = pd.DataFrame({
        "Name":["Alice", "Bob", "James","Harald"],
        "DOJ":[datetime(year=2016,month=9,day=1),datetime(year=2017,month=10,day=1),datetime(year=2018,month=11,day=1),datetime(year=2019,month=12,day=1)],
        "ProgammingLanguage":["Javascript","Typescript","Python","C#"]
    })
    return df

def get_employees():
    df = dummy_data.get_employees()
    return df