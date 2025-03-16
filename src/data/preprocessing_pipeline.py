# preprocessing_pipeline.py
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import FunctionTransformer
import numpy as np

def create_preprocessing_pipeline():
    columns_to_drop = ['ID', 'Year_Birth', 'Kidhome', 'Teenhome', 'Dt_Customer', 'Marital_Status']
    columns_to_exclude = ['Recency', 'AcceptedCmp3', 'AcceptedCmp4', 'AcceptedCmp5', 'AcceptedCmp1', 'AcceptedCmp2', 'Complain', 'Response', 'Income']
    numerical_columns = ['MntWines', 'MntFruits', 'MntMeatProducts', 'MntFishProducts', 'MntSweetProducts', 'MntGoldProds', 'NumDealsPurchases', 'NumWebPurchases', 'NumCatalogPurchases', 'NumStorePurchases', 'NumWebVisitsMonth', 'Z_CostContact', 'Z_Revenue', 'Age', 'Total_Children', 'Total_Household_Size', 'Total_Spending', 'Loyalty_Months', 'Campaign_Response_Rate', 'Shopping_Frequency']
    categorical_columns = ['Education', 'Marital_Status_Grouped']

    pipeline = Pipeline(steps=[
        ('feature_engineering', FunctionTransformer(
            lambda df: df.assign(
                Age=2024 - df['Year_Birth'],
                Total_Children=df['Kidhome'] + df['Teenhome'],
                Marital_Status_Grouped=df['Marital_Status'].map({
                    'Single': 'Single_Household',
                    'Divorced': 'Single_Household',
                    'Widow': 'Single_Household',
                    'Alone': 'Single_Household',
                    'Together': 'Couples',
                    'Married': 'Couples',
                    'Absurd': 'Unknown',
                    'YOLO': 'Unknown'
                }),
                Total_Household_Size=(
                    (df['Marital_Status'].isin(['Together', 'Married'])).astype(int) + 1 + df['Total_Children']
                ),
                Total_Spending=df[['MntWines', 'MntFruits', 'MntMeatProducts',
                                   'MntFishProducts', 'MntSweetProducts', 'MntGoldProds']].sum(axis=1),
                Loyalty_Months=((pd.to_datetime('today') - pd.to_datetime(df['Dt_Customer'], format='%d-%m-%Y')).dt.days // 30),
                Campaign_Response_Rate=df[['AcceptedCmp1', 'AcceptedCmp2', 'AcceptedCmp3', 'AcceptedCmp4', 'AcceptedCmp5']].sum(axis=1) / 5,
                Shopping_Frequency=df[['NumDealsPurchases', 'NumWebPurchases', 'NumCatalogPurchases', 'NumStorePurchases']].sum(axis=1)
            ).drop(columns_to_drop, axis=1), validate=False)
        ),
        ('preprocessing', ColumnTransformer(
            transformers=[
                ('num', Pipeline([
                    ('imputer', SimpleImputer(strategy='median')),
                    ('scaler', StandardScaler())
                ]), numerical_columns),
                ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_columns)
            ],
            remainder='passthrough'
        ))
    ])
    return pipeline