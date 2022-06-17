import requests
import pandas as pd
import time
import re
from sqlalchemy import create_engine

time.sleep(30)

while True:
    #pg = create_engine('postgresql://postgres:loop@0.0.0.0:5555/postgres', echo=True)
    pg = create_engine('postgresql://postgres:1234@postgresdb:5432/postgres', echo=True)

    query = pg.execute('''SELECT * FROM tweets ORDER BY sentiment DESC LIMIT 1;''')

    #pp = list(query)
    kk = str(list(query)[0])
    #te = str(re.findall(r'\w.+',kk))
    webhook_url = "https://hooks.slack.com/services/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"
    tweet = {
        "text": kk
    }
    requests.post(url=webhook_url, json = tweet)
    time.sleep(30)