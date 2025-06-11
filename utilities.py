import os
import pandas as pd
from functools import reduce
from numpy import nan


class Utilities:
    acronym_states = {
        'Acre': 'AC',
        'Alagoas': 'AL',
        'Amapá': 'AP',
        'Amazonas': 'AM',
        'Bahia': 'BA',
        'Ceará': 'CE',
        'Distrito Federal': 'DF',
        'Espírito Santo': 'ES',
        'Goiás': 'GO',
        'Maranhão': 'MA',
        'Mato Grosso do Sul': 'MS',
        'Mato Grosso': 'MT',
        'Minas Gerais': 'MG',
        'Pará': 'PA',
        'Paraíba': 'PB',
        'Paraná': 'PR',
        'Pernambuco': 'PE',
        'Piauí': 'PI',
        'Rio de Janeiro': 'RJ',
        'Rio Grande do Norte': 'RN',
        'Rio Grande do Sul': 'RS',
        'Rondônia': 'RO',
        'Roraima': 'RR',
        'Santa Catarina': 'SC',
        'São Paulo': 'SP',
        'Sergipe': 'SE',
        'Tocantins': 'TO',
    }

    category_race = {
        "1": 'branca'
        , "2": 'preta'
        , "3": 'amarela'
        , "4": 'parda'
        , "5": 'indígena'
        , "9": 'Sem registro'
    }

    category_classi_final = {
        '1': 'Confirmado'
        , '2': 'Descartado'
        , '3': 'Inconclusivo'
        , '8':'Inconclusivo'
    }

    category_CRITERIO = {
        '1': 'Laboratorial'
        , '2': 'Clínico-Epidemiológico'
        , '3': 'Clínico'
    }

    category_EVOLUCAO = {
        '1': 'Vivo'
        , '2': 'Óbito por doença de Chagas aguda'
        , '3': 'Óbito por outras causas'
        , '9': 'Ignorado'
    }

    def __init__(self):
        pass

    def get_files_path_chagas(self) ->list:
        return [
            os.path.abspath(os.path.join("SINAN_CHAGAS_ANO", base_diretory))
            for base_diretory in os.listdir("SINAN_CHAGAS_ANO")
        ]

    def extract_dim_municipios(self):
        df = pd.read_csv("Dim_Municipios_Pa.csv"
                             ,delimiter=';'
                             )

        df['CD_MUN'] = df['CD_MUN'].astype(str)
        df['CD_UF'] = df['CD_UF'].astype(str)


        return df

    def remove_nan_null(self,df,col_name):
        df[col_name] = df[col_name].replace(" ", nan, regex=True)
        df[col_name] = pd.to_numeric(df[col_name], errors='coerce').astype('Int64')

        return df[col_name]


if __name__ == '__main__':
    Utilities().extract_dim_municipios()