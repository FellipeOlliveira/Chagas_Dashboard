#THIS SCRIPT ONLY WORK FOR LINUX
#Cause pysus libary can only be downloaded on linux env

#from pysus.online_data import SINAN
#import pandas as pd
from pprint import pprint

#variaveis ultilizadas
diseases = 'CHAG'
years = ['2024']
data_path='.'
uf = 'PA'

#metadados da coluna
#metadata =  SINAN.metadata_df(diseases)
#df_meta = pd.DataFrame(metadata)
#df_meta.to_excel("metadados_sinan.xlsx",index=False)


#Para baixar as bases por ano e colocar em uma pasta
#SINAN.download(diseases=deseasses,years=years,data_path=data_path)

#pegando os anos disponiveis
#available_years = SINAN.get_available_years('CHAG')
#for year in available_years:
# print(f'Ano disponivel: {year}')
