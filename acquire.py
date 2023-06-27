#Import Libraries
import pandas as pd
import numpy as np
import os
from pydataset import data

# Acquire
from env import host, user, password

# Create a function that retrieves the necessary connection URL.

def get_connection(db_name):
    """
    This function uses my info from my env file to
    create a connection url to access the Codeup db.
    """
    return f'mysql+pymysql://{user}:{password}@{host}/{db_name}'

# Create function to retrieve telco_churn data
def get_telco_churn_data():
    """
    This function reads in the Telco Churn data from the Codeup db
    and returns a pandas DataFrame with all columns.
    """
    filename = 'telco.csv'

    if os.path.isfile(filename):
        return pd.read_csv(filename)

    else:
        sql = '''
                SELECT *
                FROM customers
                JOIN payment_types USING (payment_type_id)
                JOIN contract_types USING (contract_type_id)
                JOIN internet_service_types USING (internet_service_type_id);
                '''

        df = pd.read_sql(sql, get_connection('telco_churn'))

        df.to_csv(filename, index=False)

        return df


