# Import libraries
import pandas as pd
import numpy as np
import os
from pydataset import data

# Acquire
from env import host, user, password


# Create helper function to get the necessary connection url
def get_connection(db_name):
    '''
    This function uses my info from my env file to
    create a connection url to access the Codeup db.
    '''
    return f'mysql+pymysql://{user}:{password}@{host}/{db_name}'

# Create function to retrieve telco_churn data

def get_telco_churn_data():
    '''
    This function reads in the Telco Churn data from the Codeup db
    and returns a pandas DataFrame with all columns.
    '''
    sql_query = '''
    SELECT *
    FROM customers
    JOIN contract_types ON customers.contract_type_id = contract_types.contract_type_id
    JOIN payment_types ON customers.payment_type_id = payment_types.payment_type_id
    JOIN internet_service_types ON customers.internet_service_type_id = internet_service_types.internet_service_type_id
    '''
    return pd.read_sql(sql_query, get_connection('telco_churn'))

# Now, you can simply call get_telco_churn_data function to retrieve the data.
df = get_telco_churn_data()

# To inspect the first few rows of the DataFrame, you can use the head function.
print(df.head())n pd.read_sql(sql_query, get_connection('telco_churn'))

    
    
    
