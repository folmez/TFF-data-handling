import src
import datetime

# Default years
START, END = src.START_YEAR, src.END_YEAR
ARCHIVE_FILENAME = src.DEFAULT_MATCH_ARCHIVE
DF = src.read_matches(ARCHIVE_FILENAME, silent=True)

def leagues(start=START, end=END, df=DF):

    # Leagues generally are on a break in July
    start_datetime = datetime.datetime(start,7,1,0,0,0)
    end_datetime = datetime.datetime(end,7,1,0,0,0)

    # Remove matches that are not needed
    df = df.drop(df[df['Tarih'] < start_datetime].index)
    df = df.drop(df[df['Tarih'] > end_datetime].index)

    print(df['Organizasyon'].unique())
    return list(df['Organizasyon'].unique())

def referees(search_str, df=DF):
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
                    set(df_dort['Dorduncu Hakem'].unique()))
    print(names)
    return names

def deplasman_skor(filename, df=DF):
    print(df['Deplasman skor'].unique())
