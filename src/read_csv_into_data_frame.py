import pandas as pd
import csv

def read_csv_into_data_frame(filename):
    df = pd.read_csv(filename, quoting = csv.QUOTE_NONE)

    # Fix the first and the last entries, they both have an extra quote
    df['TFF Match ID'] = df['TFF Match ID'].apply(lambda x: int(x[1:]))
    df['Deplasman skor'] = df['Deplasman skor'].apply(lambda x: int(x[:-1]))

    # Convert dates to datetime format
    df['Tarih'] = pd.to_datetime(df['Tarih'], format='%Y-%m-%d %H:%M:%S')

    return df
