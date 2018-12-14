#import src
import src
import datetime

# Default years
START, END = src.START_YEAR, src.END_YEAR
FILENAME = src.DEFAULT_MATCH_ARCHIVE

def leagues(filename=FILENAME, start=START, end=END):
    df = src.read(filename, silent=True)

    # Leagues generally are on a break in July
    start_datetime = datetime.datetime(start,7,1,0,0,0)
    end_datetime = datetime.datetime(end,7,1,0,0,0)

    # Remove matches that are not needed
    df = df.drop(df[df['Tarih'] < start_datetime].index)
    df = df.drop(df[df['Tarih'] > end_datetime].index)

    print(df['Organizasyon'].unique())

def referees(search_str, filename=FILENAME):
    df = src.read(filename, silent=True)

    # Remove matches that are not needed
    df_hakem = df[df['Hakem'].str.contains(search_str)]
    df_ar1 = df[df['AR1'].str.contains(search_str)]
    df_ar2 = df[df['AR2'].str.contains(search_str)]

    # Remove nan rows, they cause a big in string search
    df = df.dropna(how='any')
    df_dort = df[df['Dorduncu Hakem'].str.contains(search_str)]

    names = list(   set(df_hakem['Hakem'].unique()) or \
                    set(df_ar1['AR1'].unique()) or \
                    set(df_ar2['AR2'].unique()) or \
                    set(df_dort['Dorduncu Hakem'].unique())
                )
    print(names)

def deplasman_skor(filename):
    df = src.read_csv_into_data_frame(filename)

    print(df['Deplasman skor'].unique())
