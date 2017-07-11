from sklearn import preprocessing as pp
import pandas as pd
import numpy as np
from pandas import DataFrame, Series
def csv_to_dataframe(filepath):
    try:
        df = pd.read_csv(filepath)
        return df
    except IOError:
        raise 'FileNotFound'

def merge_dataframe(dataframe1, dataframe2, column_name):
    try:
        return pd.merge(dataframe1,dataframe2, on=column_name)
    except KeyError:
        raise 'Column not found'

def dtype_category(dataframe, column_list):
    try:
        for cols in column_list:
            dataframe[cols] = dataframe[cols].astype('category')
        return dataframe
    except KeyError:
        raise 'Column not found'

def centre_and_scale(dataframe, column_list):
    try:
        for cols in column_list:
            dataframe[cols] = pp.scale(dataframe[cols],copy = False)
        return dataframe
    except KeyError:
        raise 'Column not found'

def label_encoder(dataframe, column_list):
    try:
        le = pp.LabelEncoder()
        for cols in column_list:
            dataframe[cols] = le.fit_transform(dataframe[cols])
        return dataframe
    except KeyError:
        raise 'Column not found'

def one_hot_encoder(dataframe, column_list):
    try:
        return pd.get_dummies(dataframe,columns = column_list)
    except KeyError:
        raise 'Column not found'

def skewness(dataframe, column_list):
    my_skew_list = []
    try:
        my_skew_list = [x for x in dataframe[column_list].skew()]
        return my_skew_list
    except KeyError:
        raise 'Column not found'

def sqrt_transform(dataframe, column_list):
    my_sqrt_list = []
    try:
        my_sqrt_list = [x for x in np.sqrt(dataframe[column_list])]
        return my_sqrt_list
    except KeyError:
        raise 'Column not found'

def plots(dataframe, column_list):
    try:
        original_sub = dataframe.loc[:,column_list]
        df = centre_and_scale(dataframe,column_list)
        df_sub = df.loc[:,column_list]
        sub_cols = list(df_sub.columns)
        cols = list(original_sub.columns)
        col_length = len(sub_cols)
        for i in range(0,col_length):
            figure = plt.figure(figsize=(30,10))

            plt.subplot(221)
            plt.boxplot(original_sub.iloc[:,i],0,'rs',0)
            plt.title("Original " + cols[i])
            plt.xlabel("Value")
            plt.ylabel(cols[i])

            plt.subplot(222)
            plt.boxplot(df_sub.iloc[:,i], 0, 'rs', 0)
            plt.title("Transformed "+sub_cols[i])
            plt.xlabel("Value")
            plt.ylabel(sub_cols[i])

            plt.subplot(223)
            plt.hist(original_sub.iloc[:,i], bins=10)
            plt.title("Original "+cols[i])
            plt.xlabel("Value")
            plt.ylabel(cols[i])
            plt.show()

            plt.subplot(224)
            plt.hist(df_sub.iloc[:,i], bins=10)
            plt.title("Transformed "+sub_cols[i])
            plt.xlabel("Value")
            plt.ylabel(sub_cols[i])
            plt.show()

    except KeyError:
        raise 'Column does not exist or column in not categorical'
