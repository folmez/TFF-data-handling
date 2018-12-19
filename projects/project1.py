import src
import helpers

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

# Drop old matches
DF_matches = helpers.drop_old_matches(DF_matches, START_DATETIME, END_DATETIME)

# Get unique assistant referee ID list
hakem_IDs = helpers.get_unique_AR_list(DF_matches)

# Drop out of area referees
hakem_IDs = helpers.drop_out_of_area_referees(hakem_IDs, DF_refs, AREAS)

df_mac_count = pd.DataFrame()
for id in hakem_IDs:
    BAL_count = helpers.get_mac_count(id, DF_matches, BAL)
    U21_count = helpers.get_mac_count(id, DF_matches, U21)
    if BAL_count is not 0 and U21_count is not 0:
        df_mac_count = df_mac_count.append(\
            {'id': id, 'name': src.tff_hakem_id_to_name(id, DF_refs), \
            '#BAL': BAL_count, '#U21': U21_count}, \
            ignore_index=True)

df_mac_count = df_mac_count.astype({'id': int, 'name': str, '#BAL': int, '#U21': int})
df_efso_mac_count = df_mac_count[df_mac_count['name'].isin(EFSOLAR)]

print(df_mac_count.sort_values(by=['#BAL']))
print(df_mac_count['#BAL'].median(), df_mac_count['#U21'].median())
print(df_efso_mac_count)

print(df_mac_count.sort_values(by=['#U21']))
