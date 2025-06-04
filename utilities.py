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
            os.path.abspath(os.path.join("Bases_Chagas", base_diretory))
            for base_diretory in os.listdir("Bases_Chagas")
        ]


    def extract_dim_municipios(self):
        df = pd.read_excel("RELATORIO_DTB_BRASIL_MUNICIPIO.xlsx"
                             ,skiprows=6
                             )

        df = df.rename(columns={
            'UF': 'uf'
            ,'Nome_UF':'nome_uf'
            , 'Código Município Completo': 'cod_mun'
        })
        df['uf'] = df['uf'].astype(str)

        df['sigla'] = df['nome_uf'].map(self.acronym_states)

        return df

    def remove_nan_null(self,df,col_name):
        df[col_name] = df[col_name].replace(" ", nan, regex=True)
        df[col_name] = pd.to_numeric(df[col_name], errors='coerce').astype('Int64')

        return df[col_name]


if __name__ == '__main__':
    ...