import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder, FunctionTransformer
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer

# Define column categories
columns_to_drop = ['ID', 'Year_Birth', 'Kidhome', 'Teenhome', 'Dt_Customer', 'Marital_Status', 'Z_CostContact', 'Z_Revenue']
numerical_columns = ['Income', 'MntWines', 'MntFruits', 'MntMeatProducts', 'MntFishProducts', 'MntSweetProducts',
                     'MntGoldProds', 'NumDealsPurchases', 'NumWebPurchases', 'NumCatalogPurchases', 'NumStorePurchases',
                     'NumWebVisitsMonth', 'Age', 'Total_Children', 'Total_Household_Size',
                     'Total_Spending', 'Total_Purchase_Num', 'Discount_Dependency', 'Loyalty_Months',
                     'Campaign_Response_Rate', 'Shopping_Frequency']
categorical_columns = ['Education', 'Marital_Status_Grouped']

def preprocess_data(df, numerical_columns, categorical_columns, columns_to_drop):
    """
    Preprocesses the input DataFrame using a predefined pipeline.

    Args:
        df (pd.DataFrame): The input DataFrame.
        numerical_columns (list): List of numerical column names.
        categorical_columns (list): List of categorical column names.
        columns_to_drop (list): List of columns to drop.

    Returns:
        pd.DataFrame: The preprocessed DataFrame.
    """

    def remove_outliers(df):
        if 'Income' not in df.columns:
            print("Warning: 'Income' column not found. Skipping outlier removal.")
            return df
        income_threshold = df['Income'].quantile(0.999)
        df_filtered = df[df['Income'] <= income_threshold].reset_index(drop=True)
        print(f"Removed {df.shape[0] - df_filtered.shape[0]} income outliers.")
        return df_filtered

    pipeline = Pipeline(steps=[
        ('outlier_removal', FunctionTransformer(remove_outliers, validate=False)),
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
            ), validate=False)
        ),
        ('feature_engineering2', FunctionTransformer(
            lambda df: df.assign(
                Total_Household_Size=(df['Marital_Status'].isin(['Together', 'Married'])).astype(int) + 1 + df['Total_Children'],
                Total_Spending=df[['MntWines', 'MntFruits', 'MntMeatProducts', 'MntFishProducts', 'MntSweetProducts', 'MntGoldProds']].sum(axis=1),
                Total_Purchase_Num=df[['NumWebPurchases', 'NumCatalogPurchases', 'NumStorePurchases']].sum(axis=1),
            ), validate=False)
        ),
        ('feature_engineering3', FunctionTransformer(
            lambda df: df.assign(
                Discount_Dependency=np.where(
            df['Total_Purchase_Num'] > 0, 
            df['NumDealsPurchases'] / df['Total_Purchase_Num'], 
            0  # Set to 0 when Total_Purchase_Num is zero
        ),
                Loyalty_Months=((pd.to_datetime('today') - pd.to_datetime(df['Dt_Customer'], format='%d-%m-%Y')).dt.days // 30),
                Campaign_Response_Rate=df[['AcceptedCmp1', 'AcceptedCmp2', 'AcceptedCmp3', 'AcceptedCmp4', 'AcceptedCmp5', 'Response']].sum(axis=1) / 6,
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

    df_featured = pipeline.fit_transform(df)

    transformer = pipeline.named_steps['preprocessing']
    numerical_names = numerical_columns
    categorical_encoded_names = transformer.named_transformers_['cat'].get_feature_names_out(categorical_columns)

    final_columns = numerical_names + list(categorical_encoded_names)

    passthrough_columns = [col for col in df.columns if col not in numerical_columns and col not in categorical_columns and col not in columns_to_drop]

    final_columns = final_columns + passthrough_columns

    processed_df = pd.DataFrame(df_featured, columns=final_columns)

    # Store the fitted pipeline as an attribute of the function
    preprocess_data.pipeline = pipeline

    return processed_df