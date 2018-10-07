'''
Python for Machine Learning - P89

Topic to be covered - Unveil the ipaddress to get the treasure of Information

'''

import pandas as pd
import pygeoip 

gi = pygeoip.GeoIP('GeoIP.dat')
gi.country_code_by_addr('64.233.161.99')  
gi.country_name_by_addr('64.233.161.99')  

gp = pygeoip.GeoIP('GeoLiteCity.dat')
gp.record_by_addr('100.10.100.1')

df = pd.read_csv('ipaddress1.csv')

ip1 = []
for x in range(len(df)):
    z = gp.record_by_addr(df.iloc[x][0])
    ip1.append(z)

df1=pd.DataFrame(ip1, columns=['area_code','city','continent','country_code','country_code3',
                                   'country_name','dma_code','latitude','longitude','metro_code',
                                   'postal_code','region_code','time_zone'])

ip2 = []
for i in range(len(ip1)):
    if ip1[i] is not None:
        ip2.append(ip1[i])
        print(ip1[i])
        
df2=pd.DataFrame(ip2, columns=['area_code','city','continent','country_code','country_code3',
                                   'country_name','dma_code','latitude','longitude','metro_code',
                                   'postal_code','region_code','time_zone'])     
