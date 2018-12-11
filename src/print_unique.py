#import src
import src
import datetime

# Default years
START, END = 1000, 3000

def leagues(filename, start=START, end=END):
    df = src.read_csv_into_data_frame(filename)

    # Leagues generally are on a break in July
    start_datetime = datetime.datetime(start,7,1,0,0,0)
    end_datetime = datetime.datetime(end,7,1,0,0,0)

    # Remove matches that are not needed
    df = df.drop(df[df['Tarih'] < start_datetime].index)
    df = df.drop(df[df['Tarih'] > end_datetime].index)

    print(df['Organizasyon'].unique())

def deplasman_skor(filename):
    df = src.read_csv_into_data_frame(filename)

    print(df['Deplasman skor'].unique())
