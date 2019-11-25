import pandas as pd
df=pd.read_csv('cars.csv')
cars=pd.concat([df.head(5),df.tail(5)])
