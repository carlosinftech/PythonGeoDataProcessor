import pandas as pd
from datetime import datetime
import uuid

class Transformer:

    def __init__(self,data:pd.DataFrame):
        self.data = data

    def cast_to_date(self,column_name:str,datetime_format:str):
        self.data[column_name] = pd.to_datetime(column_name,format = datetime_format)
        return self

    def add_literal_to_df(self,column_name:str,literal:str):
        self.data[column_name] = literal
        return self

    def select_columns(self,column_name:str,literal:str):
        self.data[column_name] = literal
        return self

    def create_column_from_index(self,column_name:str):
        self.data[column_name] = self.data.index
        return self

