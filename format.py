import pandas as pd
import numpy as np
from openpyxl import Workbook


def reformat(file):
    df = pd.DataFrame(pd.read_csv(file))
    df['mobile'] = df['mobile'].astype(str)
    # find all the elements in a column of length 10
    # and replace them with the mean of the column
    for i in range(len(df['mobile'])):
        df['mobile'][i] = df['mobile'][i].strip(".0")
        # print(df['mobile'][i])
        if len(df['mobile'][i]) == 9:
            # concatenate the prefix and the number
            df['mobile'][i] = "27" + df['mobile'][i]
            # print(df['mobile'][i])
    return (df)


def clean(dataframe):
    df = dataframe
    df['mobile'] = df['mobile'].astype(str)
    for i in range(len(df['mobile'])):
        if len(df['mobile'][i]) <= 10:
            # remove the entire row
            df = df.drop(i)
    return df


def df_csv(dataframe):
    # save the dataframe as a csv file
    dataframe.to_csv('data.csv')


if __name__ == '__main__':
    df = reformat('Database1.csv')
    df_clean = clean(df)
    df_csv(df_clean)
