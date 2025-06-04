from numpy import nan
import pandas as pd
from functools import reduce
from datetime import datetime

from utilities import Utilities


class Chagas:
    util = Utilities()

    def __init__(self):
        ...


    def extract(self) -> pd.DataFrame:
        return reduce(lambda a, b: pd.concat([a, b], axis=0)
                      , map(lambda x: pd.read_parquet(x), self.util.get_files_path_chagas())
                      )

    def transform(self,df:pd.DataFrame):
        # tratando valores que estão vazios
        df['CS_RACA'] = self.util.remove_nan_null(df, col_name='CS_RACA')

        df['CRITERIO'] = self.util.remove_nan_null(df, col_name='CRITERIO')

        df['EVOLUCAO'] = self.util.remove_nan_null(df, col_name='EVOLUCAO')

        df['CLASSI_FIN'] = self.util.remove_nan_null(df, col_name='CLASSI_FIN')

        # Substituindo as informações pelos reais valores que estão na tabela

        #Raça: 1=branca | 2=preta | 3=amarela | 4=parda | 5=indígena | 9=Sem registro
        df['CS_RACA'] = df['CS_RACA'].astype(str).map(self.util.category_race).fillna(df['CS_RACA'])

        #Criterio: 1=Laboratorial | 2=Clínico-Epidemiológico | 3=Clínico
        df['CRITERIO'] = df['CRITERIO'].astype(str).map(self.util.category_CRITERIO).fillna(df['CRITERIO'])

        #Evolucao: 1=Vivo | 2=Óbito por doença de Chagas aguda | 3=Óbito por outras causas | 9=Ignorado
        df['EVOLUCAO'] = df['EVOLUCAO'].astype(str).map(self.util.category_EVOLUCAO).fillna(df['EVOLUCAO'])

        #Classificacao Final: 1=Confirmado | 2=Descartado | 3=Inconclusivo
        df['CLASSI_FIN'] = df['CLASSI_FIN'].astype(str).map(self.util.category_classi_final).fillna(df['CLASSI_FIN'])

        # Calcula a idade
        current_year = datetime.now().year
        df['idade'] = df['ANO_NASC'].replace(" ", nan)
        df['ANO_NASC'] = pd.to_numeric(df['ANO_NASC'], errors='coerce')
        df['idade'] = current_year - df['ANO_NASC']

        # Ajeita as Siglas #NUMERO ESTADO DO PARÁ = 15
        df_aux_mun = self.util.extract_dim_municipios()[['uf', 'sigla']].drop_duplicates()

        #Caso queira pelo numero do estado enves da sigla - descomentar esta linha e comentar a outra
        # uf_dict = df_aux_mun.set_index('sigla')['uf'].to_dict()
        uf_dict = df_aux_mun.set_index('uf')['sigla'].to_dict()

        df['SG_UF_NOT'] = df['SG_UF_NOT'].map(uf_dict).fillna(df['SG_UF_NOT'])
        df['SG_UF'] = df['SG_UF'].map(uf_dict).fillna(df['SG_UF'])

        # Corrige tipos de coluna problemáticas antes de salvar com pyarrow
        for col in df.select_dtypes(include='object').columns:
            df[col] = df[col].where(df[col].notna(), None).astype("string")

        return df

    def load(self,df:pd.DataFrame) ->None:
        df.to_parquet("chagas_consolidado.parquet", index=False, engine='pyarrow')

    def execute(self):
        df = self.extract()

        df = self.transform(df)

        self.load(df)

if __name__ == '__main__':
    Chagas().execute()