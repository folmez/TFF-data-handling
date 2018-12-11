import pandas as pd
import csv

def read_csv_into_data_frame(filename, silent=False):
    # Load the csv file
    # 1) Dort ID and Stad ID are sometimes inputted as [], pandas doesn't
    # recognize this.
    df = pd.read_csv(filename, dtype={'Dort ID': object, 'Stad ID': object},\
                                                    quoting = csv.QUOTE_NONE)

    # Replace [] with -1 in the Dort ID and Stad ID columns
    df['Dort ID'] = df['Dort ID'].replace({"[]":"-1"})
    df['Stad ID'] = df['Stad ID'].replace({"[]":"-1"})
    df['Dort ID'] = df['Dort ID'].apply(lambda x: int(x))
    df['Stad ID'] = df['Stad ID'].apply(lambda x: int(x))

    # Fix the first and the last entries, they both have an extra quote
    df['TFF Match ID'] = df['TFF Match ID'].apply(lambda x: int(x[1:]))
    df['Deplasman skor'] = df['Deplasman skor'].apply(lambda x: int(x[:-1]))

    # Convert dates to datetime format
    df['Tarih'] = pd.to_datetime(df['Tarih'], format='%Y-%m-%d %H:%M:%S')

    if not silent:
        print(df.head())

    return df
