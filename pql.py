from typing import List, Dict, Tuple
import pandas as pd
import sqlite3


class PQL:

    def __init__(self, dataframe: Tuple[pd.DataFrame, str]):

        self.cnx = sqlite3.connect(':memory:')

        if isinstance(dataframe, List):
            for frame in dataframe:
                frame[0].to_sql(name=frame[1], con=self.cnx)
        
        elif isinstance(dataframe, Tuple):
            dataframe[0].to_sql(name=dataframe[1], con=self.cnx)
        
        else:
            dataframe.to_sql(name='x', con=self.cnx)
    
    def q(self, query):
        return pd.read_sql(query, self.cnx)
