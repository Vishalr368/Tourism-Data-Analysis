import pandas as pd
import numpy as np

df = pd.read_csv('cleaned tourism data')

df['date']=pd.to_datetime(df['date'])
#print(df)

#analysis of domestic visitors .
#list down the top 10 districts that have the highest number of domestic visitors overall (2016-2019)?.

grouped_data= df.groupby('district')['visitors'].sum()
#print(grouped_data)
sorted_data = grouped_data.sort_values(ascending=False)
top10_district= sorted_data.head(10)
#print(top10_district)


#calculating number of visitors each years of every district.
all_data = df.groupby(['district','year'])['visitors'].sum()
sort_dis= all_data.sort_values(ascending=False)
top3_district= sort_dis.head(3)
#print(top3_district)

#calculating CAGR for each district.
def calculate_cagr(start_value, end_value, num_years):
    return (end_value / start_value) ** (1 / num_years) - 1

valid_districts = all_data.dropna().index
cagr_by_district = (all_data.loc[valid_districts, 2019] / all_data.loc[valid_districts, 2016]) ** (1 / 3) - 1
top_3_districts = cagr_by_district.nlargest(3)
print(top_3_districts)



