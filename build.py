import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
import os


def csv_to_dataframe(filepath):
    if os.path.exists(filepath):
        df = pd.read_csv(filepath)
    else:
        raise IOError('Please provide valid file path')
    return df


def merge_dataframe(dataframe1, dataframe2, column_name):
    if column_name not in dataframe1.columns:
        raise KeyError

    if column_name not in dataframe2.columns:
        raise KeyError

    dataframe = dataframe1.merge(dataframe2, on=column_name, how='outer')
    return dataframe


def dtype_category(dataframe, column_list):
    for column in column_list:
        if column not in dataframe.columns:
            raise KeyError
    for column in column_list:
        dataframe.loc[:,column] = dataframe.loc[:,column].astype('category')
    return dataframe


def centre_and_scale(dataframe, column_list):
    for column in column_list:
        if column not in dataframe.columns:
            raise KeyError
    for column in column_list:
        dataframe[column] = dataframe[column].fillna(np.nanmedian(dataframe[column]))
        dataframe[column] = preprocessing.scale(dataframe[column])
    return dataframe


def label_encoder(dataframe, column_list):
    for column in column_list:
        if column not in dataframe.columns:
            raise KeyError
    le = preprocessing.LabelEncoder()
    return dataframe[column_list].apply(le.fit_transform)


def one_hot_encoder(dataframe, column_list):
    return pd.get_dummies(dataframe, columns = column_list)


def skewness(dataframe, column_list):
    for column in column_list:
        if column not in dataframe.columns:
            raise KeyError
    skew_list = []
    for column in column_list:
        dataframe[column] = dataframe[column].fillna(np.nanmedian(dataframe[column]))
        skew_list.append(dataframe[column].skew())
    return skew_list



def sqrt_transform(dataframe, column_list):
    sqrt_data = []
    for column in column_list:
        if column not in dataframe.columns:
            raise KeyError
    for column in column_list:
        dataframe[column] = dataframe[column].fillna(np.nanmedian(dataframe[column]))
        sqrt_data.append(np.sqrt(dataframe[column]))
    return sqrt_data


def plots(dataframe, column_list):
    for column in column_list:
        if column not in dataframe.columns:
            raise KeyError
    original_df = dataframe.loc[:,column_list]
    trans_df = centre_and_scale(dataframe,column_list).loc[:,column_list]

    trans_cols = list(trans_df.columns)
    original_cols = list(original_df.columns)
    col_length = len(trans_cols)


    for i in range(0,col_length):
        figure = plt.figure(figsize=(30,10))

        plt.subplot(221)
        plt.boxplot(original_df[column_list[i-1]],0,'rs',0)
        plt.title("Original " + original_cols[i])
        plt.xlabel("Value")
        plt.ylabel(original_cols[i])

        plt.subplot(222)
        plt.boxplot(trans_df[column_list[i]], 0, 'rs', 0)
        plt.title("Transformed "+trans_cols[i])
        plt.xlabel("Value")
        plt.ylabel(trans_cols[i])

        plt.subplot(223)
        plt.hist(original_df[column_list[i]], bins=20)
        plt.title("Original "+original_cols[i])
        plt.xlabel("Value")
        plt.ylabel(original_cols[i])
        plt.show()

        plt.subplot(224)
        plt.hist(trans_df[column_list[i]], bins=20)
        plt.title("Transformed "+trans_cols[i])
        plt.xlabel("Value")
        plt.ylabel(trans_cols[i])
plt.show()
