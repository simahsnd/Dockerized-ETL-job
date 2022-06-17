import requests
import pandas as pd
import time
import re
from sqlalchemy import create_engine

time.sleep(30)

while True:
    
    pg = create_engine('', echo=True)

    query = pg.execute('''SELECT * FROM tweets ORDER BY sentiment DESC LIMIT 1;''')

  
    kk = str(list(query)[0])
   
    webhook_url = ""
    tweet = {
        "text": kk
    }
    requests.post(url=webhook_url, json = tweet)
    time.sleep(30)
