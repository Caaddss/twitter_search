from twitter import *
import json
import pandas as pd

# Tratando erro de importação do json
try:
    import json
except ImportError:
    import simplejson as json

# Load credentials from json file
with open("twitter_credentials.json", "r") as file:  
    creds = json.load(file)



# Instanciando um objeto
credentials_tw_api = Twitter(auth=OAuth(creds['ACCESS_TOKEN'], creds['ACCESS_TOKEN_SECRET'], creds['CONSUMER_KEY'], creds['CONSUMER_SECRET']))

# Criando a query

query = {
    'q':'marina silva',
    'result_type':'popular',
    'count':'50',
    'lang': 'pt',
}

# Criando a busca
busca = credentials_tw_api.search.tweets(q='marina silva', result_type='popular', count='50', lang='pt')

# Procurando os tweets
dict_ = {'user': [], 'date': [], 'text':[],'favorite_count':[]}
for status in busca['statuses']:
    dict_['user'].append(status['user']['screen_name'])
    dict_['date'].append(status['created_at'])
    dict_['text'].append(status['text'])
    dict_['favorite_count'].append(status['favorite_count'])

# Estruturando os dados em um dataframe do Pandas
df = pd.DataFrame(dict_)
df.sort_values(by='favorite_count', inplace=True, ascending=False)
print(df.head(5))