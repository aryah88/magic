import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('startup_funding.csv')
def normalize_city(city):
    if pd.isnull(city):
        return None
    city = city.split('/')[0].strip().title()  # Take the first city in case of multiple locations
    if city == 'Delhi':
        return 'New Delhi'
    elif city in ['Bangalore', 'Bengaluru']:
        return 'Bangalore'
    return city
df['CityLocation'] = df['CityLocation'].apply(normalize_city)


df = df[df['CityLocation'].notna()]

#df[df['AmountInUSD'==""]]='0'
city_counts = df['AmountInUSD'].value_counts()
sorted_city_counts = city_counts.sort_values(ascending=False)
top_10_cities = sorted_city_counts.head(10)

sum_f=top_10_cities.sum()



for city,count in top_10_cities.items():
    percentage =(count/sum_f)*100 
    print(f'{city}  {percentage:.2f}')
