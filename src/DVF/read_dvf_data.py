import pandas as pd

from src.pipeline.transformer import Transformer


pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 2000)
pd.set_option('display.float_format', '{:20,.2f}'.format)
pd.set_option('display.max_colwidth', None)

def transformDVFData():
    dvf_df = pd.read_csv("output.txt", sep="|",nrows =10,dtype=object)
    dvf_transformer = Transformer(dvf_df)
    final_df = dvf_transformer.add_literal_to_df("country","France")\
        .concatenate_columns("full_adress"," ",['No voie','Type de voie','Voie','Code postal','Commune','country'])\
        .drop_na_in_columns(['No voie','Type de voie'])\
        .get_longitude_and_latitude_from_adress("full_adress","latitude","longitude")\
        .select_columns(["full_adress","latitude","longitude","Date mutation","Nature mutation","Valeur fonciere"])\
        .data
    print(final_df)


transformDVFData()