import pandas as pd
import errno
import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def csv_to_dataframe(filepath):
    try:
        open(filepath)
    except:
        raise IOError('Incorrect Filepath')

    dataframe = pd.read_csv(filepath)
    return dataframe

def merge_dataframe(dataframe1, dataframe2, column_name):
    if column_name in dataframe1 and column_name in dataframe2:
        df = pd.merge(dataframe1, dataframe2, on=column_name)
        return df
    else:
        raise KeyError('some column(s) in the list are not present in the dataframe')

def dtype_category(dataframe, column_list):
    if set(column_list).issubset(dataframe.columns):
        for col in column_list:
            dataframe[col] = dataframe[col].astype('category')
            return dataframe
    else:
        raise KeyError('some column(s) in the list are not present in dataframe')

def centre_and_scale(dataframe, column_list):
    from sklearn.preprocessing import RobustScaler
    scaler = RobustScaler()

    if set(column_list).issubset(dataframe.columns):
        dataframe[column_list] = scaler.fit_transform(dataframe[column_list])
        return dataframe
    else:
        raise KeyError('some column(s) in the list are not present in dataframe')

def label_encoder(dataframe, column_list):
    from sklearn.preprocessing import LabelEncoder
    le = LabelEncoder()
    if set(column_list).issubset(dataframe.columns):
        dataframe[column_list] = dataframe[column_list].apply(le.fit_transform)
        return dataframe
    else:
        raise KeyError('some column(s) in the list are not present in the dataframe')

def one_hot_encoder(dataframe, column_list):
    if set(column_list).issubset(dataframe.columns):
        return pd.get_dummies(dataframe[column_list], drop_first=True)
    else:
        raise KeyError('some column(s) in the list are not present in the dataframe')

def skewness(dataframe, column_list):
    if set(column_list).issubset(dataframe.columns):
        return list(dataframe[column_list].skew())
    else:
        raise KeyError('some column(s) in the list are not present in the dataframe')

def sqrt_transform(dataframe, column_list):
    if set(column_list).issubset(dataframe.columns):
        transformed = dataframe[column_list].apply(np.sqrt)
        transformed_list = []
        for key in transformed:
            transformed_list.append(transformed[key])
        return transformed_list
    else:
        raise KeyError('some column(s) in the list are not present in the dataframe')

def plots(dataframe, column_list):
    transformed_list = sqrt_transform(dataframe)
    transformed = pd.DataFrame(data=transformed_list).T
    for col in column_list:
        plt.figure(figsize=(20,10))
        plt.subplot(221)
        plt.title('Original distribution : {}'.format(col))
        sns.distplot(dataframe[col], fit=norm, kde=False)

        plt.subplot(222)
        plt.title('Transformed distribution : {}'.format(col))
        sns.distplot(transformed[col], fit=norm, kde=False)

        plt.subplot(223)
        plt.title('Original boxplot : {}'.format(col))
        sns.boxplot(x=col, data=dataframe)

        plt.subplot(224)
        plt.title('Transformed boxplot : {}'.format(col))
        sns.boxplot(x=col, data=transformed)
        plt.show()
