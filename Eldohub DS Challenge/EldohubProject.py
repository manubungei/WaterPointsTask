from urllib.request import urlopen
  
# import json and pandas
import json
import pandas as pd

url = "https://raw.githubusercontent.com/onaio/ona-tech/master/data/water_points.json"
  
response = urlopen(url)
  
data_json = json.loads(response.read())
  
# print json response
water_df = pd.DataFrame(data_json)
#print(water_df.head())

new_water = pd.DataFrame(water_df[['communities_villages', 'water_functioning']].copy())
#print(new_water)

def water_points():
    wf = pd.DataFrame(new_water.water_functioning.value_counts())
    rank = new_water.groupby('communities_villages')
    rank1 = rank.water_functioning.count()
    df = pd.DataFrame(rank1)
    pd.set_option('display.max_rows', None)
    df.rename(columns={'communities_villages': 'Community', 'water_functioning': 'No. of Water Points'}, inplace=True)
    newdf = new_water[(new_water.water_functioning=='no')]
    newdf = newdf.groupby('communities_villages').count()
    newdf = pd.DataFrame(newdf)
    newdf.rename(columns={'communities_villages': 'Community', 'water_functioning': 'Broken Water Pipes'}, inplace=True)
    rank_df = pd.DataFrame(newdf.sort_values('Broken Water Pipes', ascending=False))
    print('1. The number of water points that are functional:', wf['water_functioning'][0])
    print('2. The number of water points per community',df)
    print('3. The Rank of each Community by broken pipes:',rank_df)
    return
water_points()