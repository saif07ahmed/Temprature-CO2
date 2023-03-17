import pandas as pd

co_data=pd.read_csv('./Saif\co2_emissions_kt_by_country.csv')
temp_data=pd.read_csv('./Saif\city_temperature.csv')

co_data.columns=['country_code','Country',"Year",'Co2 Value']
country_year_temp = temp_data.groupby(['Country', 'Year'])['AvgTemperature'].mean()
country_year_df = country_year_temp.to_frame().reset_index()

merged_df = pd.merge(country_year_df, co_data, on=['Country','Year'])
merged_df.to_csv('merged_df.csv')