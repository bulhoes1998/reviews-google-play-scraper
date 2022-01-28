from google_play_scraper import app, reviews_all
import pandas as pd

gog3_reviews = reviews_all('com.itau.pers', lang='pt_BR', country='br')
print("ok")
df = pd.DataFrame(gog3_reviews)
print("ok")
df.to_csv('pers.csv', index=False)