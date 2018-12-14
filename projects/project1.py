import src
import csv
import datetime
import pandas as pd

U21 = 'U21 Ligi'
BGL = 'Bölgesel Amatör Lig'

EFSOLAR = set(['ÖMER KİBİROĞLU', 'MERTCAN YILMAZ', 'MÜCAHİD ADEM ÇELEBİ'])

FILENAME = src.DEFAULT_MATCH_ARCHIVE
print('Archive filename:', FILENAME)

DF = src.read(FILENAME, silent=True)

START_DATETIME = datetime.datetime(2018,8,1,0,0,0)
END_DATETIME = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')

def yardimci_hakem_list(df=DF, start=START_DATETIME, end=END_DATETIME):
    # Remove matches that are not needed
    df = df.drop(df[df['Tarih'] < start].index)
    df = df.drop(df[df['Tarih'] > end  ].index)

    names = list(   set(df['AR1'].unique()) or \
                    set(df['AR2'].unique()))
    return names, df

# Drop old matches, get unique referee list
hakem_names, df = yardimci_hakem_list(DF)

def mac_sayisi(hakem_name, league_name, df=DF):
#   print(df[df['AR1'].str.contains(hakem_name)])
#    print(df[df['AR2'].str.contains(hakem_name)])

    df = df[ (df['AR1'].str.contains(hakem_name)) | \
                (df['AR2'].str.contains(hakem_name)) ]
    df = df[ df['Organizasyon'].str.contains(league_name) ]
    return len(df.index)

df_mac_count =pd.DataFrame()
for name in hakem_names:
    BGL_count = mac_sayisi(name, BGL, df)
    U21_count = mac_sayisi(name, U21, df)
    if BGL_count is not 0 and U21_count is not 0:
        df_mac_count = df_mac_count.append(\
            {'name': name, '#BGL': BGL_count, '#U21': U21_count}, \
            ignore_index=True)

df_mac_count = df_mac_count.astype({'name': str, '#BGL': int, '#U21': int})
df_efso_mac_count = df_mac_count[df_mac_count['name'].isin(EFSOLAR)]

print(df_mac_count.sort_values(by=['#BGL']))
print(df_mac_count['#BGL'].median(), df_mac_count['#U21'].median())
print(df_efso_mac_count)
