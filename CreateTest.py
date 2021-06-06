import pandas as pd

df_station_hour = pd.read_csv("station_hour.csv", parse_dates = ["Datetime"] )
df =df_station_hour


df[df['AQI'].isnull()].dropna(subset=['PM2.5','PM10','NO','NO2','NOx','NH3','CO','SO2','O3','Benzene','Toluene','Xylene']).to_csv("test.csv")


