import pandas as pd
from datetime import datetime, time, timedelta
def get_employees():
    now = datetime.utcnow()
    df = pd.DataFrame({
        "Name":["Alice","Bob","James","Harald"],
        "DOJ":[now, now-timedelta(weeks=13),now-timedelta(weeks=52),now-timedelta(weeks=102)],
        "Interest":["C#","Python","Javascript","Typescript"]
    })
    print(df)
    return df