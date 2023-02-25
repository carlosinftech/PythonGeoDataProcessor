import pandas as pd
from geopy.geocoders import Nominatim

dvf_df = pd.read_csv("output.txt", sep="|")
print(dvf_df.columns)

#select values of interest, mainly date of transaction type of transaction

print(dvf_df[['Date mutation',
              'Nature mutation',
              'Valeur fonciere',
              ]].head(3))

print(dvf_df[['Code departement',
              'Code commune',
              'Prefixe de section',
              ]].head(3))

print(dvf_df[[
              'Section',
              'No plan']].head(3))

print(dvf_df[[
              'No voie','Type de voie','Voie']].head(3))

print(dvf_df[[
              'Code postal','Commune']].head(3))

#geolocator = Nominatim(user_agent = "carlos_python_geo_processor")
#location = geolocator.geocode("16 rue des rigoles 75020 Paris France")
#print(location.latitude,location.longitude)

dvf_sample3 = dvf_df.head(10)



def str_join(df, sep, *cols):
   from functools import reduce
   return reduce(lambda x, y: x.astype(str).str.cat(y.astype(str), sep=sep),
                      [df[col] for col in cols])

# dvf_sample3['adress'] = dvf_sample3['No voie'].str.cat(dvf_sample3[['Type de voie','Comunne','Departement','Code postal']], sep=' ')
dvf_sample3['adress'] = str_join(dvf_sample3,' ' ,'No voie', 'Type de voie', 'Commune', 'Code departement', 'Code postal')
print(dvf_sample3['adress'])