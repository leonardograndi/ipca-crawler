import pandas as pd
import html5lib
import matplotlib.pyplot as plt
import seaborn as sns
import requests

url = 'https://www.portalbrasil.net/ipca/'

header = { 
  'User-Agent': 'Mozilla/5.0'
}

result = requests.get(url, headers = header)

ipca = pd.read_html(result.text)

ipca = ipca[1]

rename_column = ipca.columns.values
rename_column[0] = 0
rename_column[3] = 3

ipca.columns = rename_column

ipca = ipca[[0,3]]
ipca = ipca.iloc[1:]

df = ipca[3].astype(float) / 10000
df = pd.concat([ipca, df], axis = 1)
df.columns = ['Data', 'IPCA_OLD', 'IPCA']
df = df[['Data','IPCA']]
df.set_index(['Data'], inplace = True)  

del(ipca)

# Reverse order
df = df.iloc[::-1]

df.to_csv('ipca.csv', sep=';', encoding='utf-8')

print('Extract data - Success')
