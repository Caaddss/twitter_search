from twitter import *
import pandas as pd
try:
    import simplejson as json
except ImportError:
    from json import json

# Load credentials from json file
with open("twitter_credentials.json", "r") as api_tokens:  
    creds = json.load(api_tokens)

# Instanciando um objeto
credentials_tw_api = Twitter(auth=OAuth(creds['ACCESS_TOKEN'], creds['ACCESS_TOKEN_SECRET'], creds['CONSUMER_KEY'], creds['CONSUMER_SECRET']))

# Criando a busca
search = credentials_tw_api.search.tweets(q='marina silva', result_type='popular', count='50', lang='pt')

# Iniciando o dicionário da busca
search_keys = {'user': [], 'date': [], 'text':[],'favorite_count':[]}

# Organizando uma lista para cada chave
for status in busca['statuses']:
    dict_['user'].append(status['user']['screen_name'])
    dict_['date'].append(status['created_at'])
    dict_['text'].append(status['text'])
    dict_['favorite_count'].append(status['favorite_count'])

# Estruturando os dados em um dataframe do Pandas
df = pd.DataFrame(dict_)
df.sort_values(by='favorite_count', inplace=True, ascending=False)
print(df.head(5))