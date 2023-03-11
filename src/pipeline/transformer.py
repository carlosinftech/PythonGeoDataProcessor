import pandas as pd
from datetime import datetime
from geopy.geocoders import Nominatim
from geopy.location import Location
import uuid

class Transformer:

    def __init__(self,data:pd.DataFrame):
        self.geolocator = Nominatim(user_agent="carlos_python_geo_processor")
        self.data = data

    def cast_to_date(self,column_name:str,datetime_format:str):
        self.data[column_name] = pd.to_datetime(column_name,format = datetime_format)
        return self

    def add_literal_to_df(self,column_name:str,literal:str):
        self.data[column_name] = literal
        return self

    def select_columns(self,columns:list[str]):
        self.data = self.data[columns]
        return self

    def create_column_from_index(self,column_name:str):
        self.data[column_name] = self.data.index
        return self

    def create_timestamp_column(self,column_name:str):
        self.data[column_name] = self.data.index
        return self

    def concatenate_columns(self, column_name:str, separator:str, cols_to_concat:list[str]):
        temp_df = self.data[cols_to_concat]
        temp_df[cols_to_concat] = temp_df[cols_to_concat].astype(str)
        temp_df[column_name] = temp_df[cols_to_concat].apply(separator.join,axis = 1)
        self.data = self.data.join(temp_df[column_name])
        return self

    def rename_column(self,old_column:str, new_column:str):
        self.data= self.data.rename({old_column:new_column},axis = 'columns')

    def generate_uuid_column(self,column_name:str):
        self.data[column_name] = [str(uuid.uuid4()) for _ in range(len(self.data.index))]

    def cast_date_to_string(self,column_name:str,expected_output_format:str):
        self.data[column_name] = self.data[column_name].dt.strftime(expected_output_format)
        return self

    def drop_na_in_columns(self,columns:list[str]):
        self.data = self.data[self.data[columns].notnull().all(1)]
        return self

    def __get_location_of_address(self,adress:str):
        location = self.geolocator.geocode(adress)
        return location

    def __get_latitude(self,geoloc:Location):
        return geoloc.latitude

    def __get_longitude(self,geoloc:Location):
        return geoloc.longitude

    def get_longitude_and_latitude_from_adress(self,adress_column:str,latitude_column:str,longitude_column:str):
        self.data['geoloc'] = self.data[adress_column].apply(lambda x:self.__get_location_of_address(x))
        self.data[latitude_column] = self.data['geoloc'].apply(lambda x:self.__get_latitude(x))
        self.data[longitude_column] = self.data['geoloc'].apply(lambda x: self.__get_longitude(x))
        self.data = self.data.drop('geoloc', axis=1)
        return self
