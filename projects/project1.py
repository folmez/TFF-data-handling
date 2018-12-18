import src
import csv
import datetime
import pandas as pd

U21 = 'U21 Ligi (PAF Takımı)'
BAL = 'SporToto Bölgesel Amatör Lig (BAL Takımı)'

AREAS = set(['İSTANBUL', 'EDİRNE', 'TEKİRDAĞ', 'KIRKLARELİ'])

EFSOLAR = set(['ÖMER KİBİROĞLU', 'MERTCAN YILMAZ', 'MÜCAHİD ADEM ÇELEBİ'])

MATCH_ARCHIVE = src.DEFAULT_MATCH_ARCHIVE
REF_ARCHIVE = src.DEFAULT_REFEREE_ARCHIVE
print('Match archive:', MATCH_ARCHIVE)
print('Referee archive:', REF_ARCHIVE)

DF_matches = src.read_matches(MATCH_ARCHIVE, silent=True)
DF_refs = src.read_referees(REF_ARCHIVE, silent=True)

START_DATETIME = datetime.datetime(2018,8,1,0,0,0)
END_DATETIME = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')

def drop_old_matches(df=DF_matches, start=START_DATETIME, end=END_DATETIME):
    # Remove matches that are not needed
    df = df.drop(df[df['Tarih'] < start].index)
    df = df.drop(df[df['Tarih'] > end  ].index)

    names = list(   set(df['AR1'].unique()) or \
                    set(df['AR2'].unique()))
    return names, df

####
###
### MOVE FROM NAMES TO HAKEM IDs
###
###

# Drop old matches, get unique referee list
hakem_names, DF_matches = drop_old_matches(DF_matches)

def drop_out_of_area_referees(hakem_names, area_set = AREAS):
    for n in hakem_names:
        print(n, src.name_to_area(n, DF_refs))
#        if src.name_to_area(n, DF_refs) in area_set:
#            print(n)
    # return [n for n in hakem_names if src.name_to_area(n, DF_refs) in area_set]

drop_out_of_area_referees(hakem_names)

def mac_sayisi(hakem_name, df=DF_matches, silent=True):
#   print(df[df['AR1'].str.contains(hakem_name)])
#    print(df[df['AR2'].str.contains(hakem_name)])

    df = df[ (df['AR1'].isin([hakem_name])) | \
                (df['AR2'].isin([hakem_name])) ]
    df_u21 = df[ df['Organizasyon'].isin([U21]) ]
    df_bal = df[ df['Organizasyon'].isin([BAL]) ]
    if not silent:
        print(df)
    return len(df_u21.index), len(df_bal.index)

# mac_sayisi('SEMİH KOCA', df, silent=False)

df_mac_count =pd.DataFrame()
for name in hakem_names:
    BAL_count, U21_count = mac_sayisi(name, DF_matches)
    if BAL_count is not 0 and U21_count is not 0:
        df_mac_count = df_mac_count.append(\
            {'name': name, '#BAL': BAL_count, '#U21': U21_count}, \
            ignore_index=True)

df_mac_count = df_mac_count.astype({'name': str, '#BAL': int, '#U21': int})
df_efso_mac_count = df_mac_count[df_mac_count['name'].isin(EFSOLAR)]

print(df_mac_count.sort_values(by=['#BAL']))
print(df_mac_count['#BAL'].median(), df_mac_count['#U21'].median())
print(df_efso_mac_count)

print(df_mac_count.sort_values(by=['#U21']))
