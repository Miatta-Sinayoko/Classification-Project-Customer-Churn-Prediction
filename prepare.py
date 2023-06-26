import pandas as pd
from sklearn.model_selection import train_test_split

def prep_telco_churn(df):
    '''
    This function takes in the DataFrame from get_telco_churn_data
    and returns the DataFrame with preprocessing applied 
    '''
    # Drop duplicated columns and rows
    df = df.loc[:, ~df.columns.duplicated()]
    df.drop_duplicates(inplace=True)

    # Replace ' ' in 'total_charges' column with '0' and change its data type to float
    df.total_charges = df.total_charges.replace(' ', '0').astype(float)

    # Change data type for boolean columns
    for col in ['churn', 'partner', 'dependents', 'phone_service']:
        df[col] = df[col].map({'No': 0, 'Yes': 1})

    return df

def split_data(df):
    '''
    This function takes in a DataFrame and returns train, validate, and test DataFrames.
    '''
    # Create train_validate and test datasets
    train_validate, test = train_test_split(df, test_size=.2, random_state=123, stratify=df.churn)

    # Split train_validate into train and validate datasets
    train, validate = train_test_split(train_validate, test_size=.3, random_state=123, stratify=train_validate.churn)

    return train, validate, test
