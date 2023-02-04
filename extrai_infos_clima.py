import os
from os.path import join
import pandas as pd
from datetime import datetime, timedelta

data_inicio = datetime.today().strftime('%Y-%m-%d')
data_fim = (datetime.today() + timedelta(days=7)).strftime('%Y-%m-%d')
city = 'Vitoria'
key = '226Q4L8WS5FHK66KYMCBDT8L6'

URL = join("https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/",
          f"{city}/{data_inicio}/{data_fim}?unitGroup=metric&include=days&key={key}&contentType=csv")



dados = pd.read_csv(URL)
print(dados.head())


file_path = f'/home/daniel/Documents/curso_airflow/datapipeline/semana={data_inicio}/'
os.mkdir(file_path)

dados.to_csv(file_path + 'dados_brutos.csv')
dados[['datetime','tempmin', 'temp', 'tempmax']].to_csv(file_path + 'temperaturas.csv')
dados[['datetime', 'description', 'icon']].to_csv(file_path + 'condicoes.csv')
